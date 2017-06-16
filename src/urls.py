# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#from handler.getData.foo import FooHandler
from handler.foo import FooHandler
from handler.index import MainHandler
from handler.index import IndexHandler
from handler.movie import MovieHandler
from handler.register import RegisterHandler
from handler.loginout import LoginHandler
from handler.loginout import LogoutHandler
from handler.buy import BuyHandler
from handler.order import OrderHandler
url_patterns = [

    #Test server
    (r"/foo", FooHandler),
    (r'/index/(\w+)', MainHandler),
    (r'/index', MainHandler),
    (r'/movie/(\w+)', MovieHandler),
    (r'/buy/(\w+)', BuyHandler),
    (r'/register', RegisterHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/order', OrderHandler),
    (r'.*', IndexHandler),
]
