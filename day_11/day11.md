---
title: Forritunarmálið Python
subtitle: Day 11 \newline Pip and more
author: Hjalti Magnússon
date: 11.\ desember 2017
---

# Logging

## Logging

* Powerful preemptive debugging
* You will never log too much

## Basic setup

```
import logging
logging.debug('yay')
logging.error('yay')
```

## Logging to a file

```
logging.basicConfic(filename='debug.log', level=logging.DEBUG)
logging.debug('yay')
logging.error('yay')
```

## Formatting messages

```
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
```


# Third party packages

## PyPI

* The Python Package Index
    * A repository of software for Python

## pip

* A Python module to install packages from PyPI

```
# Normally pip is installed as a program
$ pip3 install [package name]

# Can also be run like this
$ python3 -m pip install [package name]
```

# Requests

## Requests

* A more powerful library to make HTTP requests

## Example

```
>>> import requests
>>> r = requests.get('http://dyraklam.is')
>>> r.ok
>>> r.status_code
>>> r.encoding
>>> r.text[:40]
```

## Example

```
>>> r = requests.get('http://apis.is/ship',
...                  params={'search': 'test'})
>>> r.json()
```

# BeautifulSoup

## BeautifulSoup

* An HTML and XML parser

## Example

```
>>> from bs4 import BeautifulSoup
>>> r = requests.get('http://dyraklam.is')
>>> soup = BeautifulSoup(r.text, 'html.parser')
>>> soup.img
>>> len(soup('img'))
```
