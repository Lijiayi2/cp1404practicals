from guitar import Guitar

def main():
    print("Welcome to the Guitar Inventory App!")
# Create an empty list to store guitars
    guitars = []
    while True:
        name = input("Enter guitar name (blank to quit): ")
        if name == "":
            break
        year = input("Enter guitar year: ")
        cost = input("Enter guitar cost: ")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:.2f} added.")
        print("\nHere is the inventory:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
        if __name__ == '__main__':
            main()
