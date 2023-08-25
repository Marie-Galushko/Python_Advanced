# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится
# нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

a = int(input())

if a >= 10 ** 5 or a < 0:
    print("Недопустимое значение")
else:
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1

    if count == 2:
        print("Число простое")
    else:
        # print("Число составное")