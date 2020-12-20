import fileinput
from pathlib import Path


def get_file_lines(file_list, mode='r', encoding='utf-8', errors=None):
    hook = fileinput.hook_encoded(encoding=encoding, errors=errors)
    with fileinput.input(files=file_list, mode=mode, openhook=hook) as f:
        for ln in f:
            yield ln.rstrip()


if __name__ == '__main__':
    fl = [Path('spam.txt'), 'eggs.txt']
    for line in get_file_lines(fl):
        print(line)
