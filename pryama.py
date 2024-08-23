import matplotlib.pyplot as plt
import numpy as np

# Визначаємо обмеження
x = np.linspace(0, 3000, 400)

y1 = (4000 - 1 * x) / 2  # x1 + 2x2 ≤ 4000
y2 = 2250 - 0 * x  # x1 ≤ 2250
y3 = 1750 - 0 * x  # x2 ≤ 1750
y4 = (10000 - 2 * x) / 5  # 2x1 + 5x2 ≤ 10000
y5 = (10000 - 5 * x) / 2  # 5x1 + 2x2 ≤ 10000
y6 = 600 - 0 * x  # x1 ≥ 600 (вертикальна лінія)
y7 = 1500 - x  # x1 + x2 ≥ 1500

# Побудова обмежень
plt.plot(x, y1, label=r'$x_1 + 2x_2 \leq 4000$')
plt.plot(x, y2, label=r'$x_1 \leq 2250$')
plt.plot(x, y3, label=r'$x_2 \leq 1750$')
plt.plot(x, y4, label=r'$2x_1 + 5x_2 \leq 10000$')
plt.plot(x, y5, label=r'$5x_1 + 2x_2 \leq 10000$')
plt.axvline(x=600, color='r', linestyle='--', label=r'$x_1 \geq 600$')
plt.plot(x, y7, label=r'$x_1 + x_2 \geq 1500$')

# Область допустимих рішень
plt.fill_between(x, np.minimum.reduce([y1, y2, y3, y4, y5]),
                 where=(600 <= x) & (y7 <= np.minimum.reduce([y1, y2, y3, y4, y5])),
                 color='gray', alpha=0.5)

# Лінії рівня цільової функції
for z in [20000, 30000, 40000, 50000, 60000]:
    plt.plot(x, (z - 30 * x) / 40, '--', color='blue', alpha=0.6, label=f'Z={z / 1000}k')

plt.xlim((0, 3000))
plt.ylim((0, 2000))

plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title('Графічне рішення прямої задачі')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
