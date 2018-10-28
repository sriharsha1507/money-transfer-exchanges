# import libraries
import json
import re

# specify the parser url
from parsers.helper.scraper import Scraper

target_page = 'https://www.xoom.com/india/send-money'
scraper = Scraper(target_page)
# xvx-text-right xvx-font-copy is the class name which contains our required data for this project
infoTag = scraper.get_html_data().find('p', attrs={'class': 'xvx-text-right xvx-font-copy'})
data = re.findall("\d+\.\d+", infoTag.text)
xoomResult = {"amount": data}

print json.dumps(xoomResult, indent=2)
