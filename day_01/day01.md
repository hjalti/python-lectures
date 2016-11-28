Forritunarmálið Python
======================

Dagur 1
-------

---


### Course schedule

* Classes
* Evaluation
    * Assignments
        * Mooshak assignments
        * Competition
        * Larger assignments
    * Final
        * Home exam, auto-graded and open book
* Mooshak
    * Examples
    * Time limit exceeded
    * Sorted output
* Book

---

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
        * Idle, PyCharm, Idle, honny

---

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

---

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

---

* Variables
    * Dynamically typed
    * Duck typing
    * type
* *Everything* is an object
    * Variables are objects
    * Numbers are objects
    * Functions are objects
    * Modules are objects
    * `is` vs `==`

---

* `dir, help`
* len
* "Boolean"
    * True/False
        * Synonyms for 0 and 1
    * "Boolean" operators
        * and, or, not
            * Short circuit
        * bool
* print (*Py23*)

---

### Running python as a script

* Python has two "modes"
    * Interactive mode, or REPL
    * Script mode
    * Also possible to run script and then enter REPL

---

#### Windows
* GUI method
    * Double-click on python file
    * A python terminal will open while the script is running and close as soon as it stops
* Command line method
    * Open cmd/powershell
    * `C:\...> py file.py` or `C:\...> file.py`

---

#### Linux/MAC OS
* Run with Python
    * Open a terminal
    * `$ python3 file.py`
* Shebang method
    * Put the line `#! /usr/bin/env python3` at the top of `file.py`
    * Run `$ chmod +x file.py` or `$ chmod u+x file.py`
    * To run Python script run `$ ./file.py`

---

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
--- 

* None
* Einföld föll
    * def
    * parameters
    * return types
    * docstrings

---

### Parameters

* Positional
* Named (with default value)
* Variable-length arguments
* Variable-length keyword arguments

----

### Scope
* Only created by functions!
* `global`
* `locals()` and `globals()`

