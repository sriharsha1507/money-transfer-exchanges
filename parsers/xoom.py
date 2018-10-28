# import libraries
import re

from parsers.helper.scraper import Scraper


class Xoom:

    def __init__(self):
        pass

    @staticmethod
    def get_amount():
        target_page = 'https://www.xoom.com/india/send-money'
        scraper = Scraper(target_page)
        # xvx-text-right xvx-font-copy is the class name which contains our required data for this project
        info_tag = scraper.get_html_data().find('p', attrs={'class': 'xvx-text-right xvx-font-copy'})
        data = re.findall("\d+\.\d+", info_tag.text)
        xoom_result = {"amount": data}
        return xoom_result
