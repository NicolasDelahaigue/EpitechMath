#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from sys import stderr, stdout
from var import deb, debm, mid, dur

__author__ = 'nicolas'


def read_file(path):
    """
    Lecture du fichier et remplis une list
    :param path: chemin vers le fichier
    :return: list
    """
    lst = {}
    try:
        with open(path) as f:
            for data in f:
                data = data.strip('\n')
                p = data.split(';')
                lst[p[0]] = [[0 for i in range(4)]]
                lst[p[0]][0][3] = int(p[2])
                lst[p[0]].append(p[3:])
        return lst
    except IOError as e:
        print >> stderr, e
        exit(84)


def write_weeks(dic, lst):
    """
    Affiche le nombre de semaines
    :param dic: dictionaire
    :param lst: list des clé dans l'ordre
    :return: None
    """
    t = dic[lst[-1]][0][1] - dic[lst[0]][0][0]
    print "{}{} semaines".format(dur, t)


def write_time(dic, lst):
    """
    Affiche le temps de la tache
    :param dic: dictionnaire
    :param lst: list des clés dans l'ordre
    :return: None
    """
    stdout.write('\n')
    for i in lst:
        if dic[i][0][2] is 0:
            print "{}{}{}".format(i, deb, dic[i][0][0])
        else:
            print "{}{}{}{}{}".format(i, debm, dic[i][0][0], mid, dic[i][0][0] + dic[i][0][2])


def write_planning(mp, lst):
    """
    Affiche le diagramme de gantt
    :param mp: dictionaire
    :param lst: list des clés dans l'ordre
    :return: None
    """
    stdout.write('\n')
    for i in lst:
        print "{}   ({})    {}{}".format(i, mp[i][0][2], ''.join([' ' for k in range(0, mp[i][0][0])]), ''.join(['=' for g in range(0, mp[i][0][3])]))
