import os


files = os.listdir()


def rename_files(desired_name, num_digits, source_extension, target_extension, name_range=None):
    files = os.listdir()
    counter = 1

    if name_range:
        name_range[0] -= 1

    for file in files:
        extension = file.split('.')[-1]
        if extension == source_extension:
            if name_range:
                file_name = file[name_range[0]:name_range[1]] + desired_name
            else:
                file_name = desired_name

            new_name = file_name + str(counter).zfill(num_digits) + '.' \
                        + target_extension
            os.rename(file, new_name)

            counter += 1


rename_files("new", 1, 'txt', 'md', [1, 2])
