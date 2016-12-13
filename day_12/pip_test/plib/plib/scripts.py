from .pword import random, xkcd

import argparse
from cowpy import cow

def randpass():
    parser = argparse.ArgumentParser(description='Generate a password')

    parser.add_argument('count', metavar='N', nargs='?', default=1, type=int, help='Number of passwords to be generated (default: %(default)s)')
    parser.add_argument('-m', '--min-len', metavar='MIN', default=5, type=int, help='Minimum length of password (default: %(default)s)')
    parser.add_argument('-a', '--max-len', metavar='MAX', default=10, type=int, help='Maximum length of password (default: %(default)s)')
    parser.add_argument('-p', '--use-punct', action='store_true', help='Use punctuations in passwords (default: %(default)s)')

    args = parser.parse_args()

    for _ in range(args.count):
        print(random(args.min_len, args.max_len, args.use_punct))


def _xkcdpass_string():
    parser = argparse.ArgumentParser(description='Generate a password using dictionary words')

    parser.add_argument('count', metavar='N', nargs='?', default=1, type=int, help='Number of passwords to be generated (default: %(default)s)')
    parser.add_argument('-w', '--nwords', metavar='NWORDS', default=3, type=int, help='Number of words to use in password (default: %(default)s)')
    parser.add_argument('-s', '--sep', metavar='SEP', default=' ', help='Separator used between words (default: "%(default)s")')

    args = parser.parse_args()

    return '\n'.join(xkcd(args.nwords, args.sep) for _ in range(args.count))


def xkcdpass():
    print(_xkcdpass_string())


def cowpass():
    cheese = cow.Moose()
    print(cheese.milk(_xkcdpass_string()))

