import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Коєфіцієнти цільової функції для мінімізації W
c_dual = [4000, 2250, 1750, 10000, 10000, 600, 1500]

# Матриця обмежень для двоїстої задачі
A_dual = [
    [1, 1, 0, 2, 5, -1, -1],  # x1 = y1 + y2 + 2y4 + 5y5 - y6 - y7
    [2, 0, 1, 5, 2, 0, -1]  # x2 = y1 + y3 + 5y4 + 2y5 - y7
]

# Вектор обмежень для двоїстої задачі
b_dual = [30, 40]

# Розв'язок двоїстої задачі
result_dual = linprog(c_dual, A_eq=A_dual, b_eq=b_dual, bounds=(0, None), method='highs')

y = result_dual.x

# Вивід результатів двоїстої задачі
print("\nРозв'язок двоїстої задачі:")
print(
    f"y1 = {y[0]:.2f}, y2 = {y[1]:.2f}, y3 = {y[2]:.2f}, y4 = {y[3]:.2f}, y5 = {y[4]:.2f}, y6 = {y[5]:.2f}, y7 = {y[6]:.2f}")
print("Мінімальне значення W:", result_dual.fun)

# Побудова двоїстої задачі на графіку (лише для y1 і y3 як приклад)
plt.figure()
plt.bar(['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7'], y, color='skyblue')
plt.xlabel('Змінні двоїстої задачі')
plt.ylabel('Значення')
plt.title('Результати двоїстої задачі')
plt.grid(True)
plt.show()
