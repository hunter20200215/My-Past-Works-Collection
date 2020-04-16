import requests
import time
import pprint
import re
import pyperclip
import bs4
from bs4 import BeautifulSoup
from lxml import html

def upcominglists():
    page=requests.get('https://www.prepbaseballreport.com/showcases')
    tree=html.fromstring(page.content)
    showcaseslist=tree.xpath('//td//a[contains(@href,event)]/text()')
    print('Upcoming Events:',showcaseslist)

def listsurl_scraper():
    pageurl=requests.get('https://www.prepbaseballreport.com/showcases')
    base_url='https://www.prepbaseballreport.com'
    soup=BeautifulSoup(pageurl.content,'html.parser')
    for table in soup.findAll('table', {'class': 'results-table'}):
        for tr in table.findAll('tr'):
            for a in tr.findAll('a'):
                urls = a.get('href')
                url2=base_url+urls
#                print(url2)
                findroster(url2)
def findroster(url):
    url2page=requests.get(url)
    treeroster=html.fromstring(url2page.content)
    search=treeroster.xpath('//li//a[contains(@href,"?tab=rosters")]/text()')
    if search is None:
        print ('None')
    else:
        print(search)
    url_add='?tab=rosters'
    urlroster=url+url_add
#    print(urlroster)
    
    Playerinfoscraper(urlroster)

def Playerinfoscraper(urllast):
    url3page=requests.get(urllast)
    treelast=html.fromstring(url3page.content)       
    name=treelast.xpath('//td//strong/text()')
    print(name)
    highschool=treelast.xpath('//td[contains(@class,"highschool")]/text()')
    print(highschool)
    gradyear=treelast.xpath('//td[contains(@class,"gradyear")]/text()')
    print(gradyear)	
    position=treelast.xpath('//td[contains(@class,"position")]/text()')
    print(position)



upcominglists()
                 
listsurl_scraper()
