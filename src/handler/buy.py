# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado
import mysqlDb.mysql as mysql
import time
# /buy/cinemaid_showinid_movieid
class BuyHandler(tornado.web.RequestHandler):
	
	def get(self, URL, alert=0, alert_msg=""):
		#read movies and cinemas etc
		#cinema
		user_id = self.get_cookie('UserId')
		print user_id
		username = mysql.get_user_info(user_id)
		res = URL.split('_')

		if len(res) != 3: #argument not match
			self.redirect('/')
		
		movie_detail = mysql.get_movie(res[2])[0]
		showin_detail = mysql.get_showin(res[1])[0]
		seat_list = str(showin_detail['seat']).split(',')
		self.render('buy.html', cookieName = username, movie = movie_detail,
			alert = alert, alert_msg = alert_msg,seat_list = seat_list,
			cinema_id = res[0], showin_id = res[1], flag = 1)
	
	def post(self, URL):
		user_id = self.get_cookie('UserId')
		booklist = self.request.arguments['booklist'][0].split(',')
		res = URL.split('_')
		showin_detail = mysql.get_showin(res[1])
		seat_list = str(showin_detail[0]['seat']).split(',')
		ticket_id = mysql.insert_ticket(res[0], res[2], res[1], user_id, showin_detail[0]['room'], str(booklist))
		print booklist
		for each in seat_list:
			for each2 in booklist:
				print each + " " + each2
				if str(each) == str(each2):
					seat_list.remove(each)
					booklist.remove(each2)
		f_str = ""
		for each in seat_list:
			f_str += each + ','
		mysql.update_showin_seat(showin_detail[0]['showin_id'], f_str)

		mysql.insert_order(user_id, ticket_id, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 0)
		self.get(URL, 1, 'YOU HAVE SUCCESSFULLY BOOKED THOSE TICKETS')