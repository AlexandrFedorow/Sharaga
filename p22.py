import matplotlib.pyplot as plt
import math
import numpy as np
import math


def f(x):
    return x**3 - 0.2 * x**2 + 0.3 * x - 1.2


def derivative_f(x, a, b):
    h = (b-a)/100
    return (f(x + h) - f(x)) / h


def second_derivative_f(a, b):
    h = (b-a)/100
    return f(a + 2 * h) - 2 * f(a + h) + 2 * f(a)


a = 0.1
b = 3

epsilon = 1e-7
roots = 0

x = f(a)
y = second_derivative_f(a, b)

x0 = a
c = b

if x * y < 0:
    x0 = b
    c = a

x1 = (x0 * f(c) - c * f(x0))/(f(c) - f(x0))

while abs(x1 - x0) > epsilon:
    x0 = x1
    x1 = (x0 * f(c) - c * f(x0))/(f(c) - f(x0))

x = x1


plt.plot(np.linspace(a, b, 100), [f(i) for i in np.linspace(a, b, 100)],
         [i for i in range(4)], [0 for i in range(4)])

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print("Roots on the interval: ", x)