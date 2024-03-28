def is_it_good(a):
    p = []
    m = 0
    for i in a:
        for j in i:
            m += abs(j)
        p.append(m)
        m = 0
    if max(p) < 1:
        return True
    return False


def equ(x, a, b):
    x0 = [0, 0, 0, 0]

    for i in range(len(a)):
        for j in range(len(a[i])):
            x0[i]+=a[i][j]*x[j]
        x0[i]+=b[i]
    return x0


a = [
    [0, 0.22, -0.11, 0.31],
    [0.38, 0, -0.12, 0.22],
    [0.11, 0.23, 0, -0.51],
    [0.17, -0.21, 0.31, 0]
]

b = [2.7, -1.5, 1.2, -0.17]
epsilon = 1e-4

x = [i for i in b]

if is_it_good(a):
    while max([abs(x[i]-equ(x,a,b)[i]) for i in range(4)])>epsilon:

        x = equ(x,a,b)
        print(x)

