def contains(x,y,n):
    while x <= y:
        x = x + 1
    if x == n:
        return True
    
    return False

print(contains(1,10,5))