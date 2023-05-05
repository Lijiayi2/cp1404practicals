class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

guitars = []

with open("guitars.csv") as file:
    for line in file:
        name, year, cost = line.strip().split(",")
        guitars.append(Guitar(name, int(year), float(cost)))

for guitar in guitars:
    print(guitar)
