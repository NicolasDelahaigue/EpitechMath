#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'nicolas'


def draw_matrice(A):
    """
    Affichage de la matrice
    :param A: Matrice
    :return: None
    """
    for i in A:
        print '[{}]'.format(' '.join(str(x) for x in i))


def init_matrice(l, makefile):
    """
    Créé la matrice de lien
    :param l: liste des clés
    :param makefile: graph du makefile
    :return: matrice de lien
    """
    l.sort()
    A = [[0] * len(l) for _ in range(0, len(l))]
    for i in l:
        if i in makefile.keys():
            for j in makefile[i][0]:
                A[l.index(i)][l.index(j)] = 1
    return A