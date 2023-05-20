from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test the SilverServiceTaxi class."""
    hummer = SilverServiceTaxi("Hummer", 200, 4.92, 4)
    print(hummer)
    hummer.drive(18)
    print(hummer)
    print(f"Fare: ${hummer.get_fare():.2f}")


main()
