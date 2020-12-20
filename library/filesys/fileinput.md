# Cheatsheet [fileinput](https://docs.python.org/3/library/fileinput.html) — Iterate over lines from multiple input streams

#### Importing:
```python
import fileinput
```

#### Basic use:
```python
for line in fileinput.input():
    process(line)
```
or
```python
files_list = [Path('spam.txt'), 'eggs.txt']
with fileinput.input(files=files_list) as f:
    for line in f:
        process(line)
```

#### Properties:
```python
<bool> = <fileinput>.isfirstline()  # whether this line the first in the file
<bool> = <fileinput>.isstdin()      # whether this line the first in the file
```

#### Methods:
```python
<str> = <fileinput>.filename()      # current file
<int> = <fileinput>.fileno()        # current file descriptor
<int> = <fileinput>.lineno()        # current line number
<int> = <fileinput>.filelineno()    # line number in the current file
<fileinput>.nextfile()              # go to next file
<fileinput>.close()                 # close the sequence
```

#### Recipes:
```python
def get_file_lines(file_list, mode='r', encoding='utf-8', errors=None):
    """Get all lines from all files.
    :param file_list: list of files
        example: [Path('spam.txt'), 'eggs.txt']
    :param mode: 'r' (read text) or 'rb' (read bytes)
    :param encoding: input file encoding
        https://docs.python.org/3/library/codecs.html#standard-encodings
    :param errors: from method open()
        https://docs.python.org/3/library/functions.html#open
        ('strict', 'ignore', 'replace', 'surrogateescape',
        'xmlcharrefreplace', 'backslashreplace', 'namereplace')
    :return: all lines from all files
    """
    hook = fileinput.hook_encoded(encoding=encoding, errors=errors)
    with fileinput.input(files=file_list, mode=mode, openhook=hook) as f:
        for ln in f:
            yield ln.rstrip()

# use:
fl = [Path('spam.txt'), 'eggs.txt']
for line in get_file_lines(fl):
    print(line)
```
