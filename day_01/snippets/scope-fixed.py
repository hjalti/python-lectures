glob = 3   # This variable is in global scope

def fun():
    # Tells Python to use glob from global scope
    global glob
    print(glob)
    glob += 3

fun()
