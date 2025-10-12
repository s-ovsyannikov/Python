import os


def walk_dir(path, indent=0):
    """
    Рекурсивно обходит все папки и файлы, начиная с указанного пути.
    """
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        print(" " * indent + entry)  # Выводим с отступом

        if os.path.isdir(full_path):
            walk_dir(full_path, indent + 2)  # Рекурсивный вызов для подпапки


walk_dir(".")
