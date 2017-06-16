# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
import tornado

from settings import settings
from urls import url_patterns

# noinspection PyAbstractClass
class TicketSystem(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = TicketSystem()
    http_server = tornado.httpserver.HTTPServer(app, max_buffer_size=1024 * 1024 * 1024)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
