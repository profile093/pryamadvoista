from scipy.optimize import linprog

# Коєфіцієнти цільової функції для максимізації Z
c = [-30, -40]  # В лінійному програмуванні функція мінімізується, тому змінюємо знаки

# Матриця обмежень
A = [
    [1, 2],
    [1, 0],
    [0, 1],
    [2, 5],
    [5, 2],
    [-1, 0],
    [-1, -1]
]

# Вектор обмежень
b = [4000, 2250, 1750, 10000, 10000, -600, -1500]

# Розв'язок прямої задачі
result = linprog(c, A_ub=A, b_ub=b, method='highs')

x1, x2 = result.x
z = 30 * x1 + 40 * x2  # Значення цільової функції

print("Розв'язок прямої задачі:")
print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")
print(f"Максимальне значення Z = {z:.2f}")
