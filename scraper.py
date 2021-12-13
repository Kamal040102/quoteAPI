from bs4 import BeautifulSoup
import requests

class Scraper():
    def scrapedData(self, type):
        url = requests.get(f'https://quotes.toscrape.com/tag/{type}').text
        urlTesting = requests.get('https://quotes.toscrape.com/tag/{type}')
        print(urlTesting.status_code)
        quotelst = []
        soup = BeautifulSoup(url, 'lxml')
        quoteList = soup.find_all('span', class_='text')
        for quote in quoteList:
            item = {
                'Quote':quote.text,
            }
            quotelst.append(item)
        return quotelst

quotes = Scraper()
quotes.scrapedData(type)