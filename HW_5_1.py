# Напишите функцию, которая принимает на вход строку
# - абсолютный путь до файла.

def get_info(abs_path):
    path = abs_path.split("/")[-1]
    name, exp = path.split('.')

    return abs_path, name, exp


abs_path = input()

print(get_info(abs_path))