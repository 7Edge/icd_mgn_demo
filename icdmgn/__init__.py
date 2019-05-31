#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>

from flask import Flask

from z_test import TestView

def create_app():

    app = Flask(__name__)
    app.config.from_object('settings.DevConfig')

    @app.route(rule='/hello',methods=['GET'], endpoint='hello')
    def hello():
        return 'Hello World!'

    app.add_url_rule(rule='/test', endpoint='test', view_func=TestView.as_view('test'))

    return app