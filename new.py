import sys

def __is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    
    return True
        


def __getmaxday(month, year):
    dayinmonth = {
        1: 31,
        2: 29 if __is_leap_year(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    return dayinmonth[month]


def is_correct_date(date):
    d, m, y = date.split('.')
    d = int(d)
    m = int(m)
    y = int(y)
    
    if y < 1 or y > 9999:
        return False
    if m < 1 or m > 12:
        return False
    if d < 1 or d > __getmaxday(m, y):
        return False
    
    return True
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error")
        sys.exit(1)
    
    date = sys.argv[1]
    
    print(is_correct_date(date))
    