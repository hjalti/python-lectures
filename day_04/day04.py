f = open('utf8.txt', encoding='utf-8')
utf8 = f.read()
f.close()

f = open('utf8-bom.txt', encoding='utf-8-sig')
utf8bom = f.read()
f.close()

f = open('latin1.txt', encoding='ISO-8859-1')
latin1 = f.read()
f.close()


from datetime import datetime

with open('mooshak') as f:
    mooshak = [x.split('\t') for x in f.read().splitlines()]

for x in mooshak:
    x[1] = datetime.strptime(x[1].strip(), '%Y/%m/%d %S:%M')


from collections import Counter

c = (x[1].weekday() for x in mooshak)


from time import time

## Unix time stamp
time()

timestamp = datetime.fromtimestamp(1480550256.1725028)

datetime.now().strftime('%d-%m-%Y %S:%M')
