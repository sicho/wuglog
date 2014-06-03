# -*- coding:utf-8 -*-

import sys
import yaml
sys.path.append('vendor/bottle');

from bottle import route, template

import app.models.wuglog
wuglog = app.models.wuglog.WugLog()

@route('/wuglog')
def index():
    return template('content', data={
        'video': wuglog.video(True),
        'music': wuglog.music(True),
        'book': wuglog.book(True),
        'other': wuglog.other(True),
        })
