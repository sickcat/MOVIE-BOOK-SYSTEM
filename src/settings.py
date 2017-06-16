# !/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado
import tornado.template
import os
from tornado.options import define, options
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

# Make file paths relative to settings.
get_path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=5266, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
define('portStartCheck', default=5267, help='startcheck server port', type=int)
tornado.options.parse_command_line()

# Deployment Configuration 部署配置
# settings 配置
settings = dict()
settings['debug'] = True
settings['cookie_secret'] = "your-cookie-secret"
settings['buf_size'] = 4096 
settings['static_path'] = os.path.join(os.path.dirname(__file__), 'static')
settings['template_path'] = os.path.join(os.path.dirname(__file__), 'template')

settings['host'] = '127.0.0.1'
settings['database'] = 'ticket'
settings['user'] = 'root'
settings['password'] = '83147439'
settings['timezone'] = '+8:00'