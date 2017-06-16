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
class MovieHandler(tornado.web.RequestHandler):
	def get(self, URL):
		#read movies and cinemas etc
		#cinema
		user_id = self.get_cookie('UserId')
		username = mysql.get_user_info(user_id)
		res = URL.split('_')
		movie_detail = mysql.get_movie(res[0])[0]
		cinema_list = mysql.get_cinema_list_from_movie(movie_detail['movie_id'])

		showin_list = {}
		for each in cinema_list:
			showin_list[str(each['cinema_id'])] = mysql.get_same_movie_showin(each['cinema_id'], res[0])
		self.render('movie.html', cookieName = username, movie = movie_detail, cinema = cinema_list,
			showin_list = showin_list, alert = 0, alert_msg = "")
