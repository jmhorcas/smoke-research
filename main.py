import json

from crossref.restful import Works
import scholarly
#from scholarly import scholarly, ProxyGenerator


def google_scholar() -> None:
    # Set up a ProxyGenerator object to use free proxies
    # This needs to be done only once per session
    
    pg = scholarly.ProxyGenerator()
    pg.FreeProxies()
    scholarly.scholarly.use_proxy(pg)

    search_query = scholarly.scholarly.search_pubs('An approach for deploying and monitoring dynamic security policies')
    scholarly.scholarly.pprint(next(search_query))


def crossref() -> None:
    works = Works()
    result = works.doi('10.1016/J.COSE.2015.11.007')
    print(json.dumps(result, indent=4))

if __name__ == '__main__':
    google_scholar()
