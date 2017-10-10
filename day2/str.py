s = "ABC"

print(s.lower())

s = "the man ran away"

print(s.title())

s = "ABCDEFGHIJKLM"

result = s[4:len(s)]
print(result)

s = "ABCDEFGHIJKLM"

result = s[:-4]
print(result)

l = [13, 34, 21, 55, 17, 89, 100]

print(l[-3])
s = "Hello"
print(s[4])
r = range(3, 21, 3)
x = list(r)
print(list(r))

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l[2])

l = [[29, 180, 86], [29, 100, 86], [29, 190, 86]]
print(l[2][1])

l = [i * 2 for i in range(10)]
print(l)

l = [i for i in range(0, 22, 3)]
l2 = [i * 3 for i in range(8)]
print(l)

l = [i % 2 == 0 for i in range(10)]
print(l)

r = ["Richard", 21, 130, 86]
print(r[0])

print(sum(list(range(11))))

people = [
    {
    "name": "Richard",
    "age": 43,
    "favorite-color": ["Blue", "Green"]
},
  {
    "name": "Tom",
    "age": 33,
    "favorite-color": []
},
{
    "name": "Harry",
    "age": 23,
    "favorite-color": ["Green", "White", "Purple"]
}
]

print(people[-1]["favorite-color"][1])