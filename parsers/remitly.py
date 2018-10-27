# import libraries
import json
import urllib2
from bs4 import BeautifulSoup

# specify the parser url
target_page = 'https://www.remitly.com/us/en/india'
page = urllib2.urlopen(target_page)
parsedHtmlPage = BeautifulSoup(page, 'html.parser')
# flsmo2ix is the class name which contains our required data for this project
infoTag = parsedHtmlPage.find_all('td', attrs={'class': 'f1smo2ix'})

remitlyResult = {}
for index, data in enumerate(infoTag):
    if data.text.encode('utf-8') != "$0Fee":
        if index == 0:
            remitlyResult['express'] = data.text
        else:
            remitlyResult['economy'] = data.text

print json.dumps(remitlyResult, indent=2)
