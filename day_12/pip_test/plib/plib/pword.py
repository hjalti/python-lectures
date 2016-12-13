import string
from random import choice, randint
from pathlib import Path

_letters = string.ascii_letters + string.digits
_letters_with_symbols = _letters + string.punctuation

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
        return choice(self.words)

_file = Path(__file__).parent / 'all_words.txt'
_words = _Words(str(_file))

def random(minlen=5,maxlen=10,punct=False):
    letters = [_letters, _letters_with_symbols][punct]
    return ''.join( choice(letters) for _ in range(randint(minlen, maxlen)) )

def xkcd(words=3, separator=' '):
    return separator.join( _words.get_word() for _ in range(words) )

