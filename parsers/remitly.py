# import libraries
import json
import re
from parsers.helper.scraper import Scraper

target_page = 'https://www.remitly.com/us/en/india'
scraper = Scraper(target_page)
# flsmo2ix is the class name which contains our required data for this project
infoTag = scraper.get_html_data().find_all('td', attrs={'class': 'f1smo2ix'})

remitlyResult = {}
for index, data in enumerate(infoTag):
    if data.text.encode('utf-8') != "$0Fee":
        if index == 0:
            remitlyResult['express'] = re.findall("\d+\.\d+", data.text)
        else:
            remitlyResult['economy'] = re.findall("\d+\.\d+", data.text)

print json.dumps(remitlyResult, indent=2)
