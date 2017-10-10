def count_upper_case(message):
    return sum([2 for c in message if c.isupper()])

def count_lower_case(message):
    return sum([1 for c in message if c.islower()])

print(count_lower_case("Hello World How Are You?")) + (count_upper_case("Hello World How Are You?"))

def score_message(message):
    return sum([2 for c in message if c.isupper()]) + sum([1 for c in message if c.islower()])
print(score_message("Hello"))

message = "HelloWorld"
scores = [1, 2]
print([scores[int(c.isupper())] for c in message])