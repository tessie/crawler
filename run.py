from crawler import Crawler

seed_url = raw_input(' Enter the url to crawl:')
depth = int(raw_input('Enter the max number of urls to be fetch'))
crawler = Crawler(depth)
links = crawler.crawl([seed_url])
for link in links:
    print link
