# Треугольник существует только тогда,
# когда сумма любых двух его сторон больше третьей.
# Дано а, b, с - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других.
# Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника
# с такими сторонами не существует.
# Отдельно сообщить является ли треугольник
# разносторонним, равнобедренным или
# равносторонним.

a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b and b == c and c == a:
        print("Треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")

else:
    print("Треугольник не существует")