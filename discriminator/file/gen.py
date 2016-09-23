#! /usr/bin/python3.4

import random
from sys import argv as a

random.seed()

if __name__ == "__main__":
    if len(a) is 4:
        st = ""
        for _ in range(0, int(a[1])):
            st += "{};{}\n".format(*[random.uniform(int(a[2]), int(a[3])) for _ in range(2)])
    print(st, end='')
