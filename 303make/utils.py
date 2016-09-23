#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from sys import stderr, stdout

__author__ = 'nicolas'


def read_file(path):
    """
    Lecture du fichier et remplis dictionnaire de double list
    :param path: chemin vers le fichier
    :return: dictionaire de double liste
    """
    dic = {}
    last = None
    try:
        with open(path) as f:
            for data in f:
                data = data.strip('\n')
                tmp = data.split(':')
                if len(tmp) > 1:
                    dic[tmp[0]] = [tmp[1].strip(' ').split(' '), []]
                    last = tmp[0]
                else:
                    tmp[0] = tmp[0].strip(' \t')
                    if last is not None and tmp[0] is not '':
                        dic[last][1].append(tmp[0])
        return dic
    except IOError as e:
        print >> stderr, e
        exit(84)


def define_rules(makefile, key=True):
    """
    Créé une liste de tout les des dépendance si key = True les clés sont comprises dedans
    :param makefile: graph représentant le makefile
    :param key: si key == True les clés sont comprises dans la liste
    :return: liste unique des dépendances trié
    """
    ret = []
    if key is True:
        ret.extend(makefile.keys())
    for i in makefile.keys():
        ret.extend(makefile[i][0])
    ret = list(set(ret))
    ret.sort()
    return ret


def print_order(elem, beg='', end=''):
    """
    affiche le contenu d'un liste
    :param elem: liste
    :param beg: string à afficher avant
    :param end: string à afficher après
    :return: None
    """
    elem.sort()
    stdout.write(beg)
    for i in elem:
        print i
    stdout.write(end)


def rules_to_exec(board, rules):
    """
    trouve les règles à exécuter
    :param board: liste de petites fleches
    :param rules: règle à trouver
    :return: list des règles à exécuter
    """
    lst = [j.split(' -> ') for j in board]
    t = []
    for v in lst:
        if rules == v[0]:
            t.extend(v[1:])
    t = list(set(t))
    t.reverse()
    return t
