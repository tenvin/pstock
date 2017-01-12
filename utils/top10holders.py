#!/usr/bin/env python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

s = requests.Session()
def get_items():
    code = '603131'
    date = '2016-09-30'
    URL_Base = 'http://quotes.money.163.com/service/gdfx.html?ltdate='+ date +'&symbol=' + code
    print URL_Base
    r = s.get(URL_Base)
    soup = BeautifulSoup(r.content,"lxml")
    r.close()

    # list = soup.find_all(class_='td_text')
    # for item in list:
    #     print item.string

    tables = soup.findAll('table')
    tab = tables[0]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            print td.getText(),
        print


if __name__ == '__main__':
    get_items()

