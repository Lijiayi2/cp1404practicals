import csv

def read_csv_file(filename):
    """Reads the CSV file and returns a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            data.append(row)
    return data

def get_champions(data):
    """Returns a dictionary of champions and how many times they have won."""
    champions = {}
    for row in data:
        if row[0] != 'Year':
            name = row[1]
            if name in champions:
                champions[name] += 1
            else:
                champions[name] = 1
    return champions

def get_countries(data):
    """Returns a set of countries of the champions in alphabetical order."""
    countries = set()
    for row in data:
        if row[0] != 'Year':
            country = row[2]
            countries.add(country)
    return sorted(countries)

def display_results(champions, countries):
    """Displays the processed information."""
    print("Champions:")
    for name, count in champions.items():
        print(f"{name}: {count}")
    print("Countries:")
    countries_str = ", ".join(countries)
    print(countries_str)

def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)
    champions = get_champions(data)
    countries = get_countries(data)
    display_results(champions, countries)

if __name__ == "__main__":
    main()

