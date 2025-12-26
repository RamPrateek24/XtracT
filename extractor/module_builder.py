def extract_modules(pages):
    output = []

    for page in pages:
        if not page.get("extractable"):
            output.append({
                "url": page["url"],
                "status": "unsupported",
                "reason": "No meaningful documentation content available in server-rendered HTML"
            })
            continue

        modules = []
        current_module = None

        for tag in page["content"].find_all(["h2", "h3", "p", "li"]):
            if tag.name == "h2":
                current_module = {
                    "module": tag.get_text(strip=True),
                    "Description": "",
                    "Submodules": {}
                }
                modules.append(current_module)

            elif tag.name == "h3" and current_module:
                sub = tag.get_text(strip=True)
                current_module["Submodules"][sub] = ""

            elif tag.name in ["p", "li"] and current_module:
                text = tag.get_text(strip=True)
                if current_module["Submodules"]:
                    last = list(current_module["Submodules"].keys())[-1]
                    current_module["Submodules"][last] += " " + text
                else:
                    current_module["Description"] += " " + text

        for m in modules:
            m["Description"] = m["Description"].strip()
            for k in m["Submodules"]:
                m["Submodules"][k] = m["Submodules"][k].strip()

        output.append({
            "url": page["url"],
            "status": "extracted",
            "modules": modules
        })

    return output
