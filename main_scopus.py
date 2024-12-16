import pybliometrics


pybliometrics.scopus.init()  # read API keys

# Document-specific information
from pybliometrics.scopus import AbstractRetrieval, CitationOverview


DOI = '10.1016/J.COSE.2015.11.007'
def scopus() -> None:
    ab = AbstractRetrieval(DOI)
    print(ab.title)
    print(ab.coverDate)
    print(ab.date_created)
    print(ab.confdate)
    year = ab.coverDate.split('-')[0]
    cites = CitationOverview([DOI], f'{year}-2024')
    print(cites)


if __name__ == '__main__':
    scopus()
