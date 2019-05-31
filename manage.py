#!/usr/bin/env python
# coding:utf-8
# author: zhangjiaqi<zhangjiaqi77777@outlook.com>

from flask_script import Manager
from icdmgn import create_app

app = create_app()
manager = Manager(app)


if __name__ == "__main__":
    manager.run()