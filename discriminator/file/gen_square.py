#! /usr/bin/python3

__author__ = 'kevin'

import sys
import random
random.seed()


def main(av):
    try:
        st = ""
        for i in range(int(av[0])):
            st += "{};{}\n".format(random.uniform(int(av[1]), int(av[3])),
                                   random.uniform(int(av[2]), int(av[4])))

        print(st)

    except ValueError:
        print("param must be Integer: ")


if __name__ == "__main__":
    if len(sys.argv) is 6:
        main(sys.argv[1:])
    else:
        print("./gen_square <nb_points> <x1> <y1> <x2> <y2>")
