from bs4 import BeautifulSoup
from getpage import get_page


class Crawler:

    def __init__(self, depth=4):
        self.depth = depth

    def crawl(seed):
        links = []
        return links

    def __get_links(content):
        links = []
        soup = BeautifulSoup(content, 'html.parser')
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links
