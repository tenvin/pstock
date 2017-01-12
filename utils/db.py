#-*- coding:utf-8 -*-
from sqlalchemy import create_engine, \
    Table, Column, Integer, String, Float, MetaData, ForeignKey


engine = create_engine('mysql://root:root@localhost/pstock?charset=utf8',encoding="utf-8")

# 获取元数据
metadata = MetaData()

investor = Table('investor_data', metadata,
        Column('id', Integer, primary_key=True),
        Column('code', String(10)),
        Column('quarter', String(20)),
        Column('name',String(120)),
        Column('ratio',Float),
        Column('amount',Float),
        Column('status',Integer)
    )

# 创建数据表，如果数据表存在，则忽视
metadata.create_all(engine)
# 获取数据库连接
conn = engine.connect()


if __name__ == '__main__':

    i = investor.insert()
    u = dict(code='603131',
         quarter='2016-9-30',
         name='陈留杭',
         ratio=0.23,
         amount=22.97,
         status=1
         )
    r=conn.execute(i,**u)




