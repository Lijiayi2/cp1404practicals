class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50


my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(my_guitar)
print("Age: {} years".format(my_guitar.get_age()))
print("Is vintage? {}".format(my_guitar.is_vintage()))
