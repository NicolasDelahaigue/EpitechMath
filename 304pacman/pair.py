#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'nicolas'


class pair:
    y = 0
    x = 0

    def __init__(self, _y, _x):
        self.y = _y
        self.x = _x

    def __str__(self):
        return '<p:' + str(self.y) + ',' + str(self.x) + '>'

    def __call__(self, *args, **kwargs):
        return [self.y, self.x]

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, item):
        return self

    def copy(self):
        return pair(self.y, self.x)
