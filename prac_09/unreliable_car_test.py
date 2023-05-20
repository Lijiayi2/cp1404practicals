from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    good_car = UnreliableCar("Good Car", 100, 90)
    bad_car = UnreliableCar("Bad Car", 100, 9)

    # drive the cars many times and print the distance driven
    for i in range(1, 11):
        print(f"\nDrive {i} km:")
        print(f"{good_car.name} drove {good_car.drive(i)} km")
        print(f"{bad_car.name} drove {bad_car.drive(i)} km")

    # print the final states of the cars
    print(f"\n{good_car.name} final state:\n{good_car}")
    print(f"\n{bad_car.name} final state:\n{bad_car}")


main()
