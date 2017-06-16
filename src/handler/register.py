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
class RegisterHandler(tornado.web.RequestHandler):
	def get(self):
		#read movies and cinemas etc
		#cinema
		self.render('register.html', sameName=False, sameMail=False, samePhone=False)
	
	def post(self):
		print self.request.arguments
		username = self.get_argument('username')
		mail = self.get_argument('mail')
		password = self.get_argument('password')
		phone = self.get_argument('phone')
		same_user_username = mysql.get_user_from_name(username)
		same_user_email = mysql.get_user_from_email(mail)
		same_user_phone = mysql.get_user_from_phone(phone)
		if len(same_user_username) != 0:
			self.render('register.html', sameName=True, sameMail=False, samePhone=False)
			print "user exist"
			return
		if len(same_user_email) != 0:
			self.render('register.html', sameName=False, sameMail=True, samePhone=False)
			print "email exist"
			return
		if len(same_user_phone) != 0:
			self.render('register.html', sameName=False, sameMail=False, samePhone=True)
			print "phone exist"
			return
		if mysql.insert_user(username, mail, password, phone):
			user = mysql.get_user_from_name(username)
			self.set_cookie("UserId", str(user[0]['user_id']))
			self.redirect('/index/N')
		else:
			self.redirect('/')