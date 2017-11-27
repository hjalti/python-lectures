lis = [1, 5, 2, 3, 4]

it = iter(lis)   # Create iterator
while True:
    try:
        i = next(it)   # Consume one item from it
    except StopIteration:
        break
    print('i is now', i)
