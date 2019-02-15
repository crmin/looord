import os

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

from commands.crawler.const import headers, stat_card_idx, stat_section_idx, kills_breakdown_idx

_driver = None


class Platform():
    pc = 'pc'
    ps4 = 'ps4'
    xbox = 'xbox'


html_parser = 'lxml'


def request_get(url):
    return requests.get(url, headers=headers)


def get_uuid(username, platform=Platform.pc):
    result_resp = request_get(
        'https://r6stats.com/search/{username}/{platform}/'.format(
            username=username,
            platform=platform
        )
    )
    result_soup = BeautifulSoup(result_resp.text, html_parser)
    users = result_soup.find_all('a', class_='result')
    user_uuids = []
    for user in users:
        user_uuids.append(user['href'][7:-1])
    return user_uuids


def get_simple_info(uuid):
    url = 'https://r6stats.com/stats/{}/'.format(uuid)
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    username = soup.find('h1', class_='username').text
    profile_img = soup.find('img', class_='profile')['src']
    ranks = soup.find_all('div', class_='season-rank')
    stat_cards = soup.find_all('div', class_='stat-card')
    return {
        'url': url,
        'username': username,
        'profile_img': profile_img,
        'rank': ' > '.join(sorted([rank.img['title'] for rank in ranks[:3]], reverse=True)),
        'ranked_stats': {
            stat_name: stat_value.find('span', class_='stat-count').text
            for stat_name, stat_value in zip(stat_section_idx, stat_cards[stat_card_idx.index('ranked_stats')]
                .find('div', class_='card__content')
                .find_all('div', class_='stat-section'))
        },
        'casual_stats': {
            stat_name: stat_value.find('span', class_='stat-count').text
            for stat_name, stat_value in zip(stat_section_idx, stat_cards[stat_card_idx.index('casual_stats')]
                .find('div', class_='card__content')
                .find_all('div', class_='stat-section'))
        },
        'overall_stats': {
            stat_name: stat_value.find('span', class_='stat-count').text
            for stat_name, stat_value in zip(stat_section_idx, stat_cards[stat_card_idx.index('overall_stats')]
                .find('div', class_='card__content')
                .find_all('div', class_='stat-section'))
        },
    }


# Legacy code: $hist <username> --> send screenshot to channel
def get_webdriver(webdriver_path=None):
    global _driver
    if _driver is None:
        if webdriver_path is None:
            webdriver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'webdrivers', 'chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        _driver = webdriver.Chrome(webdriver_path, options=options)
        _driver.set_window_size(1200, 1670)
    return _driver


def get_history_img_path(uuid):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'history_imgs', '{}.png'.format(uuid))


def capture(driver, url, save_path=None):
    if save_path is None:
        save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'history_imgs', 'screenshot.png')
    driver.get(url)
    driver.execute_script('document.getElementsByClassName("ad-container")[0].style.display = "none"')
    driver.execute_script('document.getElementsByClassName("ad-container")[1].style.display = "none"')
    driver.execute_script('document.getElementsByTagName("header")[0].style.display = "none"')
    driver.execute_script('document.getElementsByTagName("footer")[0].style.display = "none"')
    driver.execute_script('document.getElementsByClassName("favorite-button")[0].style.display = "none"')
    driver.save_screenshot(save_path)


def save_history(username):
    driver = get_webdriver()
    uuids = get_uuid(username)
    if uuids:
        uuid = uuids[0]
    else:
        return None
    save_path = get_history_img_path(uuid)
    save_dir = os.path.dirname(save_path)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir, exist_ok=True)
    capture(driver, 'https://r6stats.com/stats/{}/'.format(uuid), save_path)
    return save_path
