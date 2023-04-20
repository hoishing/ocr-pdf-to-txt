import fitz
from pathlib import Path

fname = Path("test.pdf")

with fitz.open(fname) as doc:
    with open(fname.with_suffix(".txt"), "wb") as f:
        for page in doc:  # iterate the document pages
            text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
            f.write(text)  # write text of page
