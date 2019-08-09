# Internal imports

# External imports
import pdfbox
import scihub

# CONSTANTS

class PaperManager():
    """Manage papers in pdf, with DOI, etc."""

    def __init__(self):
        pass

    def extract_text(self, pdf_filename: str) -> str:
        """Extract txt from pdf using the pdfbox module."""
        p = pdfbox.PDFBox()
        text = p.extract_text(pdf_filename)
        return text

    def download_paper(self, paper_doi: str, pdf_filename: str):
        sh = scihub.SciHub()
        result = sh.fetch(paper_doi)
        with open(pdf_filename, 'wb+') as fd:
            fd.write(result['pdf'])
