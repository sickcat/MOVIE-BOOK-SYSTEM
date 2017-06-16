# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado

# noinspection PyAbstractClass
class FooHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('test get')
    def post(self):
    	self.write('test post')
    def put(self):
    	self.write('test put')
