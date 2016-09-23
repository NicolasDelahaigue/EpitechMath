__author__ = 'nicolas'

fxp = False
vtab = False
vgauss = False
vallf = False


def verb_tab(tab):
    if vtab is False:
        return
    print("xi\tf(xi)")
    for i in tab:
        print(str(i[0]) + "\t" + str(i[1]))
    print()


def verb_fxp(fxab, fxabc):
    if fxp is False:
        return
    print("\033[34mfxab :\033[0m\tf[xi, xi+1] = (f(xi+1) - f(xi)) / (xi+1 - xi)\nvalue : ", fxab, "\n")
    print("\033[34mfxabc :\033[0m\tf[xi, xi+1, xi+2] = (f[xi+1, xi+2] - f[xi, xi+1]) / (xi+2 - xi)\nvalue : ", fxabc, "\n")


def verb_gauss(mat, secmem):
    if vgauss is False:
        return
    print("Système à résoudre")
    le = max([len(str(k)) for k in secmem])
    for i in range(0, len(mat)):
        print("[ ", end='')
        for j in mat[i]:
            print("{:<4}".format(j), end='')
        print("] [ f\"" + str(i) + " ] " + ("=" if i == 2 else " ") + " [ " + "{:<{}s}".format(str(secmem[i]), le) + " ]")
    print()


def verb_all_f(ftab):
    if vallf is False:
        return
    for i in range(0, len(ftab)):
        print("| f" + str(i), "   =", ftab[i][0])
        print("| f'" + str(i), "  =", ftab[i][1])
        print("| f''" + str(i), " =", ftab[i][2])
        print("| f'''" + str(i), "=", ftab[i][3], "\n")
    print()
