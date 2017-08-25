from getpage import get_page
from bs4 import BeautifulSoup


class Crawler:

    def __init__(self, depth=4):
        self.depth = depth

    def crawl(self, seed):
        links = set(seed)
        crawled = []
        while len(crawled) < self.depth and links:
            url = links.pop()
            if url not in crawled:
                content = get_page(url)
                scrapped_links = self.__get_links(content, url)
                print scrapped_links
                links.update(scrapped_links)
                crawled.append(url)
        return crawled

    def __get_links(self, content, url):
        links = []
        soup = BeautifulSoup(content, 'html.parser')
        for link in soup.find_all('a'):
            link = link.get('href')
            if link.startswith('/'):
                link = url + link[1:]
            links.append(link)
        return links
