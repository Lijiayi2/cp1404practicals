import random

NUM_QUICK_PICKS = 5
NUM_NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

for i in range(NUM_QUICK_PICKS):
    numbers = []
    while len(numbers) < NUM_NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    print(" ".join("{:2d}".format(number) for number in numbers))
