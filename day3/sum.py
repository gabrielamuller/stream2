def listsum(l):
    total = 0
    for n in l:
        total += n
    return total
    
print(listsum([1, 2, 5, 9, 13]))

def sumlist(l):
    if l == []:
        return 0
    return l[0] + sumlist(l[1:])
print(sumlist([1, 2, 5, 9, 13]))

print({i : i%2==0 for i in range(5)})

words = ["Hello", "There", "How", "Are", "You"]
l = {w : len(w) for w in words}
print(l)
        