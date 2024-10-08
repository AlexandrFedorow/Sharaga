import matplotlib.pyplot as plt
import numpy as np

# Пример данных
x = [0, 6102, 6102, 10882, 10882, 11882]
y = [400, 0, 0, 1000, 1000, 900]

x2 = [0, 3318, 3318, 5266, 5266, 6266]
y2 = [400, 1000, 1000, 0, 0, 100]

ax = plt.gca()

plt.plot(x, y, 'r')
plt.plot(x2, y2, 'b')
ax.set_ylim(0, 1000)
ax.set_xlim(0, 12000)

plt.xlabel('Дальность r, м')
plt.ylabel('Глубина h, м')
plt.grid()

plt.gca().xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
plt.gca().invert_yaxis()


# Рисуем график
plt.show()