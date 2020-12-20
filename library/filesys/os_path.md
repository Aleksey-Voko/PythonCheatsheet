# Cheatsheet [os.path](https://docs.python.org/3/library/os.path.html) — Common pathname manipulations

#### Importing:
```python
from os import path
```

#### Properties:
```python
<bool> = path.exists(<path>)                # whether this path exists, False for broken symbolic links
<bool> = path.lexists(<path>)               # whether this path exists, True for broken symbolic links
<bool> = path.isdir(<path>)                 # whether this path is a directory
<bool> = path.isfile(<path>)                # whether this path is a file
<bool> = path.isabs(<path>)                 # whether this path is absolute
<bool> = path.islink(<path>)                # whether this path is a symbolic link
<bool> = path.ismount(<path>)               # whether this path is a mount point

<bool> = path.samefile(<path1>, <path2>)    # whether this path is relative to another path
<bool> = path.sameopenfile(<fp1>, <fp2>)    # whether the file descriptors refer to the same file
<bool> = path.samestat(<st1>, <st2>)        # whether the stat tuples refer to the same file
<bool> = path.supports_unicode_filenames    # can Unicode strings be used as filenames
```

#### Methods:
```python
<str> = path.abspath(<path>)                # absolute path
<str> = path.expanduser('~/f/egg.py')       # absolute path
<str> = path.expandvars('%name%/f/egg.py')  # absolute path
<str> = path.basename('foo/bar/egg.py')     # 'egg.py'
<str> = path.dirname('foo/bar/egg.py')      # 'foo/bar'

<str>  = path.join(<path>, *<paths>)         # connecting path components
<iter> = path.split(<path>)                 # split the pathname path into a pair (head, tail)
<iter> = path.splitdrive(<path>)            # split the pathname path into a pair (drive, tail)
<iter> = path.splitext(<path>)              # split the pathname path into a pair (root, ext)

<int> = path.getsize(<path>)                # size in bytes

<float> = path.getatime(<path>)             # time of last access
<float> = path.getmtime(<path>)             # time of last modification
<float> = path.getctime(<path>)             # time of last modification

<str> = path.normcase(<path>)               # normalize the case of a pathname
<str> = path.normpath(<path>)               # collapsing redundant separators
<str> = path.realpath(<path>)               # canonical path
<str> = path.relpath(<path>, start=os.curdir)  # relative filepath
<str> = path.commonpath(<paths>)            # longest common sub-path
<str> = path.commonprefix(<paths>)          # longest path prefix
```

