# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут в рюкзак
# передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый
# вариант.
# *Верните все возможные варианты комплектации рюкзака.

bag = {
    'cup': 0.2,
    'bed': 2,
    'tent': 1,
    'food': 0.5,
    'snack': 0.1,
}

beg_res = dict()


max_weight = float(input())


summary = 0

for key, value in bag.items():
    if summary + value <= max_weight:
        summary += value
        beg_res[key] = value
