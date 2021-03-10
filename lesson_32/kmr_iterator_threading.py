from threading import Thread

import requests
from bs4 import BeautifulSoup


class Document(Thread):

    def __init__(self):
        super().__init__()
        # self.filename = ''
        # self.link = ''
        # self.title = ''
        self.url = 'https://kmr.gov.ua/uk/stenogramu'

    def get_doc(self):
        while self.url:
            page = self.get_page_content()
            links = self.get_document_links(page)
            for link in links:
                yield link
            self.url = self.get_next_url(page)

    def get_next_url(self, page):
        domen = 'https://kmr.gov.ua/'
        if page.find('li', {'class': "pager-next"}):
            if page.find('li', {'class': "pager-next"}).find('a'):
                return domen + page.find('li', {'class': "pager-next"}).find('a').get('href')

    def get_document_links(self, soup):
        links = soup.findAll('div', {'class': "views-field views-field-title"})
        return links

    def get_page_content(self, attempts=3):

        if attempts < 0:
            raise Exception('No attempts')

        response = requests.get(self.url)
        if not response.ok:
            return self.get_page_content(attempts - 1)
        return BeautifulSoup(response.content, 'html.parser')

    def __next__(self):

        links = self.get_doc()
        for o_link in links:
            link = o_link.find('a', {'class': "field-content"}).get('href')
            title = o_link.find('span', {'class': "field-content"}).text
            filename = link.split('/')[-1]
            return title, filename, link

    def __iter__(self):
        return self


if __name__ == '__main__':
    doc = Document()
    for i in range(12):
        print(i, next(doc))
