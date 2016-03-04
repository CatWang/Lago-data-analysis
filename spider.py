import requests
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL = 'http://www.lagou.com'

def download_page(url):
    return requests.get(url, headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content

def parser_html(html):
    soup = BeautifulSoup(html)
    position_list_soup = soup.find('div', attrs={'class': 'menu_sub dn'})

    position_url_list = []

    for position_url in position_list_soup.find_all('a'):
        position_name = position_url.string
        url = position_url.get('href')
        position_url_list.append(url)
    return position_url_list

def main():
    url = DOWNLOAD_URL

    with codecs.open('position_url', 'wb', encoding='utf-8') as fp:
        html = download_page(url)
        position_url = parser_html(html)
        fp.write(u'{position_url}\n'.format(position_url='\n'.join(position_url)))

if __name__ == '__main__':
    main()