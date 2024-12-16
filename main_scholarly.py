import scholarly


def google_scholar() -> None:
    # Set up a ProxyGenerator object to use free proxies
    # This needs to be done only once per session
    
    pg = scholarly.ProxyGenerator()
    pg.FreeProxies()
    scholarly.scholarly.use_proxy(pg)

    search_query = scholarly.scholarly.search_pubs('An approach for deploying and monitoring dynamic security policies')
    scholarly.scholarly.pprint(next(search_query))


if __name__ == '__main__':
    google_scholar()
