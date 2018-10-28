# import libraries
import re

from parsers.helper.scraper import Scraper


class Remitly:
    def __init__(self):
        pass

    @staticmethod
    def get_amount():
        target_page = 'https://www.remitly.com/us/en/india'
        scraper = Scraper(target_page)
        # flsmo2ix is the class name which contains our required data for this project
        info_tag = scraper.get_html_data().find_all('td', attrs={'class': 'f1smo2ix'})

        remitly_result = {}
        for index, data in enumerate(info_tag):
            if data.text.encode('utf-8') != "$0Fee":
                if index == 0:
                    remitly_result['express'] = re.findall("\d+\.\d+", data.text)
                else:
                    remitly_result['economy'] = re.findall("\d+\.\d+", data.text)

        return remitly_result
