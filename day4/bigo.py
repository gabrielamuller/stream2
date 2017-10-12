from random import randint

nums = [randint(1, 101) for i in range(100)]
count= 0

for i in nums:
    for j in nums:
        for k in nums:
            count += 1
            if i + j + k == 147:
                print("{0} and {1} and {2} add up to 147".format(i, j, k))
                
print("It happened {0} times".format(count))