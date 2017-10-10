def contains(x,y,n):
    while x <= y:
        if x == n:
            return True
        x = x + 1
    return False

print(contains(1,10,5))