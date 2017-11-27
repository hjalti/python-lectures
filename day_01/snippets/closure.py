def outer(x):
    def inner(y):
        return x + y
    return inner

f1 = outer(3)
f2 = outer(5)

print(f1(5))
print(f2(5))

