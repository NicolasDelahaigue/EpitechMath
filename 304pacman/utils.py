#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from sys import stderr, stdout
from var import colorF, colorP, CPlayer, CFantom, CList, CWall, CNone
from pair import pair

__author__ = 'nicolas'


def read_file(path):
    """
    Lecture du fichier et remplis une list
    :param path: chemin vers le fichier
    :return: list
    """
    lst = []
    try:
        with open(path) as f:
            for data in f:
                data = data.strip('\n')
                lst.append(data)
        return lst
    except IOError as e:
        print >> stderr, e
        exit(84)


def check_map(mp):
    """
    check la bonne composition d'une map
    :param mp: map
    :return: None
    """
    try:
        if len(set([len(j) for j in mp])) != 1:
            raise Exception("Not a square")
        if ''.join(mp).count(CFantom) != 1:
            raise Exception("Wrong number of Fantom")
        if ''.join(mp).count(CPlayer) != 1:
            raise Exception("Wrong number of Player")
        if len(set(''.join(mp) + CList)) != len(CList):
            raise Exception("Wrong letter")
    except Exception as st:
        print >> stderr, "Wrong map : " + ' '.join(st.args)
        exit(84)


def draw_map(mp, ca, cb, color=False):
    """
    Affiche de la map en avec les caractères voulu
    :param mp: map
    :param ca: caractères pacman
    :param cb: caractère fantome
    :param color: activation des couleurs
    :return: None
    """
    l = {CPlayer: CPlayer, CFantom: CFantom, CWall: ca[:1], CNone: cb[:1]}
    if color is True:
        l[CPlayer] = colorP + l[CPlayer] + '\033[0m'
        l[CFantom] = colorF + l[CFantom] + '\033[0m'
    for i in mp:
        for j in i:
            if type(j) is int:
                c = l[CNone] if j < 0 else str(j % 10)
            else:
                c = l[j] if j in l.keys() else j
            stdout.write(c)
        stdout.write('\n')


def get_pos(m, charact):
    """
    donne la position d'un caractère
    :param m: liste
    :param charact: caractère
    :return: coordonées x, y
    """
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if m[i][j] is charact:
                return pair(i, j)
