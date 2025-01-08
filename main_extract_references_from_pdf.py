import re
import PyPDF2

def extract_references(pdf_path):
    """Extract the list of references from a scientific article in PDF format.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: A list of extracted references (strings).
    """
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)

            # Extract all text from the PDF
            full_text = "".join(page.extract_text() for page in reader.pages)

        # Normalize the text (e.g., handle common encodings and spaces)
        full_text = re.sub(r'\s+', ' ', full_text).strip()

        # Look for the start of the references section
        #references_start = re.search(r'(References|Bibliography|Works Cited)', full_text, re.IGNORECASE)
        print(full_text)
        references_start = re.search(r'(References)', full_text, re.IGNORECASE)
        if not references_start:
            raise ValueError("Could not find the references section in the document.")

        # Extract text from the references section onwards
        references_text = full_text[references_start.end():]

        # Split into individual references using common patterns (e.g., numbered, bullet points, etc.)
        references = re.split(r'\n\d+\.\s|\n\[\d+\]|\n[A-Z]\.', references_text)

        # Filter out invalid or empty entries
        references = [ref.strip() for ref in references if len(ref.strip()) > 20]

        return references

    except Exception as e:
        print(f"Error extracting references: {e}")
        return []

# Example usage
if __name__ == "__main__":
    pdf_path = "Horcas2016_CS.pdf"  # Replace with your PDF file path
    references = extract_references(pdf_path)

    if references:
        print("Extracted References:")
        for i, ref in enumerate(references, start=1):
            print(f"{i}. {ref}")
    else:
        print("No references found.")
