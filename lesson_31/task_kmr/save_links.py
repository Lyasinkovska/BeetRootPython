"""
скачать все документы пленарных засідань КМР
https://kmr.gov.ua/uk/stenogramu
"""
import json

import requests
from bs4 import BeautifulSoup

filename = 'task_kmr/docs.json'
default_url = f'https://kmr.gov.ua/uk/stenogramu?title=&field_start_date_n_h_value%5Bmin%5D' \
              f'&field_start_date_n_h_value%5Bmax%5D&page='


def get_soup(url):
    resp = requests.get(url)
    return BeautifulSoup(resp.content, 'html.parser')


def get_current_page(soup):
    return soup.find('li', {'class': "pager-current"}).text


def get_document_links(soup):
    links = soup.findAll('div', {'class': "views-field views-field-title"})
    dates = soup.findAll('span', {'class': "date-display-single"})
    return dates, links


def save_links_to_doc(soup, documents):
    dates, links = get_document_links(soup)
    for date, one_link in zip(dates, links):
        date = date.get('content')
        link = one_link.find('a', {'class': "field-content"}).get('href')
        name = one_link.find('span', {'class': "field-content"}).text
        result = {'name': name, 'date': date, 'link': link}
        documents.append(result)


def save_to_json(documents):
    with open(filename, 'w', encoding='cp1251') as output_file:
        json.dump(documents, fp=output_file, indent=2)


if __name__ == '__main__':
    page = 0
    documents = []
    while True:
        URL = f'{default_url}{page}'
        soup_obj = get_soup(URL)
        current_page = get_current_page(soup_obj)
        if int(current_page) == page:
            break
        save_links_to_doc(soup_obj, documents)
        page += 1
    save_to_json(documents)
    print(len(documents))
