import re
from itertools import chain

config = '''
cuteness: 1200
timeout: 400
sofa_tearing: 990
description: Extremely playful and fun
breed: Sphynx
'''











































lex = re.compile(r'end|print|;|\+|-|\*|\(|\)|\b\d+\b|\b[A-Za-z]+\b|\s+|.+')
comp_lex = re.compile(r'(?P<END>end)|(?P<PRINT>print)|(?P<EQ>=)|(?P<SEMICOL>;)|(?P<PLUS>\+)|(?P<MINUS>-)|(?P<MUL>\*)|(?P<LPAREN>\()|(?P<RPAREN>\))|(?P<INT>\b\d+\b)|(?P<ID>\b[A-Za-z]+\b)|(?P<WS>\s+)|(?P<ERR>.+)')


program = '''var = 3;
b = 4 * (7-var); @
print b;
9ee
end'''

tokens = sum(map(comp_lex.findall,program.split()),[])

for m in chain(*map(comp_lex.finditer,program.split())):
    next(filter(lambda x: x[1], m.groupdict().items()))
