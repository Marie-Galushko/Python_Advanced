# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму
# и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.import fractions

def sum_fract(fract1, fract2):
    fract1 = fract1.split('/')
    fract2 = fract2.split('/')
    
    res = ""
    
    if fract1[1] == fract2[1]:
        res = str(int(fract1[0]) + int(fract2[0])) + '/' + fract1[1]
    else:
        a = int(fract1[0]) * int(fract2[1])
        b = int(fract2[0]) * int(fract1[1])
        res = str(a + b) + '/' + str(int(fract1[1]) * int(fract2[1]))
        
    return res


def mult_fract(fract1, fract2):
    fract1 = fract1.split('/')
    fract2 = fract2.split('/')
    
    res = ""
    
    res = str(int(fract1[0]) * int(fract2[0])) + '/' + str(int(fract1[1]) * int(fract2[1]))
    
    return res
    
    


a = input()  # 1/2
b = input()  # 3/5
print(sum_fract(a, b))
print(mult_fract(a, b))
