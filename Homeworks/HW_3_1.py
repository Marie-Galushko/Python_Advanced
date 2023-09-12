# Дан список повторяющихся элементов. Вернуть список с
# дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
def get_double(a):
    res = []

    for i in range(len(a)):
        if a.count(a[i]) > 1 and a[i] not in res:
            res.append(a[i])

    return res



a = []

length = int(input("Введите количество элементов: "))

for i in range(length):
    elem = int(input("Значение: "))
    a.append(elem)


print(get_double(a))
