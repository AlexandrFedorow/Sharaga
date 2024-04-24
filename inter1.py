import matplotlib.pyplot as plt
import math
import numpy as np
import math


def lagrange_polynomial(x, xy_pairs):
    n = len(xy_pairs)
    result = 0

    for i in range(n):
        xi, yi = xy_pairs[i]
        term = yi
        for j in range(n):
            if j != i:
                xj, _ = xy_pairs[j]
                term *= (x - xj) / (xi - xj)
        result += term

    return result


ksi = 0.25
xy_pairs = [(0.2143, 0.0284), (0.2572, 0.0335), (0.3269, 0.0416), (0.4282, 0.0526), (0.5657, 0.0663)]

plt.plot(np.linspace(0.2143, 0.5657, num=100),
         [lagrange_polynomial(i, xy_pairs) for i in np.linspace(0.2143, 0.5657, num=100)],  label="Полином Лагранжа")

plt.plot([xy_pairs[i][0] for i in range(len(xy_pairs))],
         [xy_pairs[i][1] for i in range(len(xy_pairs))], 'o', label="Исходные точки")

plt.plot(ksi, lagrange_polynomial(ksi, xy_pairs), 'o',
            marker="D", label="Точка при аргументе " + str(ksi))

plt.legend(loc='best')
plt.grid()
print(lagrange_polynomial(ksi, xy_pairs))
plt.show()