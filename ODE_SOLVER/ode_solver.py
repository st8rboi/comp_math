import numpy as np
import matplotlib.pyplot as plt

# Настройки отображения графиков
plt.rcParams.update({
    'figure.figsize': (14, 9),
    'font.size': 11
})

# --- Численные методы решения ОДУ ---

def euler(f, x0, y0, h, steps):
    """Метод Эйлера первого порядка"""
    x_vals, y_vals = [x0], [y0]
    for _ in range(steps):
        y_next = y_vals[-1] + h * f(x_vals[-1], y_vals[-1])
        x_vals.append(x_vals[-1] + h)
        y_vals.append(y_next)
    return np.array(x_vals), np.array(y_vals)

def rk2(f, x0, y0, h, steps):
    """Метод Рунге-Кутты второго порядка (Модифицированный Эйлер)"""
    x_vals, y_vals = [x0], [y0]
    for _ in range(steps):
        k1 = h * f(x_vals[-1], y_vals[-1])
        k2 = h * f(x_vals[-1] + h, y_vals[-1] + k1)
        y_next = y_vals[-1] + 0.5 * (k1 + k2)
        x_vals.append(x_vals[-1] + h)
        y_vals.append(y_next)
    return np.array(x_vals), np.array(y_vals)

def rk3(f, x0, y0, h, steps):
    """Метод Рунге-Кутты третьего порядка"""
    x_vals, y_vals = [x0], [y0]
    for _ in range(steps):
        k1 = h * f(x_vals[-1], y_vals[-1])
        k2 = h * f(x_vals[-1] + h / 2, y_vals[-1] + k1 / 2)
        k3 = h * f(x_vals[-1] + h, y_vals[-1] - k1 + 2 * k2)
        y_next = y_vals[-1] + (k1 + 4 * k2 + k3) / 6
        x_vals.append(x_vals[-1] + h)
        y_vals.append(y_next)
    return np.array(x_vals), np.array(y_vals)

def rk4(f, x0, y0, h, steps):
    """Метод Рунге-Кутты четвёртого порядка"""
    x_vals, y_vals = [x0], [y0]
    for _ in range(steps):
        k1 = h * f(x_vals[-1], y_vals[-1])
        k2 = h * f(x_vals[-1] + h / 2, y_vals[-1] + k1 / 2)
        k3 = h * f(x_vals[-1] + h / 2, y_vals[-1] + k2 / 2)
        k4 = h * f(x_vals[-1] + h, y_vals[-1] + k3)
        y_next = y_vals[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x_vals.append(x_vals[-1] + h)
        y_vals.append(y_next)
    return np.array(x_vals), np.array(y_vals)

# Правая часть уравнения y' = x^2
def diff_eq(x, y):
    return x**2

# Начальные условия
start_x, start_y = 0.0, 1.0
h = 0.02
num_steps = 50

# Вычисляем численные решения
x1, y_euler = euler(diff_eq, start_x, start_y, h, num_steps)
x2, y_rk2 = rk2(diff_eq, start_x, start_y, h, num_steps)
x3, y_rk3 = rk3(diff_eq, start_x, start_y, h, num_steps)
x4, y_rk4 = rk4(diff_eq, start_x, start_y, h, num_steps)

# --- Визуализация результатов ---

plt.figure()

# 1. Все методы на одном графике
plt.subplot(2, 3, 1)
plt.plot(x1, y_euler, 'tab:blue', label='Эйлер', linestyle='--')
plt.plot(x2, y_rk2, 'tab:red', label='РК 2', linestyle='-.')
plt.plot(x3, y_rk3, 'tab:green', label='РК 3', linestyle=':')
plt.plot(x4, y_rk4, 'tab:purple', label='РК 4', linewidth=2)
plt.title('Численные методы решения ОДУ: y\' = x²')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# 2. РК4 - Эйлер
plt.subplot(2, 3, 2)
plt.plot(x1, y_rk4 - y_euler, 'darkred')
plt.title('Разность: РК4 - Эйлер')
plt.xlabel('x')
plt.ylabel('Δy')
plt.grid(True)

# 3. РК2 - Эйлер
plt.subplot(2, 3, 3)
plt.plot(x1, y_rk2 - y_euler, 'navy')
plt.title('Разность: РК2 - Эйлер')
plt.xlabel('x')
plt.ylabel('Δy')
plt.grid(True)

# 4. РК3 - Эйлер
plt.subplot(2, 3, 4)
plt.plot(x1, y_rk3 - y_euler, 'seagreen')
plt.title('Разность: РК3 - Эйлер')
plt.xlabel('x')
plt.ylabel('Δy')
plt.grid(True)

# 5. Относительные ошибки
plt.subplot(2, 3, 5)
for y_approx, color, label in [(y_rk2, 'blue', 'РК2'), (y_rk3, 'green', 'РК3'), (y_rk4, 'purple', 'РК4')]:
    safe_y = np.where(y_approx == 0, 1e-12, y_approx)
    relative_diff = (y_approx - y_euler) / safe_y
    plt.plot(x1, relative_diff, label=f'{label} / Эйлер', color=color)
plt.title('Относительные отклонения от метода Эйлера')
plt.xlabel('x')
plt.ylabel('Отн. ошибка')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# 6. Только метод Эйлера
plt.figure(figsize=(9, 5))
plt.plot(x1, y_euler, 'orangered', linewidth=2)
plt.title("Приближенное решение (метод Эйлера)")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
