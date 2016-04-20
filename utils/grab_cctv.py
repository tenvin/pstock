# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from bs4 import BeautifulSoup
import requests

s = requests.Session()
def go():
    date = raw_input(u'请输入新闻联播日期（如20141107）： ')
    print u"正在制作新闻联播文本版"
    URL_Base = 'http://cctv.cntv.cn/lm/xinwenlianbo/'+date+'.shtml'
    r = s.get(URL_Base)
    soup = BeautifulSoup(r.content)
    getnewslist = soup.find_all( class_ = 'title2 fs_14')
    for i in getnewslist:
        for news in i.find_all('li'):
           # print news.string+'\n'
            r = s.get(news.a.get('href'))
            soup = BeautifulSoup(r.content)
            text = soup.find(class_= 'body')
            with open(date+'.html','a') as f:
                f.write('<b>'+news.string.encode('gb2312')+'</b>'+'\n')
                f.write(text.encode('gb2312')+'\n')
if __name__ == '__main__':
    go()
    print u"制作完毕"
