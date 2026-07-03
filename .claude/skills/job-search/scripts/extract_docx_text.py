#!/usr/bin/env python3
"""Print the plain text of a .docx file to stdout. Usage: extract_docx_text.py <path-to-docx>"""
import sys
import zipfile
import re


def extract(path: str) -> str:
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    text = re.sub(r"<[^>]+>", " ", xml)
    return re.sub(r"\s+", " ", text).strip()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: extract_docx_text.py <path-to-docx>", file=sys.stderr)
        sys.exit(1)
    print(extract(sys.argv[1]))
