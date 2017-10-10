def fizzbuzz(n):
    if n%15 == 0:
        return "FizzBuzz"
    elif n%3 == 0:
        return "Fizz"
    elif n%5 == 0:
        return "Buzz"
    else:
        return n

l = [fizzbuzz(i) for i in range(100)]
print(l)