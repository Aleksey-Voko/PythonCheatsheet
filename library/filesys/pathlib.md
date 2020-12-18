# Cheatsheet [pathlib](https://docs.python.org/3/library/pathlib.html) — Object-oriented filesystem paths

**[`as_posix()`](#path-as_posix)**__,__
**[`as_uri()`](#path-as_uri)**__,__
**[`cwd()`](#get-path)**__,__
**[`drive`](#other)**__,__
**[`exists()`](#path-properties)**__,__
**[`glob()`](#listing-files)**__,__
**[`home()`](#get-path)**__,__
**[`is_dir()`](#path-properties)**__,__
**[`is_file()`](#path-properties)**__,__
**[`is_absolute()`](#path-properties)**__,__
**[`is_relative_to()`](#path-properties)**__,__
**[`is_reserved()`](#path-properties)**__,__
**[`iterdir()`](#directory-contents)**__,__
**[`mkdir()`](#create-a-new-directory)**__,__
**[`name`](#path-name)**__,__
**[`open()`](#opening-a-file)**__,__
**[`parent`](#path-parent)**__,__
**[`parents`](#path-parents)**__,__
**[`parts`](#other)**__,__
**[`Path()`](#get-path)**__,__
**[`PurePosixPath()`](#pureposixpath)**__,__
**[`PureWindowsPath()`](#purewindowspath)**__,__
**[`read_bytes()`](#contents)**__,__
**[`read_text()`](#contents)**__,__
**[`rename()`](#rename)**__,__
**[`replace()`](#rename)**__,__
**[`resolve()`](#make-the-path-absolute)**__,__
**[`rmdir()`](#remove-empty-directory)**__,__
**[`root`](#other)**__,__
**[`samefile()`](#other)**__,__
**[`stem`](#path-stem)**__,__
**[`suffix`](#path-suffix)**__,__
**[`suffixes`](#path-suffixes)**__,__
**[`touch()`](#other)**__,__
**[`with_name()`](#path-with_namename)**__,__
**[`with_stem()`](#path-with_stemstem)**__,__
**[`with_suffix`](#path-with_suffixsuffix)**__,__
**[`write_bytes()`](#contents)**__,__
**[`write_text()`](#contents)**

#### Importing:
```python
from pathlib import Path
```

#### Get path:
```python
<path> = Path()                              # current directory
<path> = Path('.')                           # current directory
<path> = Path.cwd()                          # current directory
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

#### Directory contents:
```python
# Listing files:
<iter> = <path>.glob('*.py')                 # in directory
<iter> = <path>.glob('**/*.py')              # in directory tree
<iter> = <path>.rglob('*.py')                # in directory tree

<iter> = <path>.iterdir()                    # Files and folders

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

#### Create and remove:
```python
<path>.touch(mode=0o666, exist_ok=True)      # create file
<path>.unlink(missing_ok=False)              # remove file or symbolic link

# create directory
<path>.mkdir(mode=0o777, parents=False, exist_ok=False)
# example:
Path('parent/dir_name').mkdir(parents=True, exist_ok=True)

# remove empty directory
<path>.rmdir()
```

#### Contents:
```python
<bytes> = <path>.read_bytes()                         # read binary contents
<path>.write_bytes(data)                              # write binary contents
<str> = <path>.read_text(encoding=None, errors=None)  # read string contents
<path>.write_text(data, encoding=None, errors=None)   # write string contents
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
```

#### Properties:
```python
<bool> = <path>.exists()                     # Whether this path exists
<bool> = <path>.is_dir()                     # Whether this path is a directory
<bool> = <path>.is_file()                    # Whether this path is a file
<bool> = <path>.is_absolute()                # Whether this path is absolute
<bool> = <path>.is_reserved()                # Whether this path reserved
<bool> = <path>.is_mount()                   # Whether this path is a mount point
<bool> = <path>.is_symlink()                 # Whether this path is a symbolic link
<bool> = <path>.is_socket()                  # Whether this path is a Unix socket
<bool> = <path>.is_fifo()                    # Whether this path is a FIFO
<bool> = <path>.is_block_device()            # Whether this path is a block device
<bool> = <path>.is_char_device()             # Whether this path is a character device
```

#### Methods:
```python
<stat> = <path>.stat()                          # Return a os.stat_result object
<stat> = <path>.lstat()                         # symbolic link

<path> = Path('bar/egg.py').resolve()           # <path>('/home/u_name/foo/bar/egg.py')
<path> = Path('~/foo/egg.py').expanduser()      # <path>('/home/u_name/foo/egg.py')
<str>  = Path('c:\\windows').as_posix()         # 'c:/windows'
<str>  = Path('/etc/passwd').as_uri()           # 'file:///etc/passwd'
<str>  = Path('c:/Windows').as_uri()            # 'file:///c:/Windows'
<path> = Path('foo/egg.py').with_name('lib.py') # Path('foo/lib.py')
<path> = Path('foo/egg.py').with_stem('lib')    # Path('foo/lib.py')
<path> = Path('foo/egg.gz').with_suffix('.bz2') # Path('foo/egg.bz2')

<path> = Path('/etc/passwd').relative_to('/')   # Path('etc/passwd')g

<str>  = <path>.group()                         # owner group name
<str>  = <path>.owner()                         # owner username

<path> = <path>.readlink()                      # path to which the symbolic link points

<path>.samefile(other_path)  # Does this path point to the same file:

< path > ('a/b.py').match('*.py')  # If pattern is relative
< path > ('/a.py').match('/*.py')  # If pattern is absolute

<bool> = <path>.is_relative_to(*other)   # Whether this path is relative to another path
```

#### Actions:
```python
<path>.replace(target)           # rename file

# Change the file mode and permissions:
< path >.chmod(0o444)
< path >.lchmod(0o444)  # symbolic link

# Make this path a symbolic link to target:
< path >.symlink_to(target, target_is_directory=False)
# example:
Path('mylink').symlink_to('setup.py').resolve()
# PosixPath('/home/antoine/pathlib/setup.py')

# Create a hard link pointing to a path named target:
< path >.link_to(target)
```

#### PurePosixPath
*class* pathlib.**PurePosixPath**(*pathsegments)
```python
from pathlib import PurePosixPath

PurePosixPath('/etc')
# PurePosixPath('/etc')
```

#### PureWindowsPath
*class* pathlib.**PureWindowsPath**(*pathsegments)

```python
from pathlib import PureWindowsPath

PureWindowsPath('c:/Program Files/')
# PureWindowsPath('c:/Program Files')
```
