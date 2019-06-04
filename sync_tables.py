#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>

from icdmgn.db import db_engine
from icdmgn.rbac import models  # 导入才能将自定义的模型类注册到db_engine.Model中
from icdmgn.icd import models

from icdmgn import create_app

app = create_app()

with app.app_context():  # 必须在app上线文中，保证app时可用且进行了db_engine.ini_app(app)
    # db_engine.drop_all()
    db_engine.create_all()
