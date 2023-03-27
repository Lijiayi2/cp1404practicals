import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0  # $100
INITIAL_PRICE = 10.0  # $10
Day = 0

OUTPUT_FILE = "output_price.txt"
out_file = open(OUTPUT_FILE, 'w')
price = INITIAL_PRICE
print(f"Starting price:${price:.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    Day += 1
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

  price *= (1 + price_change)

  print(f"On day {Day} price is: ${price:,.2f}", file = out_file)
  print(f"On day {Day} price is: ${price:,.2f}")
out_file.close()
