from pathlib import Path
from random import randint, choice, random
from string import ascii_letters

def rand_str():
    return ''.join(choice(ascii_letters) for _ in range(randint(4,10)))

def rand_file():
    ext = ['.py', '.txt']
    return rand_str() + choice(ext)


def gen(p, prob=1.0):
    newprob = prob * 0.8
    for d in range(5):
        if random() < prob:
            nf = p / rand_file()
            nf.write_text('Python is fun!')
        if random() < prob:
            nd = p / rand_str()
            nd.mkdir()
            gen(nd, newprob)


p = Path('gen')
p.mkdir(exist_ok=True)
gen(p, 0.7)

