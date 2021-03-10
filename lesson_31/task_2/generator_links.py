from collections import namedtuple

import requests
from bs4 import BeautifulSoup

Document = namedtuple('Document', ['filename', 'link', 'title'])


def get_kmr_documents() -> Document:
    url = 'https://kmr.gov.ua/uk/stenogramu'
    while url:
        page = get_page_content(url)
        for doc in get_doc_from_page(page):
            yield doc
        url = get_next_page(page)


def get_next_page(page):
    domen = 'https://kmr.gov.ua/'
    if page.find('li', {'class': "pager-next"}):
        if page.find('li', {'class': "pager-next"}).find('a'):
            return domen + page.find('li', {'class': "pager-next"}).find('a').get('href')


def get_document_links(soup):
    links = soup.findAll('div', {'class': "views-field views-field-title"})
    dates = soup.findAll('span', {'class': "date-display-single"})
    return dates, links


def get_doc_from_page(soup) -> Document:
    dates, links = get_document_links(soup)
    for date, one_link in zip(dates, links):
        link = one_link.find('a', {'class': "field-content"}).get('href')
        title = one_link.find('span', {'class': "field-content"}).text
        filename = link.split('/')[-1]
        yield Document(filename, link, title)


def get_page_content(url, attempts=3):
    if attempts < 0:
        raise Exception('No attempts')

    response = requests.get(url)
    if not response.ok:
        return get_page_content(url, attempts - 1)

    return BeautifulSoup(response.content, 'html.parser')


if __name__ == '__main__':
    docs = get_kmr_documents()
    url = 'https://kmr.gov.ua/uk/stenogramu'
    content = get_doc_from_page(get_page_content(url))
    for i in range(12):
        print(i, next(docs))


