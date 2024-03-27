

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

def check_epsilon(x0, x1, e):
    ctr = 0
    for i in range(len(x0)):
        if abs(x1[i]-x0[i]) < e:
            ctr += 1
            if ctr == 4:
                print('ff')
                return False
            else:
                ctr = 0
    return True


a = [
    [0, 0.22, -0.11, 0.31],
    [0.38, 0, -0.12, 0.22],
    [0.11, 0.23, 0, -0.51],
    [0.17, -0.21, 0.31, 0]
]

b = [2.7, -1.5, 1.2, -0.17]
epsilon = 1e-4

x0 = [i for i in b]
x1 = [0, 0, 0, 0]
x2 = x1


if is_it_good(a):
    while check_epsilon(x0, x2, epsilon):
        print('gg')

        for i in range(len(a)):
            for j in range(len(a[i])):
                x1[i] += a[i][j]*x0[j]
            x1[i] += b[i]
        print(x0)
        x0 = x1
        x2 = x1
        print(x2)
        x1 = [0, 0, 0, 0]


print(x2)
