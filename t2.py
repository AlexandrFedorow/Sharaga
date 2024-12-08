import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Задаем параметры
V1 = 1  # Примерное значение V1
V2 = 0  # Примерное значение V2
theta0 = np.pi * 0.2677  # Примерное значение угла theta0
ka = [2.9, 2, 2.8]  # Примерное значение ka
n_max = 5  # Максимальный номер суммы
Dn = [[0.35, 0.34, 0.33, 0.42, 1.02, 3.57],
      [0.55, 0.55, 0.76, 2.23, 9.66, 51.31],
      [0.37, 0.36, 0.36, 0.53, 1.48, 5.57]]  # Примерный массив dn

delta = [[100.32, 32.49, -8.11, -13.16, -3.27, -0.37],
         [51.16, -1.97, -10.4, -1.97, -0.15, -0.01],
         [90.08, 24.23, 11.31, 10.54, 2.02, 0.2]]  # Примерный массив дельта


# Функция F(theta)
def F(theta):
    if 0 <= theta <= theta0 or np.pi - theta0 <= theta <= np.pi:
        return V1 * np.cos(theta)
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

f = ['proto2/5,8кГц_17.23.txt',  # 2 тип
     'proto2/5,8кГц_17.20.txt',  # 4 тип
     'proto2/5,8кГц_17.25.txt',  # 3 тип
     'proto2/5,8кГц_17.46.txt',  # 1 тип
     'proto2/11,8кГц_17.42.txt']  # 5 тип

# Построение графика
file_path = f[4]  # Замените на путь к вашему файлу
angles, values = read_data(file_path)
values = values / max(values)

a = [i-45 for i in angles]
a2 = [i+45 for i in angles]

R_vals = [R(theta, ka[0], 1) for theta in a]


plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.plot(a2, values, label="Экспериментальный график")
#ax.plot(angles, R_vals / max(R_vals), label='Теоретический график')


ax.legend(bbox_to_anchor=(1.2, 1))

ax.set_theta_zero_location("N")
plt.show()


# Укажите путь к вашему файлу




