def Celsius_To_Fahrenheit(cTemp):
    # Converting Celsius temperature to Fahrenheit
    fTemp = cTemp * 9.0 / 5 + 32
    # Returning the temperature in Fahrenheit
    return fTemp


def Fahrenheit_To_Celsius(fTemp):
    # Converting Fahrenheit temperature to Celsius
    cTemp = 5 / 9 * (fTemp - 32)
    # Returning the temperature Celsius
    return cTemp


# Main
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = Celsius_To_Fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = Fahrenheit_To_Celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
