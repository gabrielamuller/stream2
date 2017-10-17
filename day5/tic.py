def sumlist(l):
    if l == []:
        return 0
        
    return l[0] + sumlist(l[1:])
    
print(sumlist([1, 2, 3]))