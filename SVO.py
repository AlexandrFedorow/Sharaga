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
    if cpvo > c0:
        print('ПВО нет')
    return cpvo


def kvl(pd):
    pass


def knl():
    pass


def plot_points(points, title, subplot):
    x_vals = [point for point in points[0]]
    y_vals = [point for point in points[1]]

    subplot.plot(x_vals, y_vals, color='blue')

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


# Параметры
print(pvo(c0, cd, hd, hi, o))

# Визуализация
fig, axs = plt.subplots(1, 2, figsize=(12, 6))


plot_points([[c0, cd], [0, 1000]], 'Вертикальное распределение скорости звука', axs[0], )
plot_points(cord1, 'Траектория лучей в подводном канале', axs[1])

plt.tight_layout()
plt.show()