import scihub


DOI = '10.1016/J.COSE.2015.11.007'
TMP_FILE = 'paper.pdf'


def download_paper(paper_doi: str, pdf_filename: str):
        sh = scihub.SciHub()
        #result = sh.fetch(paper_doi)
        result = sh.download(paper_doi, path=pdf_filename)
        #with open(pdf_filename, 'wb+') as fd:
        #    fd.write(result['pdf'])

if __name__ == '__main__':
    download_paper(DOI, TMP_FILE)
