# -*- coding: utf-8 -*-

import sys

from bottle import route, static_file, default_app
from app.controllers import *

@route('/wuglog/public/<filepath:path>', name='static_file')
def server_static(filepath):
    return static_file(filepath, root='./public')

app = default_app()
