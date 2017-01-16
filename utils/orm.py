#!/usr/bin/env python
#-*- coding:utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.config import DB_CONNECT_STRING

engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

if __name__ == '__main__':
    pass