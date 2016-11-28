OVERVIEW
========

WEEK 1: Basics
--------------

### DAY 1
    * Intro
    * History of Python
    * Implementations of Python
    * Python Basics
    * Types and functions

### DAY 2
    * Data types: Strings, lists, tuples, sets, dicts
    * Slicing
    * decimal, fraction

### DAY 3
    * List/set/dictionary comprehension
    * Lambda functions
    * Functional programming
    * itertools
    * assert

### DAY 4
    * Working with files, I/O, encodings
    * pdb

### DAY 5
    * re
    * os, shutil, glob, pahtlib

<!--------------------------------------------------------------->

WEEK 2: Data processing, networking, OS
---------------------------------------

### DAY 6
    * json, csv, XML, pickle (zip, tar)?
    * base64
    * urllib
    * logger

### DAY 7
    * sys, argparse
    * subprocess

### DAY 8
    * Classes

### DAY 9
    * Exceptions, traceback
    * Packages and modules
    * pip

### DAY 10
    * requests, beautiful soup
    * flask
    * tkinter

<!--------------------------------------------------------------->

WEEK 3: Advanced, large frameworks
----------------------------------

### DAY 11
    * threading
    * multiprocessing
    * django

### DAY 12
    * setup server from scratch

### DAY 13
    * create packages

### DAY 14

### DAY 15
    * Exam


ADVANCED TOPICS
---------------

* generators
* decorators

SHOULD TALK ABOUT
-----------------

* collections
* contextmanager
    * redirect_stdout
    * suppress
* configparser
* datetime
* dis
* textwrap

OTHER EXTERNAL
--------------

* matplotlib
* pandas




Schedule
========

Day 1
-----

### Skipulag námskeiðs

* Tímar
* Námsmat
    * Verkerfni
        * Mooshak verkefni
        * Keppni
        * Stærri verkefni
    * Lokapróf
        * Heimapróf
        * Rafrænt með öll gögn
* Mooshak
    * Hvernig á að skila
    * Explain examples
    * Time limit exceeded
    * Sorted output

### About Python

* Python
    * Interpreted vs compiled
        * Python bytecode
    * Python 2 vs 3
        * Things that are different between Python 2 and 3 are marked with (*Py23*)
    * Open source language (CPython)
        * Developed by the community
        * Python Enhancement Proposals (PEP)
    * Python implementations
        * CPython, Jython, PyPy,...
    * IDEs
        * Idle
        * PyCharm
        * Idle
        * Thonny


### Python basics

* Two "modes" of python
    * REPL
    * Script
* Math operators
    * `+, -, *, %, /, //, **`
    * `==, !=, <, <=, >, >=` (`<>`)
    * `<<, >>, ^. &, |, ~`
    * Integer and floating point division (*Py23*)
    * power
    * Integers are big-integers (*Py23*)
    * Hex and octal integers (*Py23*)
* Floating point numbers
* Complex numbers
* Strings
    * Unicdoe strings (*Py23*)
    * Syntax
    * multilines strings
    * raw strings
    * Concatenation
    * Repetition
* Lists
    * Concatenation
    * Repetition
    * Member access
* Variables
    * Dynamically typed
    * Duck typing
    * type
* *Everything* is an object
    * Variables are objects
    * Numbers are objects
    * Functions are objects
    * Modules are objects
* dir, help
* len
* "Boolean"
    * True/False
        * Synonyms for 0 and 1
    * "Boolean" operators
        * and, or, not
            * Short circuit
        * bool
* print (*Py23*)

### Running python as a script

* Python has two "modes"
    * Interactive mode, or REPL
    * Script mode
    * Also possible to run script and then enter REPL

#### Windows
    * GUI method
        * Double-click on python file
        * A python terminal will open while the script is running and close as soon as it stops
    * Command line method
        * Open cmd/powershell
        * `C:\...> py file.py` or `C:\...> file.py`

#### Linux/MAC OS
    * Run with Python
        * Open a terminal
        * `$ python3 file.py`
    * Shebang method
        * Put the line `#! /usr/bin/env python3` at the top of `file.py`
        * Run `$ chmod +x file.py` or `$ chmod u+x file.py`
        * To run Python script run `$ ./file.py`


### More Python basics

* Control structures
    * Indentaiton
    * If/elif/else
        * Chained comparison
        * pass
    * Loops
        * while/for/else
        * range
        * iter, next
        * enumerate
        * zip
        * break/continue
* None
* Einföld föll
    * def
    * parameters
    * return types
    * docstrings
* Scope
    * Only created by functions!



Day 2
-----

* Breytur
* Functional paradigm
    * Generate new structures rather than modify
* Lists
    * del
    * Slicing
        * del
        * slice assignment
    * List comprehension
    * tuple
* List manipulation
    * reversed
    * sorted
* Dict
    * Basic usage
        * del?
    * What can be a key?
        * hash
    * Dict comprehension
    * Dict from pairs
    * Iteration
* set
    * Basic usage
        * del?
    * Set comprehension
    * Set from collection
    * Iteration
    * frozenset
* Strings
    * split
    * splitlines

Day 3
-----

* Functions parameters
* Parsing
    * int
    * float
* ASCII
    * chr
    * ord


* Function programming
    * all
    * any
    * filter
    * map
    * zip
    * len
    * max
    * min
    * sum
* Generators
* Integer converters
    * bin
    * oct
    * hex
* Data structures
    * bytes
    * complex


globals
locals




* Misc
input
print
has
repr

* File I/O
    * open

eval
exec
getattr
hasattr
id
isinstance
issubclass
object
property
round
setattr
slice
staticmethod
super

