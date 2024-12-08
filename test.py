import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Задаем параметры
V1 = -2  # Примерное значение V1
V2 = 1  # Примерное значение V2
theta0 = np.pi * 0.2677  # Примерное значение угла theta0
ka = [1.4, 2, 2.8]  # Примерное значение ka
n_max = 5  # Максимальный номер суммы
Dn = [[0.88, 1.02, 2.58, 12.22, 75.74, 578.29],
      [0.55, 0.55, 0.76, 2.23, 9.66, 51.31],
      [0.37, 0.36, 0.36, 0.53, 1.48, 5.57]]  # Примерный массив dn

delta = [[25.75, 8.97, 3.07, 0.22, -0.01, 0],
         [51.16, -1.97, -10.4, -1.97, -0.15, -0.01],
         [90.08, 24.23, 11.31, 10.54, 2.02, 0.2]]  # Примерный массив дельта


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


# Функция для чтения данных из файла
def read_data(file_path):
    angles = []
    values = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Проверка на пустые строки
                angle, value = line.replace(',', '.').split()  # Заменяем запятую на точку
                angles.append(np.radians(float(angle)))  # Преобразование угла в радианы
                values.append(float(value))
    return np.array(angles), np.array(values)


# Построение графика
file_path = "proto/5,8кГц_17.20.txt"  # Замените на путь к вашему файлу
angles, values = read_data(file_path)
values = values / max(values)


R_vals = [R(theta, ka[0], 1) for theta in angles]


plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.plot(angles, values, label="Эксперементальные данные")
ax.plot(angles, R_vals / max(R_vals), label='Теоретические даные')


ax.legend(loc="upper right")

ax.set_theta_zero_location("N")
plt.show()


# Укажите путь к вашему файлу




