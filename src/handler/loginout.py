# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado
import mysqlDb.mysql as mysql

# noinspection PyAbstractClass
# /index/N the home page
# /index/1 the cinema_id = 1 movie list
# /index/E error illegal username or password
# /index/O logout
class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.redirect('/')
	
	def post(self):
		print self.request.arguments
		username = self.get_argument('username')
		password = self.get_argument('password')
		user = mysql.get_user_from_name(username)
		if len(user) == 0 or user[0]['password'] != password:
			self.redirect('/index/E')
		else:
			self.set_cookie('UserId', str(user[0]['user_id']))
			self.redirect('/index/N')
class LogoutHandler(tornado.web.RequestHandler):
	def get(self):
		self.clear_cookie('UserId')
		self.redirect('/index/O')