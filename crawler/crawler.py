import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque


def crawl_docs(start_urls, max_pages=30):
    visited = set()
    queue = deque(start_urls)
    pages = []

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ModuleExtractor/1.0)"
    }

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                continue
        except:
            continue

        visited.add(url)
        soup = BeautifulSoup(response.text, "html.parser")

        main = (
            soup.find("main") or
            soup.find("article") or
            soup.find("div", id="content") or
            soup.find("div", class_="content") or
            soup.body
        )

        text = main.get_text(strip=True) if main else ""
        headings = soup.find_all(["h1", "h2", "h3", "h4"])

        extractable = bool(text and len(text) > 300 and headings)

        pages.append({
            "url": url,
            "content": main,
            "extractable": extractable
        })

        base_domain = urlparse(url).netloc

        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            parsed = urlparse(link)

            if parsed.netloc == base_domain and link not in visited:
                if not link.lower().endswith((".pdf", ".jpg", ".png", ".zip")):
                    queue.append(link)

    return pages
