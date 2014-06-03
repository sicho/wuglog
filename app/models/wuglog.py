# -*- coding:utf-8 -*-

import yaml

class WugLog:
    def video(self, have):
        f = open('data/video.yml').read().decode('utf-8')
        return yaml.load(f)

    def music(self, have):
        f = open('data/music.yml').read().decode('utf-8')
        return yaml.load(f)

    def book(self, have):
        f = open('data/book.yml').read().decode('utf-8')
        return yaml.load(f)

    def other(self, have):
        f = open('data/other.yml').read().decode('utf-8')
        return yaml.load(f)

