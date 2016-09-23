#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from var import CFantom, CNone, CPlayer
from pair import pair
from utils import get_pos
from sys import stderr

__author__ = 'nicolas'
"""
y => ligne
x => colonne
N => y - 1, x
E => y, x + 1
S => y + 1, x
W => y, x - 1
"""


def test_calc(m, a, b, dim, ret):
    """
    Fait le calcul d'une case
    :param m: map
    :param a: postion case d'origine
    :param b: postion de la case entrain d'etre caluclé
    :param dim: dimention de la map
    :param ret: list des cases modifié
    :return: si le player est trouvé retourne True
    """
    if b.y in range(0, dim.y) and b.x in range(0, dim.x):
        if type(m[b.y][b.x]) is int:
            if m[b.y][b.x] == -1 or m[a.y][a.x] + 1 < m[b.y][b.x] :
                m[b.y][b.x] = m[a.y][a.x] + 1
                ret.append(b.copy())
        elif m[b.y][b.x] is CPlayer:
            return True
    return False


def calc_case(m, c, dim):
    """
    Fait le calcul de postion autour d'une case
    :param m: map
    :param c: position de la case sélectionné
    :param dim: dimention de la map
    :return: list des cases modifié
    """
    ret = []
    cb = pair(c.y - 1, c.x)
    l = [[0, 0], [1, 1], [1, -1], [-1, -1]]
    for i in range(0, 4):
        cb.y += l[i][0]
        cb.x += l[i][1]
        if test_calc(m, c, cb, dim, ret) is True:
            raise Exception("Leave")
    return ret


def init_beg(m, dim):
    """
    Initialise le parcour place les 0 autour du fantom
    :param m: map
    :param dim: dimention de la map
    :return: list des cases où il y a un 0
    """
    l = []
    p = get_pos(m, CFantom)
    for j in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        b = pair(p.y + j[0], p.x + j[1])
        if b.y in range(0, dim.y) and b.x in range(0, dim.x) and type(m[b.y][b.x]) is int:
            m[b.y][b.x] = 1
            l.append(b)
    return l


def handle_loop(ret, m, dim):
    r = []
    for j in ret:
        try:
            r.extend(calc_case(m, j, dim))
        except Exception as e:
            if e.args[0] is "Leave":
                return []
            else:
                print >> stderr, "Erreur inconnu"
                exit(84)
    return r


def algo(mp):
    """
    algorythme
    :param mp: map
    :return: nouvelle map
    """
    m = [[j if j is not CNone else int(-1) for j in i] for i in mp]
    dim = pair(len(m), len(m[0]))
    ret = init_beg(m, dim)
    while len(ret) > 0:
        ret = handle_loop(ret, m, dim)
    return m