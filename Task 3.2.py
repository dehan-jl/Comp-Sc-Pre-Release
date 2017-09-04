import random

prev = 0

while True:
    lower = int(input("Lower Bound:"))
    upper = int(input("Upper Bound:"))
    curr = random.randint(lower, upper)
    if curr == prev:
        while curr == prev:
            curr = random.randint(lower, upper)
    print(curr)
    prev = curr
