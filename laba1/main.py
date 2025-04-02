"""
Решение системы линейных алгебраических уравнений (СЛАУ) методом Гаусса.

Этот модуль выполняет элементарные преобразования над матрицами, приводя их к
треугольному виду, а затем находит решение методом обратного хода.
"""

def input_matrix():
    """
    Вводит матрицу коэффициентов и вектор свободных членов с клавиатуры.
    
    :return: Кортеж (A, B), где A - матрица коэффициентов, B - вектор свободных членов.
    """
    n = int(input("Введите размерность матрицы: "))
    A = []
    B = []
    print("Введите строки матрицы A и соответствующие элементы вектора B:")
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row[:-1])  # Коэффициенты уравнения
        B.append(row[-1])   # Свободный член
    return A, B

def swap_rows(A: list, B: list, row1: int, row2: int):
    """
    Перестановка двух строк в матрице A и векторе B.
    
    :param A: Матрица коэффициентов.
    :param B: Вектор свободных членов.
    :param row1: Индекс первой строки.
    :param row2: Индекс второй строки.
    """
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]

def add_rows(A: list, B: list, row: int, source_row: int, weight: float):
    """
    Прибавляет к строке row строку source_row, умноженную на коэффициент weight.
    
    :param A: Матрица коэффициентов.
    :param B: Вектор свободных членов.
    :param row: Индекс строки, к которой прибавляется другая строка.
    :param source_row: Индекс строки, которая прибавляется.
    :param weight: Множитель для строки source_row.
    """
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight

def divide_rows(A: list, B: list, row: int, divider: float):
    """
    Делит строку row на число divider для приведения ведущего элемента к 1.
    
    :param A: Матрица коэффициентов.
    :param B: Вектор свободных членов.
    :param row: Индекс строки.
    :param divider: Делитель (ведущий элемент строки).
    """
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider

def show_matrix(A: list, B: list):
    """
    Выводит матрицу коэффициентов A и вектор свободных членов B в консоль.
    
    :param A: Матрица коэффициентов.
    :param B: Вектор свободных членов.
    """
    for row in range(len(A)):
        print(A[row], B[row])

def gauss_solve(A, B):
    """
    Решает систему уравнений методом Гаусса.
    
    :param A: Матрица коэффициентов (квадратная, невырожденная).
    :param B: Вектор свободных членов.
    :return: Список значений переменных X или None, если система несовместна.
    """
    column = 0
    while column < len(B):
        # Находим строку с максимальным по модулю элементом в текущем столбце
        current_row = None
        for row in range(column, len(A)):
            if current_row is None or abs(A[row][column]) > abs(A[current_row][column]):
                current_row = row
        if current_row is None:
            print('Решений нет!')
            return None
        
        # Меняем местами строки, если найденная строка отличается от текущей
        if current_row != column:
            swap_rows(A, B, current_row, column)
        
        # Нормализуем строку: делим на ведущий элемент, чтобы он стал равен 1
        divide_rows(A, B, column, A[column][column])
        
        # Обнуляем элементы ниже ведущего
        for row in range(column + 1, len(A)):
            add_rows(A, B, row, column, -A[row][column])
        
        column += 1
    
    # Обратный ход метода Гаусса: находим неизвестные
    X = [0 for _ in B]
    for i in range(len(B) - 1, -1, -1):
        # Вычисляем X[i], используя уже найденные X[i+1], X[i+2] и т. д.
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    return X

def show_answer(X):
    """
    Выводит найденное решение системы уравнений.
    
    :param X: Список значений переменных.
    """
    for i, x in enumerate(X):
        print(f'X{i} = {x}')

# Основная программа
A, B = input_matrix()
show_matrix(A, B)
solution = gauss_solve(A, B)
if solution:
    show_answer(solution)
