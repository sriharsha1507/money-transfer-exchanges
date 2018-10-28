import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, target_page):
        self.page = target_page

    def get_html_data(self):
        fake_agent = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        page = requests.get(self.page, fake_agent)
        return BeautifulSoup(page.text, 'html.parser')
