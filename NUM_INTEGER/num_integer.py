import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def simpson_method(f, a, b, n):
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        result += 4 * f(x) if i % 2 != 0 else 2 * f(x)
    return result * h / 3

# Интервал
a = 0
b_max = 2 * np.pi
x_vals = np.linspace(a, b_max, 200)
n = 5000

# Вычисляем интеграл от 0 до x
simpson_integrals = [simpson_method(f, a, x, n) for x in x_vals]

# Аналитическая первообразная: 1 - cos(x)
analytic = 1 - np.cos(x_vals)

# График
plt.figure(figsize=(10, 6))
plt.plot(x_vals, simpson_integrals-analytic, label='Численный интеграл (Симпсон)', color='blue')
#plt.plot(x_vals, analytic, label='Аналитически: 1 - cos(x)', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('∫sin(t) dt')
plt.title('Численное и аналитическое интегрирование sin(x)')
plt.legend()
plt.grid(True)
plt.savefig('/home/monkeyreel/study/2nd-year/вычмат/NUM_INTEGER/plot.png')
