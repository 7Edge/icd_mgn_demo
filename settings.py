#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>
"""
flask 配置类
"""

class BaseConfig(object):
    SECRET_KEY = 'sdl183&#(#sdlfj'
    DEBUG = True


class DevConfig(BaseConfig):
    SECRET_KEY = 'Dev'


class ProductConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    SECRET_KEY = 'Test'