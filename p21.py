import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return x**3 - 3 * x**2 + 12 * x-9


def derivative_f(x, a, b):
    h = (b-a)/100
    return (f(x + h) - f(x)) / h


def second_derivative_f(a, b):
    h = (b-a)/100
    return f(a + 2 * h) - 2 * f(a + h) + 2 * f(a)


a = 0
b = 3

epsilon = 1e-7

x = f(a)
y = second_derivative_f(a, b)

x0 = a

if x * y < 0:
    x0 = b


x1 = x0 - f(x0)/derivative_f(x0, a, b)

while abs(x1 - x0) > epsilon:
    x0 = x1
    x1 = x0 - f(x0)/derivative_f(x0, a, b)

x = x1




plt.plot(np.linspace(a, b, 100), [f(i) for i in np.linspace(a, b, 100)],
         [i for i in range(4)], [0 for i in range(4)])

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print("Roots on the interval: ", x)