"""
Решение системы линейных алгебраических уравнений (СЛАУ) методом Гаусса.

Этот модуль реализует пошаговый алгоритм метода Гаусса:
1. Прямой ход -- преобразование матрицы коэффициентов к верхнетреугольному виду.
2. Обратный ход -- последовательное вычисление переменных из полученной формы.
"""

def input_matrix():
    """
    Вводит матрицу коэффициентов и вектор свободных членов с клавиатуры.
    
    Возвращает:
        Кортеж (A, B), где A -- матрица коэффициентов, B -- вектор свободных членов.
    """
    n = int(input("Введите размерность матрицы: "))
    A = []
    B = []
    print("Введите строки матрицы A и соответствующие элементы вектора B:")
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row[:-1])  # Коэффициенты уравнения (n штук)
        B.append(row[-1])   # Свободный член (последний элемент строки)
    return A, B


def swap_rows(A: list, B: list, row1: int, row2: int):
    """
    Переставляет две строки в матрице A и векторе B.

    Параметры:
        A -- матрица коэффициентов.
        B -- вектор свободных членов.
        row1 -- индекс первой строки.
        row2 -- индекс второй строки.
    """
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


def add_rows(A: list, B: list, row: int, source_row: int, weight: float):
    """
    Прибавляет к строке `row` строку `source_row`, умноженную на `weight`.

    Используется для зануления элементов под ведущим в текущем столбце.

    Параметры:
        A -- матрица коэффициентов.
        B -- вектор свободных членов.
        row -- индекс строки, которую изменяем.
        source_row -- индекс строки, которую прибавляем.
        weight -- множитель строки source_row.
    """
    A[row] = [a + weight * k for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight


def divide_rows(A: list, B: list, row: int, divider: float):
    """
    Делит строку `row` на `divider`, чтобы ведущий элемент стал равен 1.

    Параметры:
        A -- матрица коэффициентов.
        B -- вектор свободных членов.
        row -- индекс строки.
        divider -- число, на которое делим (ведущий элемент).
    """
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


def show_matrix(A: list, B: list):
    """
    Выводит расширенную матрицу системы (A | B) на экран.

    Параметры:
        A -- матрица коэффициентов.
        B -- вектор свободных членов.
    """
    print("\nТекущая матрица:")
    for row in range(len(A)):
        print(A[row], "|", B[row])
    print()


def gauss_solve(A: list, B: list):
    """
    Решает систему линейных уравнений методом Гаусса.

    Прямой ход:
        - Приводит матрицу к верхнетреугольному виду с единицами на диагонали.
    Обратный ход:
        - Последовательно вычисляет значения переменных снизу вверх.

    Параметры:
        A -- квадратная матрица коэффициентов.
        B -- вектор свободных членов.

    Возвращает:
        Список решений X или None, если система несовместна.
    """
    n = len(B)
    column = 0
    while column < n:
        # Поиск строки с максимальным по модулю элементом
        current_row = None
        for row in range(column, n):
            if current_row is None or abs(A[row][column]) > abs(A[current_row][column]):
                current_row = row
        if current_row is None or abs(A[current_row][column]) < 1e-12:
            print("Система несовместна или имеет бесконечно много решений.")
            return None
        
        # Перестановка строк
        if current_row != column:
            swap_rows(A, B, current_row, column)

        # Нормализация строки (ведущий элемент = 1)
        divide_rows(A, B, column, A[column][column])

        # Обнуление нижних элементов в текущем столбце
        for row in range(column + 1, n):
            add_rows(A, B, row, column, -A[row][column])

        column += 1

    # Обратный ход
    X = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        X[i] = B[i] - sum(A[i][j] * X[j] for j in range(i + 1, n))
    return X


def show_answer(X):
    """
    Выводит решение системы уравнений на экран.

    Параметры:
        X -- список значений переменных.
    """
    print("Решение системы:")
    for i, x in enumerate(X):
        print(f"X{i} = {x}")


# Основной блок запуска
if __name__ == "__main__":
    A, B = input_matrix()
    show_matrix(A, B)
    solution = gauss_solve(A, B)
    if solution:
        show_answer(solution)
