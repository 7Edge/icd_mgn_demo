#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>
"""
flask 配置类
"""

# Flask-SQLALchemy 配置


class DatabaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/icd_mgn_demo?charset=utf8'
    SQLALCHEMY_POOL_SIZE = 5  # 数据库连接池
    SQLALCHEMY_MAX_OVERFLOW = 2  # 最多溢出连接池数量
    SQLALCHEMY_POOL_RECYCLE = -1  # 是否对连接进行周期性回收（重置）, 如果不进行回收设置值为-1即可，但是一般还是要设置，
    # 因为有些数据库连接时长是有限制的所以最好稍微小于设置的连接时长，如mysql就有配置连接时长（不知道连接不可用后会不会自动重连连）。
    # Note that
    # MySQL in particular will disconnect automatically if no
    # activity is detected on a connection for eight hours (although
    # this is configurable with the MySQLDB connection itself and the
    # server configuration as well).
    SQLALCHEMY_POOL_TIMEOUT = 30  # 默认连接池对象使用该配置，就是到连接池取连接超时时间
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class BaseConfig(object):
    SECRET_KEY = 'sdl183&#(#sdlfj'
    DEBUG = True


class DevConfig(BaseConfig, DatabaseConfig):
    SECRET_KEY = 'Dev'


class ProductConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    SECRET_KEY = 'Test'
