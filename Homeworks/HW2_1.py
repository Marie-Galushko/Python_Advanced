# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def to_hex(a):
    if type(a) == int:
        return (str(hex(a))[2:]).upper()


def to_hex2(a):
    if type(a) == int:
        res = ""
        while a != 0:
            word = a % 16
            if word > 9:
                if word == 10:
                    res = 'A' + res
                elif word == 11:
                    res = 'B' + res
                elif word == 12:
                    res = 'C' + res
                elif word == 13:
                    res = 'D' + res
                elif word == 14:
                    res = 'E' + res
                elif word == 15:
                    res = 'F' + res
            else:
                res = str(word) + res
            a //= 16
        return res


def to_hex3(a):
    if type(a) == int:
        res = ""
        alph = {10: 'A', 11: 'B', 12: 'C',
                13: 'D', 14: 'E', 15: 'F'}
        while a != 0:
            word = a % 16
            if word > 9:
                res = alph[word] + res
            else:
                res = str(word) + res
            a //= 16
        return res


a = int(input())
print(to_hex3(a))
