# Cheatsheet [shutil](https://docs.python.org/3/library/shutil.html) — High-level file operations

**[`copy()`](#copying-files)**__,__
**[`copy2()`](#copying-files)**__,__
**[`copyfile()`](#copying-files)**__,__
**[`copyfileobj()`](#copying-files)**__,__
**[`copymode()`](#copying-file-metadata)**__,__
**[`copystat()`](#copying-file-metadata)**__,__
**[`copytree()`](#working-with-directory-trees)**__,__
**[`disk_usage()`](#file-system-space)**__,__
**[`get_archive_formats()`](#archives)**__,__
**[`get_unpack_formats()`](#archives)**__,__
**[`make_archive()`](#archives)**__,__
**[`move()`](#working-with-directory-trees)**__,__
**[`rmtree()`](#working-with-directory-trees)**__,__
**[`unpack_archive()`](#archives)**__,__
**[`which()`](#finding-files)**

#### Importing:
```python
import shutil
```

#### Copying Files:
```python
<str> = copyfile(src, dst, *, follow_symlinks=True)  # copy file
<str> = copy(src, dst, *, follow_symlinks=True)      # copy file to file or directory
<str> = copy2(src, dst, *, follow_symlinks=True)     # copy file and metadata to file or directory
copyfileobj(fsrc, fdst, length=0)                    # copy file (file handles)
```

#### Copying File Metadata:
```python
copymode(src, dst, *, follow_symlinks=True)  # copy permission bits
copystat(src, dst, *, follow_symlinks=True)  # copy permission bits and stat
```

#### Working With Directory Trees:
```python
copytree(src, dst, symlinks=False,               # recursively copy tree
         ignore=None, copy_function=copy2,
         ignore_dangling_symlinks=False,
         dirs_exist_ok=False)

rmtree(path, ignore_errors=False, onerror=None)  # delete directory tree
move(src, dst, copy_function=copy2)              # recursively move tree
```

#### Finding Files:
```python
# path to an executable for cmd
<str> = which(cmd, mode=os.F_OK | os.X_OK, path=None)
# example:
p = which('python')
```

#### Archives:
```python
<list> = shutil.get_archive_formats()     # all supported formats for archiving
<list> = shutil.get_unpack_formats()      # all registered formats for unpacking

<str> = make_archive(base_name, format,   # create an archive file
                     root_dir, base_dir,
                     verbose, dry_run,
                     owner, group,
                     logger)

unpack_archive(filename, extract_dir, format)  # unpack an archive
```

#### File System Space:
```python
<n_tuple> = disk_usage(path)  # disk usage statistics as a named tuple
```
