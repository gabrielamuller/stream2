from ryotest import *


test_is_in(range(100), 99)
test_are_equal(3, 3)
test_not_in([1, 2, 3, 4], 5)

print("All tests pass")