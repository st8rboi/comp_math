def f(x, y):
    return x + y  # Правая часть уравнения dy/dx = x + y

def euler_method(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]
    for i in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        xs.append(x0)
        ys.append(y0)
    return xs, ys

# Начальные условия
x0 = 0
y0 = 1
h = 0.1
n = 10


xs, ys = euler_method(f, x0, y0, h, n)

for i in range(len(xs)):
    print(f"x = {xs[i]:.2f}, y = {ys[i]:.4f}")
