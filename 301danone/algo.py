#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'kevin'


class Algo:
    def __init__(self, l):
        self.__list = l
        self.__nb_elem = len(l)
        self.__result = {
            "insert": 0,
            "select": 0,
            "bubble": 0,
            "merge": 0,
            "quick": 0
        }

    def insert(self):
        lst = self.__list[:]
        i = 1
        while i < len(lst):
            tmp = lst.pop(i)
            j = 0
            while j < i:
                self.__result["insert"] += 1
                if tmp < lst[j]:
                    break
                j += 1
            lst.insert(j, tmp)
            i += 1

    def select(self):
        tmp = self.__list[:]
        l = len(self.__list)
        for i in range(0, l):
            mini = i
            for j in range(i + 1, l):
                self.__result["select"] += 1
                if tmp[j] < tmp[mini]:
                    mini = j
            if min != i:
                tmp[i], tmp[mini] = tmp[mini], tmp[i]

    def bubble(self):
        tmp = self.__list[:]
        l = len(self.__list) - 1
        for i in range(l, 0, -1):
            for j in range(0, i):
                self.__result["bubble"] += 1
                if tmp[j] > tmp[j + 1]:
                    tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]

    def __merge_loop(self, lst):
        if len(lst) > 1:
            ta = self.__merge_loop(lst[0:int(len(lst) / 2)])
            tb = self.__merge_loop(lst[int(len(lst) / 2):len(lst)])
            del lst[:]
            while len(ta) > 0 or len(tb) > 0:
                if len(ta) == 0:
                    lst.extend(tb)
                    del tb[:]
                elif len(tb) == 0:
                    lst.extend(ta)
                    del ta[:]
                else:
                    self.__result["merge"] += 1
                    lst.append(tb.pop(0) if tb[0] < ta[0] else ta.pop(0))
        return lst

    def merge(self):
        self.__merge_loop(self.__list[:])

    def __partition(self, tab, f, l):
        while f < l:
            while f <= l:
                self.__result["quick"] += 1
                if tab[f] > tab[l]:
                    tab[f], tab[l] = tab[l], tab[f]
                    break
                l -= 1
            while f <= l:
                self.__result["quick"] += 1
                if tab[f] > tab[l]:
                    tab[f], tab[l] = tab[l], tab[f]
                    break
                f += 1
        return f

    def __tri_rapide(self, tab, first, last):
        if first < last:
            pivot = self.__partition(tab, first, last - 1)
            self.__tri_rapide(tab, first, pivot)
            self.__tri_rapide(tab, pivot + 1, last)

    def quick(self):
        lst = self.__list[:]
        self.__tri_rapide(lst, 0, len(lst))

    def run(self):
        self.select()
        self.insert()
        self.bubble()
        self.merge()
        self.quick()
        self.rapport()

    def rapport(self):
        print "{} élément{}".format(self.__nb_elem, 's' if self.__nb_elem != 1 else '')
        print "tri par sélection: {} comparaisons".format(self.__result["select"])
        print "tri par insertion: {} comparaisons".format(self.__result["insert"])
        print "tri par bulles: {} comparaisons".format(self.__result["bubble"])
        print "tri par fusion: {} comparaisons".format(self.__result["merge"])
        print "tri par rapide: {} comparaisons".format(self.__result["quick"])
