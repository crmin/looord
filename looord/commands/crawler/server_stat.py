from bs4 import BeautifulSoup
import requests

from commands.crawler.const import headers


url = 'https://outage.report/rainbow-six'


def get_error_num():
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    gauge_box = soup.find('div', class_='Responsive-wrapper')
    # status_category = [each for each in gauge_box.parent.find_all('section')[1].find_all('li')]
    return int(gauge_box.find('text').text)

