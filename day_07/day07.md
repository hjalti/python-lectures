---
title: Forritunarmálið Python
subtitle: Day 7 \newline Data
author: Hjalti Magnússon
date: 4.\ desember 2017
---

# Data

## Structured vs unstructured

* We have been working mainly with unstructured data
    * No formal definition
    * Possible ambiguities

* Structured data
    * Formal representation of data
    * Well defined syntax
    * No ambiguities


## JSON

* JavaScript Object Notation
* Consists of
    * objects (dictionaries)
    * arrays (lists)
    * strings
    * numbers
    * booleans
    * null

## JSON

```
>>> import json
>>> js = '''{
...   "key1": 3,
...   "key2": 43.2,
...   "list": [1, 2, 3],
...   "boolean": true,
...   "test": null
... }'''
```

## JSON

```
>>> json.loads(js)
```

## JSON

```
>>> json.dumps({
...     'test': 3,
...     5: True,
...     4.3: None
... })
```

## Serialization

* Translating data structures into a format so that they can be recreated again
* JSON can be used to serialize a subset of Python's data structures
    * Plain text serialization

## Pickle

* Python specific serialization
    * Binary serialization
* Can serialize
    * Most/all Python data structures
    * Functions
    * Classes

## Pickle

```
>>> import pickle
>>> pickle.dumps({
...     'a': {1,2,3},
...     'b': [1,2,3],
...     'c': [True, None, (1,2,3)]
... })
```

## Pickle vs. JSON

* JSON
    * Plain text
    * Can only serialize a small part of Python's data structures
    * Widely used

* Pickle
    * Binary
    * Can serialize most of Python's data structures
    * Not (or rarely) used outside Python


## XML

* Plain text
* `xml.etree.ElementTree`

## sqlite3

* SQL database in a single file

## CSV

* Comma Separated Value
* Tabular data

# HTTP requests

## `urllib.requests`

* Fetch data over HTTP (and HTTPS and FTP)

# A little extra

## Meta programming

* Like many interpreted languages, Python can execute Python code
* `eval`
    * Evaluates an expression and returns its value
* `exec`
    * Executes python code
