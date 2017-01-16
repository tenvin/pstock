#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sqlalchemy import Column
from sqlalchemy.types import Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from utils.orm import engine

BaseModel = declarative_base()
def init_db():
    BaseModel.metadata.create_all(engine)
def drop_db():
    BaseModel.metadata.drop_all(engine)

class Investor(BaseModel):
    __tablename__ = 'investor_data'

    id = Column(Integer, primary_key=True)
    code = Column(String(30))
    quarter = Column(String(20))
    name = Column(String(120))
    ratio = Column(Float)
    amount = Column(Float)
    status = Column(Integer)

    def __init__(self, list):
        self.code,self.quarter,self.name,self.ratio,self.amount,self.status = list


if __name__ == '__main__':
    init_db()
