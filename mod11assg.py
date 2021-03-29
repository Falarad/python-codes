from pandas import *
from bs4 import BeautifulSoup
import requests, urllib, time, threading

visitedUrls = []
urlsToGo = ['https://datatofish.com']
crawlers = 0

class TotallyNotMorrisWorm:
    def __init__(self, child):
        self.child = child
        self.execute()
        crawlers += 1

    def download(self, url):
        return requests.get(url).text

    def links(self, url, text):
        soup = BeautifulSoup(text, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def addUrl(self, url):
        if url not in visitedUrls and url not in urlsToGo:
            urlsToGo.append(url)

    def crawl(self, url):
        text = self.download(url)
        for url in self.links(url, text):
            self.addUrl(url)

    def execute(self):
        while urlsToGo:
            if len(urlsToGo) > 100:
                self.replicate()
            url = urlsToGo.pop(0)
            print('Crawling: {}'.format(url))
            try:
                self.crawl(url)
            except Exception as e:
                print('Failed to crawl: {}'.format(url))
                print('Reason: {}'.format(e))
            finally:
                visitedUrls.append(url)
                time.sleep(1)
                if len(urlsToGo) == 0:
                    return

    def replicate(self):
        child = self.child + 1
        code = threading.Thread(target=TotallyNotMorrisWorm, args=(child,))
        code.start()

def excel():
    document = read_excel(r'supplimentaryContent\COVID19_03242020_ByCounty.xlsx')
    return document
def main():
    covid = excel()
    print('The mean infected persons by county is {}'.format(covid['PUIsTotal'].mean()))
    input('Once you press enter, I am not liable if your IP gets banned.')
    TotallyNotMorrisWorm(0)
main()
