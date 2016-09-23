#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'kevin'

import define as d
from sys import stderr
from matrice import prod_mat, bilan_last_elem

def read_file(path):
    """
    Lecture du fichier et remplissage d'une liste des liens entre les personnes
    :param path: chemin vers le fichier
    :return: double liste
    """
    list = []
    try:
        with open(path) as f:
            for data in f:
                if data.count(d.sep2) >= 1:
                    a, b = data.split(d.sep2)
                else:
                    a, b = data.split(d.sep1)
                list.append([a.strip('\n'), b.strip('\n')])
        return list
    except IndexError:
        print >> stderr, d.file
        exit(84)
    except IOError as e:
        print >> stderr, e
        exit(84)


def create_list(l):
    """
    Créé une liste unique des personnes
    :param l: liste des liens entre les personnes
    :return: liste des personnes
    """
    ret = []
    for e in l:
        for i in e:
            if i not in ret:
                ret.append(i)
    ret.sort()
    return ret


def create_link(file, liyist):
    """
    Créé une matrice et la rempli avec les liens direct
    :param file: liste des liens
    :param liyist: liste de nom unique
    :return: matrice de liens direct
    """
    A = [[0] * len(liyist) for _ in range(0, len(liyist))]
    for i in file:
        try:
            A[liyist.index(i[0])][liyist.index(i[1])] = 1
            A[liyist.index(i[1])][liyist.index(i[0])] = 1
        except:
            print >> stderr, 'oh mince une erreur'
            exit(84)
    return A


def draw_matrice(A):
    """
    Affiche la matric sous forme de tableau
    :param A: Matrice
    """
    print ''
    for i in A:
        print ' '.join(str(x) for x in i)


def link_person(par, liyist, A):
    """
    Trouve le degré de séparation entre deux personnes
    :param par: les deux noms des personnes
    :param liyist: liste des personne unique
    :param A: matrice originel
    """
    try:
        x = liyist.index(par[0])
        y = liyist.index(par[1])
        link = 0
        lA = [A]
        while par[0] != par[1] and link is 0 and len(lA) < len(liyist) + 1:
            link = bilan_last_elem(lA, x, y)
            lA.append(prod_mat(lA[len(lA) - 1], A))
        if link == 0 and par[0] != par[1]:
            link = -1
        print 'degré de séparation entre {} et {} : {}'.format(par[0], par[1], link)
    except ValueError as e:
        print 'degré de séparation entre {} et {} : {}'.format(par[0], par[1], -1)
