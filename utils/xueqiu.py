#!/usr/bin/env
# -*- coding: utf-8 -*-
# @Date    :
# @Author  :
# @Link    :
# @Version : v.0.0


import requests
import hashlib
import re
from utils.config import MY_TELEPHONE, MY_PASS
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {
    'User-Agent': agent,
    'Host': "xueqiu.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.6",
    "Connection": "keep-alive"
}

session = requests.session()


# 密码的 md5 加密
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest().upper()


# 只写了手机号登录的情况，邮箱登录的情况，可以简单修改 postdata 后实现、
def login(telephone, password):
    url = 'https://xueqiu.com/'
    session.get(url, headers=headers)  # 访问首页产生 cookies
    headers['Referer'] = "https://xueqiu.com/"
    login_url_api = "https://xueqiu.com/service/csrf?api=%2Fuser%2Flogin"  # 模拟更真实的请求
    session.get(login_url_api, headers=headers)
    login_url = "https://xueqiu.com/user/login"
    postdata = {
        "areacode": "86",
        "password": get_md5(password),
        "remember_me": "on",
        "telephone": telephone
    }
    log = session.post(login_url, data=postdata, headers=headers)
    log = session.get("https://xueqiu.com/setting/user", headers=headers)
    pa = r'"profile":"/(.*?)","screen_name":"(.*?)"'
    res = re.findall(pa, log.text)
    if res == []:
        print("登录失败，请检查你的手机号和密码输入是否正确")
    else:
        print('欢迎使用 xueqiu 模拟登录 \n 你的用户 id 是：%s, 你的用户名是：%s' % (res[0]))


if __name__ == '__main__':

    login(MY_TELEPHONE, MY_PASS)