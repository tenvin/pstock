#!/usr/bin/env python
#-*- coding:utf-8 -*-


# 初始化函数，设定要操作的股票、基准等等
def initialize(context):
    # 定义一个全局变量, 保存要操作的股票

    g.stocks = list(get_all_securities(['stock'], date=context.current_dt).index)
    # g.stocks 就是我们要操纵的所有股票
    set_universe(g.stocks)

def before_trading_start(context):
    # 得到所有股票昨日收盘价, 每天只需要取一次, 所以放在 before_trading_start 中
    g.last_df = history(3,'1d','volume')

# 每个单位时间(如果按天回测,则每天调用一次,如果按分钟,则每分钟调用一次)调用一次
def handle_data(context, data):
    for security in g.stocks:

        oldestvolume = g.last_df[security][-2]
        oldvolume = g.last_df[security][-1]
        newvolume = g.last_df[security][0]

        if ((oldvolume-oldestvolume)/(oldestvolume))*100 > 300 and ((newvolume-oldvolume)/(oldvolume))*100 < 100:
            print "Valid Stock is :" + security
            print oldestvolume
            print oldvolume
            print newvolume
            print ((oldvolume-oldestvolume)/(oldestvolume))*100
            print ((newvolume-oldvolume)/(oldvolume))*100