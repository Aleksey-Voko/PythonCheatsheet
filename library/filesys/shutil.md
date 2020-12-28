# Cheatsheet [shutil](https://docs.python.org/3/library/shutil.html) — High-level file operations

#### Importing:
```python
import shutil
```

## Directory and files operations

#### Actions:
```python
<path> = copy(src, dst, *, follow_symlinks=True)  # copies the file src to the file or directory dst
<path> = copy2(src, dst, *, follow_symlinks=True)  # copies the file and metadata src to the file or directory dst
<path> = copyfile(src, dst, *, follow_symlinks=True)  # copy the contents
<path> = move(src, dst, copy_function=copy2)  # recursively move a file or directory

copyfileobj(fsrc, fdst, length=0)  # copy the contents
copymode(src, dst, *, follow_symlinks=True)  # copy the permission bits
copystat(src, dst, *, follow_symlinks=True)  # copy the permission bits, last access time, last modification time, and flags

<path> = copytree(src, dst, symlinks=False,
	ignore=None, copy_function=copy2,
    ignore_dangling_symlinks=False,
    dirs_exist_ok=False)  # Recursively copy an directory tree rooted at src to a directory named dst
<func> = ignore_patterns(*patterns)  # creates a function for copytree()’s ignore argument

rmtree(path, ignore_errors=False, onerror=None)  # delete directory tree

chown(path, user=None, group=None)  # Change owner user and/or group
```

#### Methods:
```python
<n_tuple> = disk_usage(path)  # disk usage statistics as a named tuple

<str> = which(cmd, mode=os.F_OK | os.X_OK, path=None)  # the path to an executable for cmd
# example:
p = which('python')
```
