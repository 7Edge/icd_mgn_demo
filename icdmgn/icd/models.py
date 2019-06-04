#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>
from sqlalchemy import Integer, String, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from ..db import db_engine

# 客户表
class Customer(db_engine.Model):
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    age = Column(Integer)
    email = Column(String(255))
    company = Column(String(255))


    def __repr__(self):
        return "<Customer(name=%s email=%s)" % (self.name, self.email)


# 符费记录
class Payment(db_engine.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    money = Column(Integer)
    create_time = Column(DateTime)

    customer = relationship('Customer', backref='payments')



    


