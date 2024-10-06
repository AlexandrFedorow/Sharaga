import matplotlib.pyplot as plt
import numpy as np

# Пример данных
x = [1480, 1455]
y = [0,1000]

x2 = 1455
y2 = 1000

ax = plt.gca()
plt.plot(x, y)
ax.set_ylim(0, 1000)

plt.xlabel('Скорость звука c, м/с')
plt.ylabel('Глубина h, м')
plt.grid()

plt.gca().xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
plt.gca().invert_yaxis()


# Рисуем график
plt.show()