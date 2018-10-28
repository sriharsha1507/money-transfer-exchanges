# import libraries
import json
import re

import requests
from bs4 import BeautifulSoup

# specify the parser url
target_page = 'https://www.xoom.com/india/send-money'
fakeAgent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
page = requests.get(target_page, fakeAgent)
parsedHtmlPage = BeautifulSoup(page.text, 'html.parser')
# xvx-text-right xvx-font-copy is the class name which contains our required data for this project
infoTag = parsedHtmlPage.find('p', attrs={'class': 'xvx-text-right xvx-font-copy'})
result = re.findall("\d+\.\d+", infoTag.text)
result = {"amount": result[0]}

print json.dumps(result, indent=2)