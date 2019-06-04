#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>
import datetime
import pytz
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from ..db import db_engine

CHENGDU_TIMEZONE = pytz.timezone('Asia/Shanghai')


class RbacUserInfo(db_engine.Model):
    __tablename__ = 'rbac_userinfo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    login_name = Column(String(64), index=True, nullable=False)
    login_pwd = Column(String(64), nullable=False)
    add_time = Column(
        DateTime, default=datetime.datetime.now(tz=CHENGDU_TIMEZONE))
    state = Column(Boolean)
    theme = Column(String(32))

    roles = relationship('RbacRole', secondary='user2role', backref='users')

    def __repr__(self):
        return "<RbacUserInfo(name=%s, login_name=%s)>" % (self.name, self.login_name)


class RbacRole(db_engine.Model):
    __tablename__ = 'rabc_role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(64), nullable=False)

    permissions = relationship(
        'Permissions', secondary='role2permission', backref='roles')

    def __repr__(self):
        return "<RbacRole(role_name=%s)" % self.role_name


class Permissions(db_engine.Model):
    __tablename__ = 'rbac_permissions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    p_name = Column(String(64), unique=True)
    p_url = Column(String(128), unique=True)


class User2Role(db_engine.Model):
    __tablename__ = 'user2role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    u_id = Column(Integer, ForeignKey('rbac_userinfo.id'))
    r_id = Column(Integer, ForeignKey('rabc_role.id'))


class Role2Permission(db_engine.Model):
    __tablename__ = 'role2permission'

    id = Column(Integer, primary_key=True, autoincrement=True)
    r_id = Column(Integer, ForeignKey('rbac_userinfo.id'))
    p_id = Column(Integer, ForeignKey('rbac_permissions.id'))

