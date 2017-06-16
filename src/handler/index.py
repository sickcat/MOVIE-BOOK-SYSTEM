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
class MainHandler(tornado.web.RequestHandler):
	def get(self, URL):
		#read movies and cinemas etc
		#cinema
		user_id = self.get_cookie('UserId')
		username = mysql.get_user_info(user_id)
		cinema_list = []
		cinema_movie_list = []

		#display i[0]
		news_list = [["misowuwulimu dahuo!", "???"]]
		#display i[0]
		recommand_list = [["THE KING OF THE WAR", "???"]]

		cml_num = 0
		cinema_list = mysql.get_cinema_list()
		res = URL.split('_')
		if str(res[0]).isdigit() and len(res) == 2:
			cinema_movie_list = mysql.get_movie_list_from_cinema(res[0])
			cml_num = len(cinema_movie_list)
			has_the_cinema = mysql.get_cinema(res[0])
			movie_showin = {}
			for each in cinema_movie_list:
				movie_showin[str(each['movie_id'])] = mysql.get_same_movie_showin(res[0], each['movie_id'])
			#can't find this cinema
			#TODOS
			if len(has_the_cinema) > 0:
				self.render('index.html', cookieName=username, news_list = news_list,
				recommand_list = recommand_list, cinema_list = cinema_list, friendLinks = [], 
				cinema_movie_list = cinema_movie_list, cml_num = cml_num, Page = res[1], cinema = res[0],
				movie_showin = movie_showin,
				alert = 0, alert_msg = "")
			else:
				self.render('index.html', cookieName=username, news_list = news_list,
				recommand_list = recommand_list, cinema_list = cinema_list, friendLinks = [], 
				cinema_movie_list = cinema_movie_list, cml_num = cml_num, Page = res[1], cinema = -2,
				movie_showin = movie_showin,
				alert = 0, alert_msg = "")
		elif res[0] == 'N':
			self.render('index.html', cookieName=username, news_list = news_list,
				recommand_list = recommand_list, cinema_list = cinema_list, friendLinks = [], 
				cinema_movie_list = cinema_movie_list, cml_num = cml_num, Page = 0, cinema = -1,
				movie_showin = {},
				alert = 0, alert_msg = "")
		elif res[0] == 'E':
			self.render('index.html', cookieName=username, news_list = news_list,
				recommand_list = recommand_list, cinema_list = cinema_list, friendLinks = [], 
				cinema_movie_list = cinema_movie_list, cml_num = cml_num, Page = 0, cinema = -1,
				movie_showin = {},
				alert = 1, alert_msg = "illegal username or password")
		elif res[0] == 'O':
			self.render('index.html', cookieName=username, news_list = news_list,
				recommand_list = recommand_list, cinema_list = cinema_list, friendLinks = [], 
				cinema_movie_list = cinema_movie_list, cml_num = cml_num, Page = 0, cinema = -1,
				movie_showin = {},
				alert = 1, alert_msg = "you have logged out")
		else:
			self.render('error.html')
class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		#read movies and cinemas etc
		#cinema
		self.redirect('/index/N')