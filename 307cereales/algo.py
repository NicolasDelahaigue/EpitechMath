from utils import matRev, draw_matrice


def have_negatif():
    # print(min(matRev[-1]))
    if min(matRev[-1][0:5]) < 0.0:
        return True
    return False


def mmin(lst):
    if len(lst) is 0:
        return None, None
    less = 0
    for i in range(0, len(lst)):
        if lst[0] < lst[less]:
            less = i
    return less, lst[less]


# def init_tab(i):
#     ret = []
#     for j in matRev[:-1]:
#         ret.append(None if j[i] == 0 else j[10] / j[i])
#     return ret


def find_min():
    mi = min(matRev[-1][0:5])
    if matRev[-1][0:5].count(mi) != 1:
        col = []
        for i in range(0, 5):
            if matRev[-1][i] == mi:
                less, val = mmin([-1 if j[i] == 0 else j[10] / j[i] for j in matRev[:-1]])
                col.append({'x': i,
                            'y': less,
                            'value': val})
        lst = [j['value'] for j in col]
        return col[lst.index(max(lst))]
    else:
        less, val = mmin([-1 if j[matRev[-1].index(mi)] == 0 else j[10] / j[matRev[-1].index(mi)] for j in matRev[:-1]])
        return {'x': matRev[-1].index(mi), 'y': less, 'value': val}


def choose_pivot():
    dic = find_min()
    print(dic)
    ind = matRev[-1].index(min(matRev[-1][0:5]))
    p = matRev[0][ind]
    #print("{} {} {}".format(matRev[-1][0:5], p, ind))
    return p, ind


def algo():
    p, ind = choose_pivot()
    #print("{}_{}".format(ind, p))
    for i in range(0, len(matRev[0])):
        matRev[0][i] /= p
    for j in range(1, len(matRev)):
        p = matRev[j][ind]
        for i in range(0, len(matRev[j])):
            matRev[j][i] -= matRev[0][i] * p
    return [i[10] for i in matRev]

