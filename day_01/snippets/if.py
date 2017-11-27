a = 99
if a < 3:
    print('a is small')
    if a < 0:
        print('a is negative')
    else:
        pass   # A no-op statement
elif 3 <= a <= 10:
    print('a is slightly larger')
else:
    print('a is big')
