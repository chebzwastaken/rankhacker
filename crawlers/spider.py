import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

class Spider:
    # it needs a seed

    def __init__(self, seed, ignore):
        self.seed = seed
        self.ignore = ignore
        self.visited = []
        self.queue = []

    def crawl(self):
        for url in self.seed:
            self.queue.append(url)
        while self.queue:
            url = self.queue.pop(0)
            self.visited.append(url)
            try:
                r = requests.get(url)
            except:
                print('Error: Could not open URL')
                continue
            soup = BeautifulSoup(r.text, 'html.parser')
            for a in soup.find_all('a', href=True):
                if a['href'] not in self.visited and a['href'] not in self.queue:
                    if a['href'].startswith('http'):
                        self.queue.append(a['href'])
                    else:
                        self.queue.append(urljoin(url, a['href']))
            print(url)
    


if __name__ == '__main__':
    seed = ['https://www.chukkyiii.tech/']
    ignore = ['']
    spider = Spider(seed, ignore)
    spider.crawl()