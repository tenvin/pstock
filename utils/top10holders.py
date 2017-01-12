#!/usr/bin/env python
#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
from sqlalchemy import select

from utils.db import investor, conn

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

def get_code():
    s = select([investor.c.code])
    r = conn.execute(s)
    ru = r.fetchall()
    print ru[0]

if __name__ == '__main__':
    get_code()

