from settings import settings
import torndb
import json
import time

def database(fun, sql):
	try:
		db = torndb.Connection(host=settings["host"],
			database=settings['database'],
			user=settings["user"],
			password=settings["password"],
			time_zone=settings["timezone"])
		if fun == 0:
			return db.query(sql)
		else:
			db.execute(sql)
			return None
	except Exception as e:
		print sql
		print e
		print "-----------Connect Error Try Again..."

#only use in this file to check digit
def isDigit(_input):
	if not _input:
		return False
	if not str(_input).isdigit():
		return False
	return True

#index.py -> [IndexHandler]
def get_cinema_list():
	sql = 'select * from cinema'
	return database(0, sql)

#index.py -> [IndexHandler]
def get_movie_list_from_cinema(cinema_id):
	sql = 'select * from movie where movie_id in (select movie_id from show_in where cinema_id = {0})'.format(cinema_id)
	return database(0, sql)

#index.py -> [IndexHandler]
def get_user_info(user_id):
	if isDigit(user_id):
		sql = 'select * from user where user_id={0}'.format(user_id)
		return database(0, sql)[0]
	else:
		return None

#index.py -> [IndexHandler]
def get_cinema(cinema_id):
	if isDigit(cinema_id):
		sql = 'select * from cinema where cinema_id={0}'.format(cinema_id)
		return database(0, sql)
	else:
		return None
def get_same_movie_showin(cinema_id, movie_id):
	sql = 'select * from show_in where cinema_id={0} and movie_id={1}'.format(cinema_id, movie_id)
	return database(0, sql)

#movie.py -> [MovieHandler]
def get_movie(movie_id):
	if isDigit(movie_id):
		sql = 'select * from movie where movie_id={0}'.format(movie_id)
		return database(0, sql)
	else:
		return None

#movie.py -> [MovieHandler]
def get_cinema_list_from_movie(movie_id):
	if isDigit(movie_id):
		sql = 'select * from cinema where cinema_id in (select cinema_id from show_in where movie_id = {0})'.format(movie_id)
		return database(0, sql)
	else:
		return None

#register.py -> [RegisterHandler]
def insert_user(username, mail, password, phone):
	if isDigit(phone):
		sql = 'insert into user(name, email, phone, password) values("{0}", "{1}", "{2}", "{3}")'.format(
			torndb.MySQLdb.escape_string(str(username)),
			torndb.MySQLdb.escape_string(str(mail)),
			torndb.MySQLdb.escape_string(str(phone)),
			torndb.MySQLdb.escape_string(str(password)))
		database(1, sql)
		return True
	else:
		return False

#register.py -> [RegisterHandler]
def get_user_from_name(username):
	sql = 'select * from user where name="{0}"'.format(
		torndb.MySQLdb.escape_string(str(username)))
	return database(0, sql)
def get_user_from_email(email):
	sql = 'select * from user where email="{0}"'.format(
		torndb.MySQLdb.escape_string(email))
	return database(0, sql)
def get_user_from_phone(phone):
	sql = 'select * from user where phone="{0}"'.format(
		torndb.MySQLdb.escape_string(str(phone)))
	return database(0, sql)

#buy.py
def get_showin(showin_id):
	if isDigit(showin_id):
		sql = 'select * from show_in where showin_id={0}'.format(showin_id)
		return database(0, sql)
	else:
		return None
def insert_ticket(cinema_id, movie_id, showin_id, user_id, room, seat):
	sql = 'insert into ticket(cinema_id, movie_id, showin_id, user_id, room, seat) values({0},{1},{2},{3},"{4}","{5}")'.format(
		cinema_id, movie_id, showin_id, user_id,
		torndb.MySQLdb.escape_string(str(room)),
		torndb.MySQLdb.escape_string(str(seat)) )
	database(1, sql)
	sql = 'select max(ticket_id) from ticket'
	return database(0, sql)[0]['max(ticket_id)']
def update_showin_seat(showin_id, seat):
	sql = 'update show_in set seat="{0}" where showin_id={1}'.format(
		torndb.MySQLdb.escape_string(str(seat)), showin_id)
	database(1, sql)
def insert_order(user_id, ticket_id, order_at, pay):
	sql = 'insert into `order`(user_id, ticket_id, order_at, pay) values({0},{1},"{2}",{3})'.format(
		user_id, ticket_id, order_at, pay)
	database(1, sql)

def get_order(user_id):
	sql = 'select * from `order` left join ticket on `order`.ticket_id = ticket.ticket_id where `order`.user_id={0}'.format(user_id)
	return database(0, sql)