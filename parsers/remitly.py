# import libraries
import re

from model.Exchange import Exchange
from parsers.helper.meta_data import MetaDataHelper
from parsers.helper.scraper import Scraper


class Remitly:
    def __init__(self):
        self.exchange = Exchange(name="Remitly", end_point="/remitly")

    def get_amount(self):
        target_page = 'https://www.remitly.com/us/en/india'
        scraper = Scraper(target_page)
        # flsmo2ix is the class name which contains our required data for this project
        info_tag = scraper.get_html_data().find_all('td', attrs={'class': 'f1smo2ix'})

        optional = {}
        for index, data in enumerate(info_tag):
            if data.text.encode('utf-8') != "$0Fee":
                if index == 0:
                    optional['express'] = re.findall("\d+\.\d+", data.text.encode('utf-8'))[0]
                else:
                    optional['economy'] = re.findall("\d+\.\d+", data.text.encode('utf-8'))[0]

        # TODO : Do something with optional data
        self.exchange.amount = optional['economy']

        return self.exchange.to_json()

    def meta_data(self):
        return MetaDataHelper.get_meta_data(self.exchange)