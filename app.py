import streamlit as st
import json

from utils.url_utils import is_valid_url
from crawler.crawler import crawl_docs
from extractor.module_builder import extract_modules


st.set_page_config(page_title="XtracT", layout="wide")

st.title("XtracT: Module Extraction AI Agent")

input_col, status_col = st.columns([2, 1])

with input_col:
    urls_input = st.text_area(
        "Documentation URLs",
        height=180,
        placeholder="Enter URLs (one per line)..."
    )

with status_col:
    st.markdown("### Status")
    status_box = st.empty()
    status_box.info("Waiting for input")
    download_placeholder = st.empty()

if st.button("Extract Modules"):
    urls = [u.strip() for u in urls_input.split("\n") if u.strip()]

    status_box.warning("Validating URLs")
    valid_urls = [u for u in urls if is_valid_url(u)]
    invalid_urls = [u for u in urls if not is_valid_url(u)]

    if invalid_urls:
        st.error(f"Invalid URLs: {invalid_urls}")

    if not valid_urls:
        status_box.error("No valid URLs provided")
        st.stop()

    status_box.warning("Crawling documentation")
    pages = crawl_docs(valid_urls)

    if not pages:
        status_box.error("No content could be extracted")
        st.stop()

    status_box.warning("Extracting modules and submodules")
    result = extract_modules(pages)

    status_box.success("Extraction complete")

    json_str = json.dumps(result, indent=2, ensure_ascii=False)

    download_placeholder.download_button(
        label="Download JSON",
        data=json_str,
        file_name="module_extraction.json",
        mime="application/json"
    )

    st.markdown("## Results")

    for item in result:
        with st.expander(item["url"], expanded=False):
            if item["status"] == "unsupported":
                st.error(item["reason"])
            else:
                st.json(item["modules"])
