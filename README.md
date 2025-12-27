# XtracT: Module Extraction AI Agent 🧩
*(AI-powered documentation analyzer)*

XtracT is a Python-based system that automatically extracts **modules**, **submodules**, and their **descriptions** from documentation-based help websites.

It crawls documentation URLs, analyzes content hierarchy, and returns **structured JSON output** strictly derived from the documentation content.

I have added download option and status bar additionally to enhance user experience.

Note: I kept this repository public because I don’t have the collaborator’s user ID.

---

## 🎥 Demo Video

Approach explanation and working demo :  
https://drive.google.com/file/d/1eNu6PjzKUk8zrrug1TCcOS07j650y-6d/view?usp=sharing

---

## 🧠 Features

- 🌐 Accepts one or more documentation URLs as input  
- 🕷️ Recursively crawls relevant pages within the same domain  
- 📄 Extracts meaningful documentation content (ignores navigation & layout noise)  
- 🧩 Identifies:
  - Major documentation **modules**
  - Nested **submodules**
  - Detailed descriptions for both  
- 📦 Returns structured JSON in the specified format  
- ⚠️ Gracefully handles unsupported or JS-rendered documentation sites  
- 🖥️ Supports both **CLI** and **Streamlit UI**

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|--------|
| Python | Core programming language |
| Requests | HTTP crawling |
| BeautifulSoup4 | HTML parsing |
| Streamlit | Interactive web UI |
| JSON | Structured output |

---

## 📦 Installation

```bash
git clone <private-repo-url>
cd XtracT
pip install -r requirements.txt
```

---

## 🚀 Usage
Command Line Interface
```bash
python main.py --urls https://wordpress.org/documentation/
```

---

## Multiple URLs:
```bash
python main.py --urls https://wordpress.org/documentation/ https://help.zluri.com/
```

---

## Streamlit Web Interface
```bash
streamlit run app.py
```

---

## 🧱 Technical Architecture

```bash
Input URLs
→ Validation
→ Recursive Crawler
→ Content Extraction
→ Hierarchy Analysis
→ Module/Submodule Inference
→ JSON Output
```

---

## 📂 Key Components

- main.py – CLI entry point

- app.py – Streamlit UI

- crawler/crawler.py – Crawler

- extractor/module_builder.py – Extraction logic

- utils/url_utils.py – URL validation

---

## 🧪 Testing

Tested on at least **four documentation URLs**:

| URL | Result |
|-----|--------|
| https://wordpress.org/documentation/ | Extracted |
| https://www.chargebee.com/docs/2.0/ | Extracted |
| https://help.zluri.com/ | Extracted |
| https://support.neo.space/hc/en-us | Extracted |
| https://help.instagram.com/ | Unsupported |

---

## 🧩 Design Rationale

- Modular architecture

- Rule-based hierarchy detection

- Streamlit for fast demo

- JSON for interoperability

---

## 🧠 Assumptions

- Documentation uses semantic HTML

- Same-domain pages belong to one product

---

## ⚠️ Edge Case Handling

- Broken links skipped

- Empty pages ignored

- JS-rendered sites marked unsupported

---

## 🚫 Known Limitations

- JS-rendered documentation unsupported

- Login-protected sites unsupported

- Deep heading nesting may reduce accuracy

---


## 📌 Notes

- Repository is private as required

- Runs locally; no deployment needed

- Demo video provided separately

---
