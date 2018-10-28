# import libraries
import calendar
import json
import time

from parsers.helper.scraper import Scraper


class Xoom:

    def __init__(self):
        pass

    @staticmethod
    def get_amount():
        # info_tag = scraper.get_html_data().find('p', attrs={'class': 'xvx-text-right xvx-font-copy'})
        # data = re.findall("\d+\.\d+", info_tag.text)
        target_page = 'https://www.xoom.com/calculate-fee-table?sourceCountryCode=US&sourceCurrencyCode=USD&destinationCountryCode=IN&destinationCurrencyCode=INR&sendAmount=1.00&receiveAmount=72.00&localCurrency=true&serviceType=&serviceSlug=&receiveAmountEntered=false&oldSourceCurrencyCode=USD&oldDestinationCurrencyCode=INR&remittanceResourceID=207115e0-38f8-408a-a3a5-493476792d70&_=' + str(
            calendar.timegm(time.gmtime()) * 1000)
        response = Scraper(target_page)
        result = response.get_html_data()
        json_string = result.find('data', attrs={'id': 'jsonData'}).text
        j_data = json.loads(json_string)
        return {'amount': j_data['data']['fxRate']}
