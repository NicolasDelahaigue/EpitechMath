__author__ = 'nicolas'

from verbose import verb_all_f
from utils import check_zero


# système 6
# f" => utiliser le pivot de gauss
def fprime(fus, secm):
    mat = fus.copy()
    for i in range(0, len(mat)):
        mat[i].append(secm[i])
    for i in range(0, len(mat)):
        while True:
            mx = mat[i][i]
            for j in range(0, len(mat[i])):
                mat[i][j] /= mx
            t = check_zero(mat, i)
            if t == 0:
                break
            tmp = mat[i].copy()
            k = mat[t][i]
            for m in range(0, len(tmp)):
                tmp[m] *= k
            for m in range(0, len(mat[0])):
                mat[t][m] -= tmp[m]
    return [j[-1] for j in mat]


# système 14
# f f' f" f"'
def all_f(tab, fpr, a):
    # calcul tout les f f' f" f"'
    # sous forme [[f0, f0', f0", f0"'],...,[fn, fn', fn", fn"']
    ftab = []
    for i in range(0, len(tab) - 1):
        ftab.append([tab[i][1]])
        ftab[-1].append(a[i] - (5 * fpr[i]) / 3 - (5 * fpr[i + 1]) / 6)
        ftab[-1].append(fpr[i])
        ftab[-1].append((fpr[i + 1] - fpr[i]) / 5)
    verb_all_f(ftab)
    return ftab


# système 1
# calcul du polynome
# pi(x) = fi + fi' * (x - xi) + (fi"/2!) * (x - i)² + (fi"'/3!) * (x - xi)³
def calc_pol(ftab, x, i):
    val = x - (i * 5)
    ret = ftab[i][0] + ftab[i][1] * val + (ftab[i][2] / 2) * pow(val, 2) + (ftab[i][3] / 6) * pow(val, 3)
    return ret


# change de polynome entre les écart fixes (0-5-10-15-20)
def loop(ftab, l):
    result = []
    i = 0
    j = 0.0
    pas = 20 / (l - 1) if l > 1.0 else 21
    while True:
        if j > (i + 1) * 5:
            i += 1
        result.append(calc_pol(ftab, j, i))
        j += pas
        if j > 20:
            break
    return result
