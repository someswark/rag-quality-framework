from pathlib import Path
from pypdf import PdfReader


class PDFTextExtractor:

    def extract(self, pdf_path: Path) -> str:

        reader = PdfReader(str(pdf_path))

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

        return text