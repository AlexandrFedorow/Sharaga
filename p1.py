import matplotlib.pyplot as plt
import math
import numpy as np
import math


def f(x):
    return 1/math.tan(1.01*x) - x**2


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
x1 = b
c = b

if x * y < 0:
    x0 = b
    x1 = a
    c = a

x2 = (x0 * f(c) - c * f(x0))/(f(c) - f(x0))
x3 = x1 - f(x1)/derivative_f(x1, a, b)

while abs(x3 - x2) > 2 * epsilon:
    x0 = x2
    x2 = (x0 * f(c) - c * f(x0))/(f(c) - f(x0))
    x1 = x3
    x3 = x1 - f(x1) / derivative_f(x1, a, b)

x = (x2 + x3)/2


plt.plot(np.linspace(a, b, 100), [f(i) for i in np.linspace(a, b, 100)],
         [i for i in range(4)], [0 for i in range(4)])

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print("Roots on the interval: ", x)


