sortlist = [ ['chm', 'hjuDd', 'vN', 'YKBXqv'],
 ['', 'khju', 'WJ', ''],
 ['rLToDOu', 'PXDfBe', 'pn', 'VpUcHiZ'],
 ['rLToDOu', 'PXDfBe', 'pn'],
 ['A', 'nwS', 'lk', 'r'],
 ['OPCAG', 'glzfGP', 'Z', 'CmuDLj'],
 [],
 ['X', 'RWji', 'lPqt', 'CWALZws'],
 ['uGX', '', '', 'q'],
 ['ecJbzh', 'OHp', 'E', 'VaqeiEI'],
 ['oLaml', 't', 'J', ''],
 ['Z'],
 ['AYFC', 'uHpM', 'eKaRQ', 'kXtzoF']
]

strings = ['nbJbUq',
 'vYZBsRwFA',
 'UAh',
 'Rmu',
 'ZyfBhkjs',
 'XZJORVG',
 'A',
 'SUX',
 'gsEgL',
 'dhfjO',
 'Eo',
 'ODhSouKb',
 'tgbIowR',
 'phADFGtUpa',
 'hurEhil',
 'RFjTqB',
 '',
 'gAeHeiLmL',
 'zDuMbR',
 'i',
 'EiAqf',
 'UAkCd',
 'AUWeKsrU',
 'yGtqxIOj',
 '',
 'jO',
 'eewKGIwgnv',
 'LiRCApSUAK',
 'Rgg',
 '']

filterlist = [1, [1,2], [], 0, 0, {}, frozenset(), set(), '', 'yay', 3, 0, 0]



import itertools
students = range(50)
print(list(zip(students,itertools.cycle('abcd'))))


# combinations: Poker hands
rank = 'A23456789TJQK'
suit = 'HSCD'

cards = [ ''.join([a,b]) for a,b in itertools.product(rank, suit) ]
# choose hand with properties
print(cards)


# Generate all strings over alphabet

binary_strings = list(itertools.product('01', repeat=4))

# Permutations
# SEND + MORE = MONEY?

def verbal_arithmetic(first, second, result):
    nonzero = {first[0], second[0], result[0]}
    letters = list(set(''.join([first, second, result])))
    n = len(letters)
    for p in itertools.permutations(list(map(str,range(10))), n):
        d = dict(zip(letters,p))
        mapped = { v:k for k,v in d.items() }
        if '0' in mapped and mapped['0'] in nonzero:
            continue
        f, s, res = map(lambda st: int(''.join(d[x] for x in st)), [first, second, result])
        if f + s == res:
            print(d)
