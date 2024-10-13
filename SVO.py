import numpy as np
import matplotlib.pyplot as plt
import math

cord1 = [[0, 6102, 6102, 16984, 16984, 17882],[400, 0, 0, 1000, 1000, 900]]


c0 = 1480   # Скорость у поверхноси
cd = 1455   # Скорость у дна
o = 15  # Ширина ХН
hi = 400    # Глубина источника излучения
hc = 150    # Глубина цели

hd = 1000   # Глубина нашего моря ОНА У ВСЕХ ТАКАЯ
hp = 0  # Поверхность ОНА У ВСЕХ ТАКАЯ


def pvo(c0, cd, hd, hi, o):
    g = (cd - c0) / hd
    ci = c0 + g * hi
    cpvo = ci/math.cos(math.radians(o/2))
    hpvo = 0
    if cpvo > c0:
        print('ПВО нет')
        hpvo = 0
    return ci, hpvo


def kvl(c, hi, o, hp, hd, hpvo, n):
    h = []
    r = []

    for i in range(n-1):
        o.append(math.degrees(math.acos(math.cos(math.radians(o[len(o)-1])) * c[i+1] / c[i])))

    if hpvo == 0:
        h = [hi, hd]
    else:
        h = [abs(hd - hpvo - hi), hd]

    for i in range(n-1):
        r.append(h[i]/math.tan(math.radians((o[i]+o[i+1])/2)))

    return o, r, h


def knl(c, hi, o, hp, hd, hpvo, n):
    h = []
    r = []

    for i in range(n - 1):
        o.append(math.degrees(math.acos(math.cos(math.radians(o[len(o) - 1])) * c[i + 1] / c[i])))

    if hpvo == 0:
        h = [hd-hi, hd]
    else:
        h = [hd-hi, hpvo]

    for i in range(n - 1):
        r.append(h[i] / math.tan(math.radians((o[i] + o[i + 1]) / 2)))

    return o, r, h


def make_coords(r, h, hi, hd, hpvo, ch):
    coords = [[0],[hi]]
    if hpvo == 0:
        for i in range(len(r)):
            coords[0].append(coords[0][i]+r[i])
            if ch:
                coords[1].append(hd)
                ch = False
            else:
                coords[1].append(0)
                ch = True
    else:
        for i in range(len(r)):
            coords[0].append(coords[0][i]+r[i])
            if ch:
                coords[1].append(hpvo)
                ch = False
            else:
                coords[1].append(hd)
                ch = True

    return coords


def plot_points(points1, points2, title, subplot, ch):
    x_vals = [point for point in points1[0]]
    y_vals = [point for point in points1[1]]

    subplot.plot(x_vals, y_vals, color='blue')
    if ch:
        x_vals = [point for point in points2[0]]
        y_vals = [point for point in points2[1]]
        subplot.plot(x_vals, y_vals, color='red')

    subplot.set_xlim(min(x_vals), max(x_vals))
    subplot.set_ylim(min(y_vals), max(y_vals))

    #subplot.set_aspect('equal', adjustable='box')
    subplot.xaxis.set_label_position('top')
    subplot.xaxis.set_ticks_position('top')
    subplot.invert_yaxis()
    subplot.set_title(title)
    subplot.set_xlabel('x')
    subplot.set_ylabel('y')
    subplot.grid(True)



ci, hpvo = pvo(c0, cd, hd, hi, o)
print(ci)
o1, r, h = kvl([ci, c0, cd], hi, [o/2], hp, hd, hpvo, 3)
coords1 = make_coords(r, h, hi, hd, hpvo, False)

o1, r, h = knl([ci, c0, cd], hi, [o/2], hp, hd, hpvo, 3)
coords2 = make_coords(r, h, hi, hd, hpvo, True)



fig, axs = plt.subplots(1, 2, figsize=(12, 6))


plot_points([[c0, cd], [0, 1000]], [], 'Вертикальное распределение скорости звука', axs[0], False)
plot_points(coords1, coords2, 'Траектория лучей в подводном канале', axs[1], True)


plt.tight_layout()
plt.show()