import argparse
import json
import sys

from utils.url_utils import is_valid_url
from crawler.crawler import crawl_docs
from extractor.module_builder import extract_modules


def main(urls):
    valid_urls = [url for url in urls if is_valid_url(url)]

    if not valid_urls:
        print("No valid URLs provided.")
        sys.exit(1)

    pages = crawl_docs(valid_urls)

    if not pages:
        print("No content could be extracted.")
        sys.exit(1)

    result = extract_modules(pages)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pulse – Module Extraction AI Agent"
    )

    parser.add_argument(
        "--urls",
        nargs="+",
        required=True,
        help="One or more documentation URLs"
    )

    args = parser.parse_args()
    main(args.urls)
