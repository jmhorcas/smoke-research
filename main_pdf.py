import slate3k


PDF_FILE = 'Horcas2016_CS.pdf'


def extract_text(pdf_filepath: str) -> str:
    with open(pdf_filepath, 'rb') as f:
        pdf = slate3k.PDF(f)
    text = "\n\n".join(pdf)
    return text


if __name__ == '__main__':
    text = extract_text(PDF_FILE)
    with open('output.txt', 'w+', encoding='utf-8') as f:
        f.write(text)
