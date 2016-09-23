#! /usr/bin/python3.4

__author__ = 'kevin et nicolas <3'

import random
import begin


@begin.start
def gen(nb, mi, ma):
    nb, mi, ma = int(nb), int(mi), int(ma)
    if mi > ma:
        print("min must be inferior at max")
        return
    if ma == 0:
        print("max number must be higher than 0")
        return
    while nb > 0:
        print(random.randrange(mi, ma), end=' ')
        nb -= 1
