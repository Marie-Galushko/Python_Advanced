import json
import csv
import pickle

import os


def calculate_directory_size(directory):
    total_size = 0
    for path, dirs, files in os.walk(directory):
        for f in files:
            fp = os.path.join(path, f)  # Путь до файла
            total_size += os.path.getsize(fp)

    return total_size


def save_results(directory):
    result = []

    for path, dirs, files in os.walk(directory):
        for d in dirs:
            size = calculate_directory_size(os.path.join(path, d))
            result.append({
                'name': d,
                'type': 'directory',
                'size': size,
                'parent_directory': path
            })
        for f in files:
            file_path = os.path.join(path, f)
            size = os.path.getsize(file_path)
            result.append({
                'name': f,
                'type': 'file',
                'size': size,
                'parent_directory': path
            })


    file = open('result.json', 'w')

    json.dump(result, file, indent=4)

    file.close()

    file = open('result.csv', 'w')
    writer = csv.DictWriter(file, fieldnames=['name', 'type', 'size', 'parent_directory'])
    writer.writeheader()
    writer.writerows(result)

    file.close()

    file = open('result.pickle', 'wb')

    pickle.dump(result, file)

    file.close()


save_results('m')
