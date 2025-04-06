def f(x):
    return x**2  # Пример функции: f(x) = x^2

# Метод прямоугольников (левых)
def rectangle_method(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
        result += f(a + i * h)
    return result * h

# Метод трапеций
def trapezoidal_method(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

# Пределы интегрирования и количество разбиений
a = 0
b = 1
n = 1000

print("Интеграл (метод прямоугольников):", rectangle_method(f, a, b, n))
print("Интеграл (метод трапеций):", trapezoidal_method(f, a, b, n))
