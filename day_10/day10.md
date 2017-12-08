---
title: Forritunarmálið Python
subtitle: Day 10 \newline Scripts
author: Hjalti Magnússon
date: 8.\ desember 2017
---

# Scripts

## Running Python code

* Up to now we have just been writing functions in Python
* Real worlds programs are run either in a
    * command line, then called a script
    * graphical user interface (GUI)

## Interacting with the user

* Two common ways of interacting with the user
    * Prompting the user and reading from standard input
    * Command line parameters

* Python has good support for command line parameters
    * `argparse`

## Traditions

* Traditionally Python uses Unix style command line arguments
* Programs have
    * Arguments (can be optional)
    * Options
        * Optional arguments
        * Usually have "sane" defaults

## Options

* Options are usually denoted with `-o` (short form) or `--long-option` (long form)
* Options can take no parameters
    * In which case they are called flags
* Options can also take parameters
    * In short form: `-o param another_param "param with spaces"`
    * In short form: `--long-option param another_param "param with spaces"`

## An example

```
git [--version] [--help] [-C <path>]
    [-c <name>=<value>] [--exec-path[=<path>]]
    [--html-path] [--man-path] [--info-path]
    [-p|--paginate|--no-pager]
    [--no-replace-objects] [--bare]
    [--git-dir=<path>] [--work-tree=<path>]
    [--namespace=<name>] [--super-prefix=<path>]
    <command> [<args>]
```

## Problem

CSV program that can

* Print out a CSV file
* Limit columns and rows
* Reverse the rows
* Number rows
* Sum columns
* Aggregate rows
