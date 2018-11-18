# import libraries
import calendar
import json
import time

from model.Exchange import Exchange
from parsers.helper.meta_data import MetaDataHelper
from parsers.helper.scraper import Scraper


class Xoom:
    def __init__(self):
        self.exchange = Exchange(name="Xoom",end_point="/xoom")

    def get_amount(self):
        target_page = 'https://www.xoom.com/india/send-money'
        response = Scraper(target_page)
        html_data = response.get_html_data()
        # print html_data
        send_amount = float((html_data.find('input', attrs={'id': 'sendAmount',
                                                     'class': 'xvx-field__control xvx-field__control--emphasis'})['value']).encode('utf-8'))
        receive_amount = float((html_data.find('input', attrs={'id': 'receiveAmount','class':'xvx-field__control xvx-field__control--emphasis'})['value']).encode('utf-8'))
        # Gets INR price for $1
        amount = float(receive_amount/send_amount)
        self.exchange.amount = amount

        return self.exchange.to_json()

    def meta_data(self):
        return MetaDataHelper.get_meta_data(self.exchange)


