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

