from math import ceil

prod = ["avoine: ",
        "blé:    ",
        "maïs:   ",
        "orge:   ",
        "soja:   "]

mat = [[1, 1, 2, 0],
       [0, 2, 1, 0],
       [1, 0, 0, 3],
       [0, 1, 1, 1],
       [2, 0, 0, 2]]

#          x1 x2 x3 x4 x5 x6 x7 x8 x9 f  b
matRev = [[1, 0, 1, 0, 2, 1, 0, 0, 0, 0, 0],
          [1, 2, 0, 1, 0, 0, 1, 0, 0, 0, 0],
          [2, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 3, 1, 2, 0, 0, 0, 1, 0, 0]]


def beg(lst):
    print("ressources : {} E1, {} E2, {} E3, {} E4\n".format(lst[0], lst[1], lst[2], lst[3]))


def mid(qu, pr):
    lst = []
    l = 0
    for j in qu:
        lst.append("{} unité{}".format(j, "s" if j > 1.0 else ""))
        l = len(lst[-1]) if len(lst[-1]) > l else l
    for j in range(0, len(lst)):
        lst[j] = lst[j].ljust(l + 5)
    for i in range(0, len(prod)):
        print("{}{}à {} €/unité".format(prod[i], lst[i], pr[i]))


def end(val):
    print("\nvaleur totale de la production : {} €".format(val))


def init_matrice(en, pr):
    try:
        for i in range(0, len(en)):
            matRev[i][10] = en[i]
        matRev.append([-j for j in pr])
        matRev[-1].extend([0, 0, 0, 0, 1, 0])
    except IndexError:
        pass


def draw_matrice():
    for j in matRev:
        print("{}{}{}{}{}|{}{}{}{}|{}|{}".format(*[str(i).ljust(5) for i in j]))
