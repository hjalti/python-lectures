---
title: Forritunarmálið Python
subtitle: Day 3 \newline Modules and Functional Programming
author: Hjalti Magnússon
date: 29.\ nóvember 2017
---

# Modules

## Python modules

* Python Standard Library is a large library of very useful things
* Syntax
    * `import module (as alias)`
    * `form module import fun/cls (as alias)`
* *All* python files are modules

## Example

```
>>> import string
>>> dir(string)

>>> from string import punctuation
>>> punctuation
```

# Extending the basics

## `decimal` - arbitrary precision floating point numbers

```
>>> from decimal import Decimal as D
>>> D('1.2') + D('2.2')
>>> 1.2 + 2.2

>>> D('0.1') + D('0.1') + D('0.1') - D('0.3')
>>> 0.1 + 0.1 + 0.1 - 0.3
```

## `fractions` - rational numbers

```
>>> from fractions import Fraction as Fr
>>> Fr(2, 3) + Fr(1, 3)
>>> Fr(2, 3) + Fr(1, 3) == 1
>>> Fr(1.2)
>>> Fr('1.2')
>>> Fr('9/5')
>>> f = Fr('66.6')
>>> f.numerator
>>> f.denominator
```

## `collections` - more data structures

* `defaultdict`
    * A nicer version of dictionary

* `Counter`
    * One of Python's coolest data structures

* `deque`
    * If you need fast prepend, append

## `datetime` - date and time

* A module that allows us to work with
    * Dates
    * Time
    * Dates with time
    * Time intervals

## `datetime`

```
>>> from datetime import datetime, date
>>> datetime.now()
>>> date.today()

>>> d1 = datetime(2017, 10, 28)
>>> d2 = datetime.now()
>>> d2 - d1
```

## Printing and parsing

```
>>> now = datetime.now()
>>> now.strftime('%d-%m-%Y %H:%M:%S')
>>> now.strftime('%d. %B %Y at %H:%M:%S')

>>> now.strptime('29-09-2018', '%d-%m-%Y')

>>> import time
>>> time.time()
>>> datetime.fromtimestamp(time.time())
```

# Debugging

## `pdb` - the Python debugger

Python comes with a built in debugger, pdb

```
# Set a breakpoint
import pdb; pdb.set_trace()
```

## Commands

* **s(tep)** "Jump into"
* **n(next)** "Jump over"
* **c(ontinue)** Run until next breakpoint
* **r(eturn)** Run until current function returns
* **l(ist)** (**ll**) Print where you are
* **p(rint)** (**pp**) Print
* **q(uit)** Quit the debugger
* **!** Execute statement
* **interact** Start Python interpreter

# Functions

## More about functions

* In Python functions are first class citizens
    * They can be passed as variables
    * They can be returned by functions


## Lambda functions

Python provides anonymous functions

```
>>> lambda x: x ** 2

>>> f = lambda x: x ** 2
>>> f(4)

# They can take more than one parameter
>>> g = lambda x, y: x * y
>>> g(4, 5)

# Or none
>>> h = lambda: 1377
>>> h()
```

# Functional programming

## Lists

Many builtin functions in Python take functions as parameters

* `min, max, sum`
* `map, filter, all, any`
* `sorted`

# Problems

## Problem 0

Find the word count of The Raven

## Problem 1

Find the country with the most unique letters

## Problem 2

Find the country in Europe with the highest population

## Problem 3

Sort all countries by population

## Problem 4

Sort all countries by population

## Problem 5

Find the user with the most accepted submissions

## Problem 6

For each user that has submitted problems, find the number of solved problems he has solved an his full name


# Assert

## Assert is a friend

* Assert that the state of your program is consistent
    * Check that "this should never happen" doesn't happen
