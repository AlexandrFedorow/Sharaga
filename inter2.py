import math

import matplotlib.pyplot as plt
import numpy as np


def linear(x, y, xi):
    s1 = sum(x)
    s2 = sum(y)
    s3 = sum([i**2 for i in x])
    s4 = sum([x[i]*y[i] for i in range(len(x))])

    a0 = (s2 * s3 - s1 * s4) / (len(x) * s3 - s1**2)
    a1 = (len(x) * s4 - s1 * s2) / (len(x) * s3 - s1**2)
    print(a0, a1)

    return a0 + a1 * xi

def power(x, y, xi):
    s1 = sum(x)
    s2 = sum([i ** 2 for i in x])
    s3 = sum([i ** 3 for i in x])
    s4 = sum([i ** 4 for i in x])
    s5 = sum(y)
    s6 = sum([x[i] * y[i] for i in range(len(x))])
    s7 = sum([x[i]**2 * y[i] for i in range(len(x))])
    n = len(x)

    deta0 = np.linalg.det(np.array([[s5,s1,s2], [s6,s2,s3], [s7,s3,s4]]))
    deta1 = np.linalg.det(np.array([[n,s5,s2], [s1,s6,s3], [s2,s7,s4]]))
    deta2 = np.linalg.det(np.array([[n,s1,s5], [s1, s2, s6], [s2, s3, s7]]))
    N = np.linalg.det(np.array([[n,s1,s2], [s1,s2,s3], [s2,s3,s4]]))
    print(deta0/N, deta1/N, deta2/N)

    return deta0/N + deta1/N * xi + deta2/N * xi**2


def calculate_r_squared(actual, predicted):
    mean_actual = sum(actual) / len(actual)
    ss_total = sum((y - mean_actual) ** 2 for y in actual)
    ss_residual = sum((y_actual - y_predicted) ** 2 for y_actual, y_predicted in zip(actual, predicted))

    r_squared = 1 - (ss_residual / ss_total)

    return r_squared


x = np.array([3, 3.1, 3.2, 3.3, 3.4])
y = np.array([5.715, 5.935, 5.750, 5.741, 6.647])

plt.plot(x,y, 'o', label="Исходные точки")
plt.plot(x, [linear(x,y,i) for i in x],'--', label="Линейная аппроксимация")
plt.plot(x, [power(x,y,i) for i in x], label="Квадратная аппроксимация")
plt.legend(loc='best')
plt.grid()
print(calculate_r_squared(y, [linear(x,y,i) for i in x]))
print(calculate_r_squared(y, [power(x,y,i) for i in x]))
plt.show()