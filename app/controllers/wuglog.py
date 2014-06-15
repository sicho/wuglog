# -*- coding:utf-8 -*-

import sys
import yaml

from bottle import route, template, url

import app.models.wuglog
wuglog = app.models.wuglog.WugLog()

@route('/wuglog')
def index():
    video = wuglog.video(True)
    music = wuglog.music(True)
    book = wuglog.book(True)
    other = wuglog.other(True)

    data = {
            'video': video,
            'music': music,
            'book': book,
            'other': other,
            }

    total = len(video + music + book + other)
    have = len([item for item in video if item['have']]) \
            + len([item for item in music if item['have']]) \
            + len([item for item in book if item['have']]) \
            + len([item for item in other if item['have']])

    return template('content', url = url, data = data, total = total, have = have)
