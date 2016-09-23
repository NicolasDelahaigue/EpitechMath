from verbose import verb_fxp, verb_tab, verb_gauss
from sys import stderr

__author__ = 'nicolas'


isround = True


def error(st):
    print(st, file=stderr)
    exit(84)


def check_zero(mat, i):
    for j in range(0, len(mat)):
        if j != i and mat[j][i] != 0:
            return j
    return 0


# calcul tout les f[xn, xn+1] et les f[xn, xn+1, xn+2]
def fxp(tab):
    fxp2 = [(tab[i + 1][1] - tab[i][1]) / (tab[i + 1][0] - tab[i][0]) for i in range(0, len(tab) - 1)]
    fxp3 = [(fxp2[i + 1] - fxp2[i]) / (tab[i + 2][0] - tab[i][0]) for i in range(0, len(fxp2) - 1)]
    verb_tab(tab)
    verb_fxp(fxp2, fxp3)
    return fxp2, fxp3


def add(l):
    return [0 for _ in range(0, l)]


def tab_gauss(fxabc):
    mat = [[1, 0, 0, 0, 0],
           [1/2, 2, 1/2, 0, 0],
           [0, 1/2, 2, 1/2, 0],
           [0, 0, 1/2, 2, 1/2],
           [0, 0, 0, 0, 1]]
    secmem = [0] + [6 * i for i in fxabc] + [0]
    verb_gauss(mat, secmem)
    return mat, secmem


def draw(vec, lst, l):
    j = 0.0
    pas = 20 / (l - 1) if l > 1 else 21
    print("vecteur résultat :", [0.0 if round(i, 1) == 0.0 else round(i, 1) for i in vec])
    vac = []
    for i in lst:
        vac.append(j)
        if isround is True:
            print("abscisse : {} cm\trayon : {} cm".format(round(j, 1), round(i, 1)))
        else:
            print("abscisse : {} cm\trayon : {} cm".format(j, i))
        j += pas

