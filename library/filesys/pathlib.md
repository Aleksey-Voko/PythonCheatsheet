# Cheatsheet [pathlib](https://docs.python.org/3/library/pathlib.html) — Object-oriented filesystem paths

**[`anchor`](#attributes)**__,__
**[`as_posix()`](#methods)**__,__
**[`as_uri()`](#methods)**__,__
**[`chmod()`](#actions)**__,__
**[`cwd()`](#get-path)**__,__
**[`drive`](#attributes)**__,__
**[`exists()`](#properties)**__,__
**[`expanduser()`](#methods)**__,__
**[`glob()`](#directory-contents)**__,__
**[`group()`](#attributes)**__,__
**[`home()`](#get-path)**__,__
**[`is_absolute()`](#properties)**__,__
**[`is_block_device()`](#properties)**__,__
**[`is_char_device()`](#properties)**__,__
**[`is_dir()`](#properties)**__,__
**[`is_fifo()`](#properties)**__,__
**[`is_file()`](#properties)**__,__
**[`is_mount()`](#properties)**__,__
**[`is_relative_to()`](#properties)**__,__
**[`is_reserved()`](#properties)**__,__
**[`is_socket()`](#properties)**__,__
**[`is_symlink()`](#properties)**__,__
**[`iterdir()`](#directory-contents)**__,__
**[`joinpath()`](#navigating)**__,__
**[`lchmod()`](#actions)**__,__
**[`link_to()`](#actions)**__,__
**[`lstat()`](#methods)**__,__
**[`match()`](#properties)**__,__
**[`mkdir()`](#actions)**__,__
**[`name`](#attributes)**__,__
**[`open()`](#opening-a-file)**__,__
**[`owner()`](#attributes)**__,__
**[`parent`](#attributes)**__,__
**[`parents`](#attributes)**__,__
**[`parts`](#attributes)**__,__
**[`Path()`](#get-path)**__,__
**[`PurePosixPath()`](#pureposixpath)**__,__
**[`PureWindowsPath()`](#purewindowspath)**__,__
**[`read_bytes()`](#contents)**__,__
**[`read_text()`](#contents)**__,__
**[`readlink()`](#methods)**__,__
**[`relative_to()`](#methods)**__,__
**[`replace()`](#actions)**__,__
**[`resolve()`](#methods)**__,__
**[`rglob()`](#directory-contents)**__,__
**[`rmdir()`](#actions)**__,__
**[`root`](#attributes)**__,__
**[`samefile()`](#properties)**__,__
**[`stat()`](#methods)**__,__
**[`stem`](#attributes)**__,__
**[`suffix`](#attributes)**__,__
**[`suffixes`](#attributes)**__,__
**[`symlink_to()`](#actions)**__,__
**[`touch()`](#actions)**__,__
**[`unlink()`](#actions)**__,__
**[`with_name()`](#methods)**__,__
**[`with_stem()`](#methods)**__,__
**[`with_suffix()`](#methods)**__,__
**[`write_bytes()`](#contents)**__,__
**[`write_text()`](#contents)**

**[`Recipes`](#recipes)**

#### Importing:
```python
from pathlib import Path
```

#### Get path:
```python
<path> = Path()                              # current directory
<path> = Path('.')                           # current directory
<path> = Path.cwd()                          # current directory
<path> = Path(__file__)                      # running module file
<path> = Path(__file__).parent               # directory of the running module
<path> = Path.home()                         # user’s home directory
<path> = Path('setup.py')                    # <path>('setup.py')
<path> = Path('foo/some/path')               # <path>('foo/some/path')
<path> = Path('foo', 'some/path')            # <path>('foo/some/path')
<path> = Path('foo', Path('some'))           # <path>('foo/some')
```

#### Navigating:
```python
<path> / 'init.d'                            # <path>('<path>/init.d')
<path> / 'init.d/reboot'                     # <path>('<path>/init.d/reboot')
<path> / 'init.d' / 'reboot'                 # <path>('<path>/init.d/reboot')

Path('/etc').joinpath('passwd')              # <path>('/etc/passwd')
Path('/etc').joinpath(Path('passwd'))        # <path>('/etc/passwd')
Path('/etc').joinpath('init.d', 'apache2')   # <path>('/etc/init.d/apache2')
Path('c:').joinpath('/Program Files')        # <path>('c:/Program Files')
```

#### Contents:
```python
<bytes> = <path>.read_bytes()                         # read binary contents
<path>.write_bytes(data)                              # write binary contents
<str> = <path>.read_text(encoding=None, errors=None)  # read string contents
<path>.write_text(data, encoding=None, errors=None)   # write string contents
```

#### Directory contents:
```python
# Listing files:
<iter> = <path>.glob('*.py')                 # in directory
<iter> = <path>.glob('**/*.py')              # in directory tree
<iter> = <path>.rglob('*.py')                # in directory tree
<iter> = <path>.iterdir()                    # files and folders

# Listing subdirectories:
[x for x in <path>.iterdir() if x.is_dir()]
```

#### Opening a file:
```python
Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
# example:
with <path>.open() as f:
    f.readline()
```

#### Actions:
```python
<path>.touch(mode=0o666, exist_ok=True)      # create file
<path>.mkdir(mode=0o777, parents=False,
    exist_ok=False)                          # create directory
<path>.replace(target)                       # rename file or directory
<path>.unlink(missing_ok=False)              # remove file or symbolic link
<path>.rmdir()                               # remove empty directory
<path>.chmod(0o444)                          # change permissions
<path>.lchmod(0o444)                         # change permissions for symbolic link
<path>.link_to(target)                       # create a hard link to the target
<path>.symlink_to(target)                    # make this path a symbolic link to target:
```

#### Attributes:
```python
<str>  = Path('foo/bar/egg.py').name         # 'egg.py'
<path> = Path('foo/bar/egg.py').parent       # <path>('foo/bar')
<iter> = Path('c:/foo/bar/egg.py').parents   # <iter>('c:/foo/bar', 'c:/foo', 'c:/')
<str>  = Path('foo/bar/egg.py').stem         # 'egg'
<str>  = Path('foo/bar/egg.py').suffix       # '.py'
<iter> = Path('foo/egg.tar.gar').suffixes    # ['.tar', '.gar']
<iter> = Path('c:/Program Files/PSF').parts  # ('c:\\', 'Program Files', 'PSF')
<str>  = Path('c:/Program Files/').drive     # 'c:'
<str>  = Path('c:/Program Files/').root      # '\\'
<str>  = Path('c:/Program Files/').anchor    # 'c:\\'
<str>  = <path>.owner()                      # owner username
<str>  = <path>.group()                      # owner group name
```

#### Properties:
```python
<bool> = <path>.exists()                     # whether this path exists
<bool> = <path>.is_dir()                     # whether this path is a directory
<bool> = <path>.is_file()                    # whether this path is a file
<bool> = <path>.is_absolute()                # whether this path is absolute
<bool> = <path>.is_reserved()                # whether this path reserved
<bool> = <path>.is_mount()                   # whether this path is a mount point
<bool> = <path>.is_symlink()                 # whether this path is a symbolic link
<bool> = <path>.is_socket()                  # whether this path is a Unix socket
<bool> = <path>.is_fifo()                    # whether this path is a FIFO
<bool> = <path>.is_block_device()            # whether this path is a block device
<bool> = <path>.is_char_device()             # whether this path is a character device
<bool> = <path>.match('*.py')                # does it match the pattern
<bool> = <path>.is_relative_to(*other)       # whether this path is relative to another path
<bool> = <path>.samefile(other_path)         # does this path point to the same file
```

#### Methods:
```python
<path> = Path('bar/egg.py').resolve()        # get absolute path
<path> = Path('~/f/egg.py').expanduser()     # get absolute path
<str>  = Path('c:\\windows').as_posix()      # 'c:/windows'
<str>  = Path('/etc/passwd').as_uri()        # 'file:///etc/passwd'
<str>  = Path('c:/Windows').as_uri()         # 'file:///c:/Windows'
<path> = Path('f/e.py').with_name('lib.h')   # Path('f/lib.h')
<path> = Path('f/e.py').with_stem('lib')     # Path('f/lib.py')
<path> = Path('f/e.gz').with_suffix('.bz2')  # Path('f/e.bz2')
<path> = Path('/etc/user').relative_to('/')  # Path('etc/user')
<path> = <path>.readlink()                   # path to which the symbolic link points

<stat> = <path>.stat()                       # os.stat_result for path
<stat> = <path>.lstat()                      # os.stat_result for link
<int>  = <path>.stat().st_size               # size of the file in bytes
<int>  = <path>.stat().st_mode               # file type and file mode bits (permissions)
<int>  = <path>.stat().st_ino                # inode number (Unix) or file index (Windows)
<int>  = <path>.stat().st_dev                # identifier of the device on which this file resides
<int>  = <path>.stat().st_nlink              # number of hard links
<int>  = <path>.stat().st_uid                # user identifier of the file owner
<int>  = <path>.stat().st_gid                # group identifier of the file owner
<int>  = <path>.stat().st_atime              # time of most recent access expressed in seconds
<int>  = <path>.stat().st_mtime              # time of most recent content modification expressed in seconds
<int>  = <path>.stat().st_ctime              # time of most recent metadata change (Unix), the time of creation (Windows)
```

---

#### PurePosixPath:
*class* pathlib.**PurePosixPath**(*pathsegments)
```python
from pathlib import PurePosixPath

PurePosixPath('/etc')
# PurePosixPath('/etc')
```

---

#### PureWindowsPath:
*class* pathlib.**PureWindowsPath**(*pathsegments)

```python
from pathlib import PureWindowsPath

PureWindowsPath('c:/Program Files/')
# PureWindowsPath('c:/Program Files')
```

---

#### Recipes:
```python
# create directory:
Path('parent/dir_name').mkdir(parents=True, exist_ok=True)
```

```python
# copy file:
in_file = Path('in_file.txt')
out_file = Path('out_file.txt')
out_file.parent.mkdir(parents=True, exist_ok=True)
out_file.write_bytes(in_file.read_bytes())
```
