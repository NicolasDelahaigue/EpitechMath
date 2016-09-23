#! /usr/bin/python3.4
# coding=utf-8

__author__ = 'kevin'

import time
import functools
import var


def banch(func):
    @functools.wraps(func)
    def wrapper(*args, **kawrg):
        if var.time:
            t = time.clock()
            res = func(*args, **kawrg)
            print("{}: {:5f}".format(func.__name__, time.clock() - t))
            return res
        else:
            return func(*args, **kawrg)

    return wrapper


def aff(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if var.aff:
            res = func(*args, **kwargs)
            print(func.__name__, ": ", *res)
            return res
        else:
            return func(*args, **kwargs)

    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(u"{}: {} récursions".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper
