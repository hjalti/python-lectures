glob = 3   # This variable is in global scope

def fun():
    print(glob)
    # Declares a new variable glob in fun's scope
    glob += 3

fun()
