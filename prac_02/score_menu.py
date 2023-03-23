def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def convert_usd_aud(usd):
    return usd * 1.35


def display_report(name, score):
    print("{} scored {}".format(name, score))


def calculate_average(first, second):
    return (first + second) / 2


def is_even(number):
    return number % 2 == 0


def get_age():
    age = int(input("Enter your age: "))
    while age < 0 or age > 150:
        print("Invalid age")
        age = int(input("Enter your age: "))
    return age


def main():
    print("Menu:")
    print("1. Get a valid score")
    print("2. Print result")
    print("3. Show stars")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    while choice != 4:
        if choice == 1:
            score = int(input("Enter score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Enter score: "))
        elif choice == 2:
            print(determine_grade(score))
        elif choice == 3:
            for i in range(score):
                print("*", end="")
            print()
        else:
            print("Invalid choice")
        print("Menu:")
        print("1. Get a valid score")
        print("2. Print result")
        print("3. Show stars")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
    print("Finished")


main()