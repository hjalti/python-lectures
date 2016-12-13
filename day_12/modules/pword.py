import string as _st
from random import choice as _choice, randint as _randint
from pathlib import Path as _Path
import argparse

_letters = _st.ascii_letters + _st.digits
_letters_with_symbols = _letters + _st.punctuation

class _Words:
    def __init__(self, filename):
        self.filename = filename
        self.words = None

    def _parse_file(self):
        with open(self.filename):
            with open(self.filename) as f:
                self.words = f.read().splitlines()

    def get_word(self):
        if self.words is None:
            self._parse_file()
        return _choice(self.words)

_file = _Path(__file__).parent / 'all_words.txt'
_words = _Words(str(_file))

def random(minlen=5,maxlen=10,punct=False):
    letters = [_letters, _letters_with_symbols][punct]
    return ''.join( _choice(letters) for _ in range(_randint(minlen, maxlen)) )

def xkcd(words=3, separator=' '):
    return separator.join( _words.get_word() for _ in range(words) )


def _randpass(args):
    for _ in range(args.count):
        print(random(args.min_len, args.max_len, args.use_punct))

def _xkcdpass(args):
    for _ in range(args.count):
        print(xkcd(args.nwords, args.sep))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a password')
    subparsers = parser.add_subparsers()

    parser_rand = subparsers.add_parser('rand', help='Generate a random password')
    parser_rand.add_argument('count', metavar='N', nargs='?', default=1, type=int, help='Number of passwords to be generated (default: %(default)s)')
    parser_rand.add_argument('-m', '--min-len', metavar='MIN', default=5, type=int, help='Minimum length of password (default: %(default)s)')
    parser_rand.add_argument('-a', '--max-len', metavar='MAX', default=10, type=int, help='Maximum length of password (default: %(default)s)')
    parser_rand.add_argument('-p', '--use-punct', action='store_true', help='Use punctuations in passwords (default: %(default)s)')
    parser_rand.set_defaults(func=_randpass)

    parser_xkcd = subparsers.add_parser('xkcd', help='Generate a password using dictionary words')
    parser_xkcd.add_argument('count', metavar='N', nargs='?', default=1, type=int, help='Number of passwords to be generated (default: %(default)s)')
    parser_xkcd.add_argument('-w', '--nwords', metavar='NWORDS', default=3, type=int, help='Number of words to use in password (default: %(default)s)')
    parser_xkcd.add_argument('-s', '--sep', metavar='SEP', default=' ', help='Separator used between words (default: "%(default)s")')
    parser_xkcd.set_defaults(func=_xkcdpass)

    args = parser.parse_args()
    args.func(args)
