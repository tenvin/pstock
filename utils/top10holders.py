#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time

from bs4 import BeautifulSoup
import requests
from sqlalchemy import text

from utils.db import conn
from utils.model import Investor
from utils.orm import session

s = requests.Session()
def get_items():
    date = '2016-09-30'
    URL_Base = 'http://quotes.money.163.com/service/gdfx.html?ltdate='+ date +'&symbol='
    list = get_code()
    for code in list:
        time.sleep(1000)
        print URL_Base+code
        r = s.get(URL_Base+code)

        soup = BeautifulSoup(r.content,"lxml")

    r.close()

def save(list):
    investor = Investor(list)
    session.add(investor)


def deal(soup):
    list = []
    tables = soup.findAll('table')
    tab = tables[0]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            if td.getText()==u'暂无数据':
                print td.getText()
                continue
            list.append(td.getText())
            #print td.getText(),
        #print
    print list
    #slice list
    for i in range(len(list)/4):
        if i==0:
            print list[0:3]
            continue
        print list[3*i+1:3*(i+1)]
    #save(list)


def get_code():
    # raw sql
    text_sql = "SELECT code FROM baseinfo"
    s = text(text_sql)
    result = conn.execute(s).fetchall()
    list = []
    for r in result:
        list.append(r[0])
    return list


if __name__ == '__main__':
    code = '000001'
    code2 = '300581'
    date = '2016-09-30'
    URL_Base = 'http://quotes.money.163.com/service/gdfx.html?ltdate='+ date +'&symbol=' + code
    r = s.get(URL_Base)
    soup = BeautifulSoup(r.content,"lxml")
    deal(soup)


