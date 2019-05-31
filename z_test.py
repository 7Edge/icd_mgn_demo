#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>

"""
文件主要目的：
1. 查看源码
2. 测试简单功能
"""
from flask.cli import main
from flask import views
from flask import Response
from flask import Flask, redirect, render_template, jsonify, make_response
from flask import request, session

# 测试创建一个CBV
class TestView(views.MethodView):
    methods = ['GET', 'POST']
    decorators = ()

    def get(self):
        print(request.method)
        return jsonify({'code': 1000,
                        'msg': 'from cbv'})

    def post(self):
        print(request.method)
        res = make_response('new hello.world')
        res.headers['author_name'] = 'zhangjiaqi'
        return res
