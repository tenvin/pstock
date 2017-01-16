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
    session.commit()


def deal(soup,code,quarter):
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

    #slice list
    for i in range(len(list)/4):
        l = list[4*i:4*i+4]
        l.insert(0,quarter)
        l.insert(0,code)
        save(l)



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
    quarter = '2016-09-30'
    URL_Base = 'http://quotes.money.163.com/service/gdfx.html?ltdate='+ quarter +'&symbol=' + code
    r = s.get(URL_Base)
    soup = BeautifulSoup(r.content,"lxml")
    deal(soup,code,quarter)


