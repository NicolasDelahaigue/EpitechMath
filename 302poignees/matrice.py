#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'kevin'


def prod_mat(A, B):
    """
    Fonction calculant le produit de 2 matrice
    :param A: matrice
    :param B: matrice
    :return: A*B
    """
    q = len(B[0])
    return [[sum([x*y[j] for (x, y) in zip(a, B)]) for j in range(q)] for a in A]


def calc_mat(A, n):
    """
    Créé une liste de matrice (A^1... A^n)
    :param A: matrice originel
    :param n: nombre de matrice
    :return: liste de toute les matrice
    """
    lA = [A]
    for i in range(n - 1):
        lA.append(prod_mat(lA[len(lA) - 1], A))
    return lA


def bilan_last_elem(lA, x, y):
    """
    Bilan de la derniere matrice de la liste
    :param lA: liste de matrices
    :param x: position x dans une matrice
    :param y: position y dans une matrice
    :return: lien a dans la dernière matrice
    """
    i = len(lA) - 1
    if lA[i][y][x] > 0:
        return i + 1
    return 0


def bilan_mat(lA):
    """
    Bilan des matrices
    :param lA: liste des matrices (A^1...A^n)
    :return: matrice bilan
    """
    A = [[0] * len(lA[0]) for _ in range(0, len(lA[0]))]
    # parcour list de matrices
    for i in range(len(lA)):
        # parcour ligne par ligne de la matric
        for y in range(len(lA[i])):
            # parcour colonne par colonne d'une ligne
            for x in range(len(lA[i][y])):
                if A[y][x] is 0 and lA[i][y][x] > 0:
                    A[y][x] = i + 1
    return A


def clean_dia(A):
    """
    supprimer les liens entre eux meme
    :param A: matrice
    :return: matrice
    """
    for i in range(0, len(A)):
        A[i][i] = 0
    return A
