def f(x):
    return x**2 + 2*x + 1  # Пример функции: f(x) = x^2 + 2x + 1

# Метод конечных разностей вперёд
def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Метод центральных разностей
def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

# Точка, в которой ищем производную
x0 = 1.0

print("Производная (forward difference) в x =", x0, "->", forward_difference(f, x0))
print("Производная (central difference) в x =", x0, "->", central_difference(f, x0))
