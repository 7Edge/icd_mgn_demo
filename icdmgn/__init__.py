#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>

from flask import Flask

from .db import db_engine

from z_test import TestView

def create_app():

    app = Flask(__name__)
    app.config.from_object('settings.DevConfig')

    db_engine.init_app(app)  # 给db engine 绑定flask app，其实时读取app.config中有关数据库的配置

    @app.route(rule='/hello',methods=['GET'], endpoint='hello')
    def hello():
        return 'Hello World!'

    app.add_url_rule(rule='/test', endpoint='test', view_func=TestView.as_view('test'))
    return app