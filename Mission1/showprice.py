from bs4 import BeautifulSoup
import requests
import re


wofanginfo = {}
pinfanginfo = {}


def getwofanginfo():
    for i in range(201):
        try:
            url = 'http://www.wofang.com/building/p/%i/'
            html = requests.get(url % i)
            soup = BeautifulSoup(html.text, 'lxml')
            ul = soup.body.find('div', class_='m').ul
            for li in ul.find_all('li'):
                title = li.find('div', class_='title').a.get_text()
                price = li.find('div', class_='price').p.get_text()
                wofanginfo[title] = price
        except:
            pass


def getpinfanginfo():
    for i in range(130):
        try:
            url = 'http://www.pinfangw.com/property.html?page=%i'
            html = requests.get(url % i)
            soup = BeautifulSoup(html.text, 'lxml')
            ul = soup.body.find('div', class_='newl-list').ul
            for li in ul.find_all('li'):
                tit = li.find('div', class_='newl-list-box').find('div',
                                                                class_='newl-list-con').find('div', class_='newl-list-tit')
                title = tit.find(
                    'div', class_='newl-list-titname').a.get_text()
                price = str(tit.find(
                    'div', class_='newl-list-titnote').contents[1].string).replace('\n', '') + '元/㎡'
                pinfanginfo[title] = price
        except:
            pass


getpinfanginfo()
print(pinfanginfo)
