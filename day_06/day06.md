---
title: Forritunarmálið Python
subtitle: Day 6 \newline The File System
author: Hjalti Magnússon
date: 4.\ desember 2017
---

# The File System

## Paths

* The file system is a tree
* To locate files and directories in the tree, we use paths
* Paths come in two different flavors
* Absolute path
    * Path to a file/directory from the root of the tree
    * Path to a file/directory relative to the *current working directory*
* **There is always a current directory**


## Absolute paths

### Unix (Linux, Mac OS)

* `/home/nonni/pr0n`
* `/home/nonni/favorite_movies.txt`

### Windows

* `C:\Users\nonni\pr0n`
* `C:\Users\nonni\favorite_movies.txt`
* `D:\some\other\path`

## Relative paths

* Any program that is run has a *current working directory*
* Relative paths locate files/directories relative to the CWD

* Current directory: `.`
* Parent directory: `..`


### Unix (Linux, Mac OS)

* `./favorite_movies.txt`
* `favorite_movies.txt` - same as above
* `../favorite_movies.txt`
* `../nonni/favorite_movies.txt`


## Relative paths

### Windows

* `.\favorite_movies.txt`
* `favorite_movies.txt` - same as above
* `..\favorite_movies.txt`
* `..\nonni\favorite_movies.txt`

# Python and the file system

## `os` - Working with the file system

* Current working directory
    * `chdir`, `getcwd`
* Creating directories
    * `mkdir`, `makedirs`
* Removing files and directories
    * `remove`, `removedirs`, `rmdir`
* Contents of directories
    * `listdir`, `scandir`
* Traverse file system
    * `walk`

## `os.path` - Path manipulation

* Convert relative paths to absolute paths
    * `abspath`
* Parts of the path
    * `basename, dirname, split`
* Properties
    * `exists, isfile, isdir`
* Joining paths
    * `join`
* Normalize paths
    * `normpath`

## `pathlib` - Object oriented paths

* `abspath` $\to$ `resolve`
* `basename`, `dirname`, `split` $\to$ `parts`, `parent`, `name`
* `exists`, `isfile`, `isdir` $\to$ `exists`, `is_file`, `is_dir`
* `join` $\to$ `/` or `joinpath`
* `normpath` $\to$ `resolve`


## `pathlib` - Object oriented paths

* `getcwd` $\to$ `cwd`
* `mkdir`, `makedirs` $\to$ `mkdir`
* `remove`, `removedirs`, `rmdir` $\to$ `rmdir`, `unlink`
* `listdir`, `scandir` $\to$ `iterdir`
* `walk` $\to$ `glob`


## `shutil`

* Copy files
    * `copy`, `copy2`
* Copy directories
    * `copytree`
* Remove directories and contents
    * `rmtree`
* Move (rename)
    * `move`

