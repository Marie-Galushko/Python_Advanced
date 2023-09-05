# Напишите функцию для транспонирования матрицы

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

a = []

for i in range(n):
    array = []
    for j in range(m):
        array.append(int(input()))
    a.append(array)

res = []

for i in zip(*a):
    res.append(list(i))

print(res)