import time
import random
import numpy as np

def print_matrix(Matrix, matrix_name, timetime):
    print(f"матрица {matrix_name} промежуточное время = {round(timetime, 2)} seconds")
    for i in Matrix:  # Делаем перебор строк матрицы
        for j in i:  # Перебираем все элементы в строке
            print("%5d" % j, end=" ")
        print()

t = int(input("Введите количество знаков после запятой: "))

start = time.time()
time_next = time.time()
time_prev = time_next
print("\n-Результат работы программы-\n")


row = random.randint(2, 3)
x = np.random.randint(5, size=(row, row))
r = np.linalg.matrix_rank(x)
row = int(input("Введите размерность матрицы: "))
while (row < 1) or (row > 35):
    row = int(input("Неверно!\nВведите размерность матрицы:"))

x = np.random.randint(1, 10, (row, row))
rank = np.linalg.matrix_rank(x)

num = "{:{align}{width}.{precision}f}"
print(f"Матрица: \n{x}")
print(f"Ранг матрицы: {rank}")

n = 1
n = 1
before_digit, result, accuracy = 0, 0, 1
fact_denominator = 1
fact_denominator, fact_numerator = 1, 1

while abs(accuracy) > (0.1**t):
    before_digit += result
    result += (np.linalg.det(np.dot(x, fact_denominator))) / (np.math.factorial(3 * n))
    fact_numerator = (3 * n - 1) * (3 * n)
    fact_denominator *= (3 * n - 1) * (3 * n)
    result += np.linalg.det(x*fact_numerator) / fact_denominator
    n += 1
    fact_denominator = 3 * np.math.factorial(n)
    accuracy = abs(before_digit-result)
    accuracy = abs(before_digit - result)
    before_digit = 0
    print(f"{n-1} : {num.format(result, align='0', width=8, precision=10)}   {num.format(accuracy, align='0', width=8, precision=10)}")

print(f"\nИтоговая сумма: {result}")
print(f"Кол-во итераций: {n-1}")
