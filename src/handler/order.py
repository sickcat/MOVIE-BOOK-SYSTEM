# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado
import mysqlDb.mysql as mysql

# noinspection PyAbstractClass
# /order
class OrderHandler(tornado.web.RequestHandler):
	def get(self):
		#read movies and cinemas etc
		#cinema
		user_id = self.get_cookie('UserId')
		username = mysql.get_user_info(user_id)

		if username == None or len(username) == 0:
			self.render('order.html', cookieName = username,
				order = [], alert = 1, alert_msg = "Please Login First")
		else:
			order = mysql.get_order(user_id)
			if order==None:
				order = []
			self.render('order.html', cookieName = username,
				order = order, alert = 0, alert_msg = "")
