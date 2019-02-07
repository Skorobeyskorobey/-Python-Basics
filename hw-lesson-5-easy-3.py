if __name__ == '__main__':
    import os
    import re
    import shutil
def current_file_copy():
    name_file = os.path.realpath(__file__)
    new_file = name_file + '.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'
if __name__ == '__main__':
    print(current_file_copy())
