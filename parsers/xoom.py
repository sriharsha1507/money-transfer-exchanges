# import libraries
import calendar
import json
import time

from model.Exchange import Exchange
from parsers.helper.scraper import Scraper


class Xoom:

    def __init__(self):
        pass

    @staticmethod
    def get_amount():
        target_page = 'https://www.xoom.com/india/send-money'
        response = Scraper(target_page)
        html_data = response.get_html_data()
        # print html_data
        send_amount = float((html_data.find('input', attrs={'id': 'sendAmount',
                                                     'class': 'xvx-field__control xvx-field__control--emphasis'})['value']).encode('utf-8'))
        receive_amount = float((html_data.find('input', attrs={'id': 'receiveAmount','class':'xvx-field__control xvx-field__control--emphasis'})['value']).encode('utf-8'))
        # Gets INR price for $1
        amount = float(receive_amount/send_amount)
        exchange = Exchange(name="xoom", amount=amount)

        return exchange.to_json()

