def add(x,y):
    return x + y
print (add(2,4))


def function(x):
    if x > 10:
        return "Big"
    else:
        return "Small"
print(function(5))

def are_same(x,y):
    if x == y:
        return True
    else:
        return False
        
print(are_same(5,5))


def size(x,y):
    if x > y:
        return "Bigger"
    elif x < y:
        return "Smaller"
    else:
        return "Same"
        
print(size(5,6))