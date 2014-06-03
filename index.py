# -*- coding: utf-8 -*-

import sys
sys.path.append('vendor/bottle')

from bottle import route, static_file, run
from app.controllers import *

@route('/public/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public')

run(host='192.168.58.11', port=8080, debug=True, reloader=True)
