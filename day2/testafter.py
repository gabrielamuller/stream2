def count_upper_case(message):
            return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("$%^&") == 0, "Only special characters"
assert count_upper_case("123456789") == 0, "Only numbers"
assert count_upper_case("ABCDE") == 5, "Upper case"

print("All tests pass")
