---
title: Forritunarmálið Python
subtitle: Day 8 \newline Classes
author: Hjalti Magnússon
date: 6.\ desember 2017
---

# Classes

## Classes in Python

* Create a new namespace
* A dictionary under the hood
* No such thing as "private"
    * Variables and methods starting with `_` should not be messed with
* Attributes do not need to be defined in the class definition

## Classes vs instances

* Classes and instances can have attributes
    * Can reference class attributes through instances
* Class functions can be called in two ways
    * When called on an instance, the first parameter is the instance itself
    * When called on a class, it behaves as a normal function

## Inheritance

* `isinstance`
    * Check if an object is an instance of a class or a subclass thereof
* `issubclass`
    * Check if a class is a subclass (or same class) as another
* `super`
    * Call the constructor of a superclass
* Python supports multiple inheritance

## Static methods and class methods

* `staticmethod`
    * A decorator that defines a method as a static method
* `classmethod`
    * A decorator that defines a method as a class method

## Properties

* `prop = property(fun1, fun2)`
* Decorator

## Special functions

* String representation
    * `__repr__`, `__str__`
* Indexing
    * `__getitem__`, `__setitem__`
* Attributes
    * `__getattribute__`, `__setattr__`
* Builtin functions
    * `__len__`, `__bool__`
* Operators
    * `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
* Iterator
    * `__iter__`

