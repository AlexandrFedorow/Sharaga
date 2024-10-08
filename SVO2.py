import matplotlib.pyplot as plt
import numpy as np

# Пример данных

n = 100

x = [0, 6102, 6102, 16984, 16984, 17882]
y = [400, 0, 0, 1000, 1000, 900]

x2 = [0, 3318, 3318, 12094, 12094, 13094]
y2 = [400, 1000, 1000, 0, 0, 100]

py1 = np.linspace(0, 1000, num=n)
px1 = [6102 for i in range(n)]

py2 = np.linspace(0, 1000, num=n)
px2 = [3318 for i in range(n)]

py3 = np.linspace(0, 1000, num=n)
px3 = [12094 for i in range(n)]

py4 = np.linspace(0, 1000, num=n)
px4 = [16984 for i in range(n)]

ax = plt.gca()

plt.plot(x, y, 'b')
plt.plot(x2, y2, 'b')

plt.plot(px1, py1, '--r', 'r')
plt.plot(px2, py2, '--r', 'r')
plt.plot(px3, py3, '--r', 'r')
plt.plot(px4, py4, '--r', 'r')

ax.set_ylim(0, 1000)
ax.set_xlim(0, 18000)

plt.xlabel('Дальность r, м')
plt.ylabel('Глубина h, м')


plt.gca().xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
plt.tick_params(axis='both', which='major', labelsize=10)
plt.gca().invert_yaxis()


# Рисуем график
plt.show()