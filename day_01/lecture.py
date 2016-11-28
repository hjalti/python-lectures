### ARITHMETIC ###


# Normal arithmetic
3 + 4
1 - 2
6 % 2

# Floating point division
4 / 3

# Integer division
4 // 3

# Comparison
4 == 4
3 != 2
4 < 5
9 >= 3


# Bit operators

# Bit shift
1 << 10
1024 >> 10

# xor
1023 ^ 1337

# and/or

512 | 256
1111 & 222
~1024

# integers are big integers
123109283019283109283019823019283 * 129837128379182739182731982371982
2 ** 10000

# hex integers
0xdeadbeef

# oct integers
0o1337


# Floating point numbers

1.2345
1.3E23

# Complex numbers

3j + 3
1j
(4j + 3) * (1j - 2)




### STRINGS ###

# 8 flavours

"Double quotes"
"That's very interesting"
'Single quotes'
'Ghandi said: "YAY"'
'Strings in Python are Unicode ¹²³@ł€æß„«»¢€¶ŧ„đŋ¢“”'
'Special characters and quotes are escaped with a backslash \n\r\t\\ like normally'


'''Multiline strings
Can span multiple lines
    Spacing is preserved
'''

"""
Multiline strings...
also work with double quotes
"""

r'Raw strings are verbatim (no escape character) \r\t\n\' (except for quotes)'
r"\These work too"

r'''
Raw multiline string!
'''


# String concatenation
'Hello, ' + "World!"

# or (but don't use!)

'Hello, ' "World!"

# Repetition

19 * 'Na' + ' Batman!'



### VARIBLES ###

a = 3
b = a * 12
c = a * 'yay'

a += 1
a *= 12
b //= 2
b **= 2
a |= 19
a &= 99


### LISTS ###

# Lists are resizable arrays
[1, 2, 3]
[1, 'a', 3.4]
[1, ['a', 3, [3.4]], 'yay']

# List concatenation
[1,3] + [2,4]

# List repetition
4 * [1,2]

# Member access
a = [1, 'yay', [5,3]]
a[2]
a[0]
a[1][2]
a[2][0]


### dir and help ###

dir()

li = [1,2,3]
dir(li)
help(li)

st = 'yay'
dir(st)
help(st)


### "BOOLEAN" OPERATORS ###

True
False

True == 1
False == 0

# bool function

bool(0)
bool(1)
bool(32)
bool([])
bool([1,2,3,4])
bool([1])
bool([[]])
bool('')
bool('yay')

# operators

True and False
True or False
1 == 3 or 3 < 12
3 * 3 < 18 and not (4 < 12 or 5 > 18)


[] or 0 or 'yay'
[] or 0 or ''

[1,2,3] and ''
[1,2,3] and 'w00t'


### PRINT FUNCTION ###

print('Hola, Mundo!')
print(3)
print([1,2,3,4])
print(1,'yay',3)


### CONTROL STRUCTURES ###

# Indentation

x = 3

if x == 1:
    print('yay')
elif x == 2:
    print(42)
else:
    print('w00t')


# body of control structures cannot be empty: pass

if x == 13:
    pass
else:
    print(':D')


# loops

# while

i = 0

while i < 12:
    print('i is', i)
    i += 1


while i < 12:
    if i == 3:
        continue
    if i == 10:
        break
    print('i is', i)
    i += 1


# for

li = [1, 3, 19, 'yay', 'panda']

for x in li:
    print(x)

# iterators

# ask the list for an iterator over its elements
it = iter(li)

# ask the iterator for the next element
next(it)
next(it)
next(it)
next(it)
next(it)

# deconstructed for loop

it = iter(li)
while True:
    try:
        i = next(it)
    except StopIteration:
        break
    print(i)


# range

r = range(10)

r[3]
r[9]
it = iter(r)
next(it)
next(it)
next(it)
next(it)


for i in range(10):
    print(i)


# turn iterables into lists

list(range(10))


# for/else

t = 1337

# using flags

prime = True
for i in range(2, t):
    if t % i == 0:
        prime = False
        break
if prime:
    print(prime, 'is a prime!')

# alternative

for i in range(2,t):
    if t % i == 0:
        break
else:
    print(prime, 'is a prime!')




