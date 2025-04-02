import numpy as np
import matplotlib.pyplot as plt

def plot_parametric(x_func, y_func, t_min, t_max, num_points=500, title="Параметрический график"):
    """
    Строит параметрический график для заданных функций x(t) и y(t).
    
    :param x_func: Функция x(t)
    :param y_func: Функция y(t)
    :param t_min: Минимальное значение параметра t
    :param t_max: Максимальное значение параметра t
    :param num_points: Количество точек
    :param title: Заголовок графика
    """
    t = np.linspace(t_min, t_max, num_points)
    x = x_func(t)
    y = y_func(t)

    plt.plot(x, y, label=title)
    plt.axis("equal")
    plt.legend()
    plt.grid()
    plt.savefig("/home/monkeyreel/study/2nd-year/вычмат/PARAMETRIC/plot.png")  # Сохранение изображения


# Примеры использования:

# 1. Окружность
plot_parametric(lambda t: np.cos(t), lambda t: np.sin(t), 0, 2 * np.pi, title="Окружность")

# 2. Лемниската Бернулли
plot_parametric(lambda t: np.cos(t) / (1 + np.sin(t)**2),
                lambda t: (np.cos(t) * np.sin(t)) / (1 + np.sin(t)**2),
                0, 2 * np.pi, title="Лемниската Бернулли")

# 3. Спираль Архимеда
plot_parametric(lambda t: 0.1 * t * np.cos(t),
                lambda t: 0.1 * t * np.sin(t),
                0, 10 * np.pi, title="Спираль Архимеда")
