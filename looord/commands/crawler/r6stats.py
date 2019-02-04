import os

from bs4 import BeautifulSoup
import requests
from selenium import webdriver

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 '
        'Safari/537.36'
}

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
