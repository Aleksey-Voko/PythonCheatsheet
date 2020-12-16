# Cheatsheet [pathlib](https://docs.python.org/3/library/pathlib.html) — Object-oriented filesystem paths

**&nbsp;&nbsp;&nbsp;**
**[`with_suffix`](#Path with_suffix\(suffix\):)**__,__

#### Importing:
```python
from pathlib import Path
```

#### Get path:
```python
Path()                         # current directory
Path('.')                      # current directory
Path.cwd()                     # current directory
Path.home()                    # user’s home directory
Path('setup.py')
Path('foo/some/path')
Path('foo', 'some/path')
Path('foo', Path('bar'))
```

#### Navigating:
```python
<path> / 'init.d'
<path> / 'init.d/reboot'
<path> / 'init.d' / 'reboot'
```

#### Path properties:
```python
<path>.exists()                # Whether this path exists
<path>.is_dir()                # Whether this path is a directory
<path>.is_file()               # Whether this path is a file
```

#### Listing files:
```python
list(<path>.glob('*.py'))      # in directory
list(<path>.glob('**/*.py'))   # in directory tree
list(<path>.rglob('*.py'))     # in directory tree
```

#### Directory contents:
```python
<path>.iterdir()
# Listing subdirectories:
[x for x in <path>.iterdir() if x.is_dir()]
```

#### Create a new directory:
```python
<path>.mkdir(mode=0o777, parents=False, exist_ok=False)
# example:
Path('parent/dir_name').mkdir(parents=True, exist_ok=True)
```

#### Opening a file:
```python
Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
# example
with <path>.open() as f:
    f.readline()
```

#### Rename:

```python
# Rename this file or directory:
<path>.rename(target)            # guaranteed only for unix
<path>.replace(target)           # cross-platform
# examples:
Path('old_name').replace(Path('new_name'))
Path('parent/old_name').replace('parent/new_name'))
```

#### Contents:

```python
# Binary contents:
<path>.read_bytes()
<path>.write_bytes(data)
# Decoded contents as a string:
<path>.read_text(encoding=None, errors=None)
<path>.write_text(data, encoding=None, errors=None)
```

---

#### Path name:
```python
Path('my/library/setup.py').name
# 'setup.py'
```

#### Path parent:
```python
Path('/a/b/c/d').parent
# PurePosixPath('/a/b/c')
```

#### Path parents:
```python
p = Path('c:/foo/bar/setup.py').parents
p.parents[0]
# PureWindowsPath('c:/foo/bar')
p.parents[1]
# PureWindowsPath('c:/foo')
p.parents[2]
# PureWindowsPath('c:/')
```

#### Make the path absolute:
```python
<path>.resolve()
```

#### Remove empty directory:
```python
<path>.rmdir()
```

#### Path suffix:
```python
Path('my/library/setup.py').suffix
# '.py'
Path('my/library.tar.gz').suffix
# '.gz'
Path('my/library').suffix
# ''
```

#### Path suffixes:
```python
Path('my/library.tar.gar').suffixes
# ['.tar', '.gar']
Path('my/library').suffixes
# []
```

#### Path stem:
```python
Path('my/library.tar.gz').stem
# 'library.tar'
Path('my/library.tar').stem
# 'library'
Path('my/library').stem
# 'library'
```

#### Path as_posix():
```python
Path('c:\\windows').as_posix()
# 'c:/windows'
```

#### Path as_uri():
```python
Path('/etc/passwd').as_uri()
# 'file:///etc/passwd'
Path('c:/Windows').as_uri()
# 'file:///c:/Windows'
```

#### Path with_name(name):
```python
Path('c:/Downloads/pathlib.tar.gz').with_name('setup.py')
# Path('c:/Downloads/setup.py')
```

#### Path with_stem(stem)
```python
Path('c:/Downloads/draft.txt').with_stem('final')
# Path('c:/Downloads/final.txt')
Path('c:/Downloads/pathlib.tar.gz').with_stem('lib')
# Path('c:/Downloads/lib.gz')
```

#### Path with_suffix(suffix):
```python
Path('c:/Downloads/pathlib.tar.gz').with_suffix('.bz2')
# Path('c:/Downloads/pathlib.tar.bz2')
Path('README').with_suffix('.txt')
# Path('README.txt')
Path('README.txt').with_suffix('')
# Path('README')
```

---

*class* pathlib.**PurePosixPath**(*pathsegments)
```python
from pathlib import PurePosixPath

PurePosixPath('/etc')
# PurePosixPath('/etc')
```

*class* pathlib.**PureWindowsPath**(*pathsegments)

```python
from pathlib import PureWindowsPath

PureWindowsPath('c:/Program Files/')
# PureWindowsPath('c:/Program Files')
```

---

### Other

```python
# Create a file:
<path>.touch(mode=0o666, exist_ok=True)
```

```python
# Path drive:
Path('c:/Program Files/').drive
# 'c:'
Path('/Program Files/').drive
# ''
Path('//host/share/foo.txt').drive
# '\\\\host\\share'
Path('/etc').drive
# ''
```

```python
# Path parts:
Path('/usr/bin/python3').parts
# ('/', 'usr', 'bin', 'python3')
Path('c:/Program Files/PSF').parts
# ('c:\\', 'Program Files', 'PSF')
```

```python
# Path root:
Path('c:/Program Files/').root
# '\\'
Path('c:Program Files/').root
# ''
Path('/etc').root
# '/'
```

```python
# Does this path point to the same file:
<path>.samefile(other_path)
```
