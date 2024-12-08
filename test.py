import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Задаем параметры
V1 = 2  # Примерное значение V1
V2 = -1  # Примерное значение V2
theta0 = np.pi * 0.2677  # Примерное значение угла theta0
ka = [1.2, 2, 2.8]  # Примерное значение ka
n_max = 5  # Максимальный номер суммы
Dn = [[1.08, 1.4, 4.6, 25.8, 186.9, 1668.9],
      [0.55, 0.55, 0.76, 2.23, 9.66, 51.31],
      [0.37, 0.36, 0.36, 0.53, 1.48, 5.57]]  # Примерный массив дельта

delta = [[18.56, 8.11, 1.59, 0.08, 0, 0],
         [51.16, -1.97, -10.4, -1.97, -0.15, -0.01],
         [90.08, 24.23, 11.31, 10.54, 2.02, 0.2]]  # Примерный массив Dn


# Функция F(theta)
def F(theta):
    if 0 <= theta <= theta0 or np.pi - theta0 <= theta <= np.pi:
        return V1 * np.abs(np.cos(theta))
    elif theta0 <= theta <= np.pi - theta0:
        return V2 * np.sin(theta)
    else:
        return 0


# Вычисляем коэффициенты Vn
Vn = []
for n in range(n_max + 1):
    Pn = legendre(n)  # Полином Лежандра степени n
    integrand = lambda theta: F(theta) * Pn(np.cos(theta)) * np.sin(theta)
    Vn_value = (2 * n + 1) / 2 * np.trapz(
        [integrand(theta) for theta in np.linspace(0, np.pi, 500)],
        np.linspace(0, np.pi, 500)
    )
    Vn.append(Vn_value)


# Функция R(theta, ka)
def R(theta, ka, k):
    R_sum = 0
    for n in range(n_max + 1):
        Pn = legendre(n)  # Полином Лежандра степени n
        term = (Vn[n] * Pn(np.cos(theta)) * np.exp(-1j * (delta[k][n] - (n + 1) * np.pi / 2)) / Dn[k][n])
        R_sum += term
    return np.abs(R_sum)


# Строим график
theta_vals = np.linspace(0, 2 * np.pi, 500)

R_vals = [R(theta, ka[0], 0) for theta in theta_vals]

R_vals2 = [R(theta, ka[1], 1) for theta in theta_vals]

R_vals3 = [R(theta, ka[2], 2) for theta in theta_vals]


# График в полярных координатах
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

ax.plot(theta_vals, R_vals / max(R_vals), label=f'ka={ka[0]}')
ax.plot(theta_vals, R_vals2 / max(R_vals2), label=f'ka={ka[1]}')
ax.plot(theta_vals, R_vals3 / max(R_vals3), label=f'ka={ka[2]}')


ax.set_theta_zero_location("N")
ax.legend()
plt.show()
