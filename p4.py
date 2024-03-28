import numpy as np

# Определение матрицы коэффициентов и вектора свободных членов
A = np.array([
    [5.6, 2.7, -1.7],
    [3.4, -3.6, -6.7],
    [0.8, 1.3, 3.7]
])

B = np.array([1.9, -2.4, 1.2])



# Преобразование матрицы A с учетом вектора B
AB = np.column_stack((A, B))

# Приведение матрицы A к треугольному виду
n = len(AB)
for i in range(n):
    for j in range(n):
        if i != j:
            ratio = AB[j][i] / AB[i][i]
            AB[j] = AB[j] - ratio * AB[i]
    print(AB)

# Нормировка строк
for i in range(n):
    AB[i] = AB[i] / AB[i][i]

# Вывод решения
print("Решение системы:")
for i in range(n):
    print(f"x{i+1} = {round(AB[i][-1], 6)}")
