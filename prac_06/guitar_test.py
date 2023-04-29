class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        return self.get_age() >= 50


guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 2000)

# Test get_age() method
print("Gibson L-5 CES get_age() - Expected 100. Got", guitar1.get_age())
print("Another Guitar get_age() - Expected 9. Got", guitar2.get_age())

# Test is_vintage() method
print("Gibson L-5 CES is_vintage() - Expected True. Got", guitar1.is_vintage())
print("Another Guitar is_vintage() - Expected False. Got", guitar2.is_vintage())

# Test a wrong implementation of is_vintage() method
print("50-year old guitar is_vintage() - Expected True. Got", guitar1.is_vintage())
