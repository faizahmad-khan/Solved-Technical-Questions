def kelvin_to_celsius(kelvin):
    """Convert temperature from Kelvin to Celsius."""
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    """Convert temperature from Celsius to Kelvin."""
    return celsius + 273.15

# Main program
def main():
    print("Temperature Converter: Kelvin ↔ Celsius")
    print("1. Kelvin to Celsius")
    print("2. Celsius to Kelvin")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        k = float(input("Enter temperature in Kelvin: "))
        c = kelvin_to_celsius(k)
        print(f"{k} K = {c:.2f} °C")
    elif choice == "2":
        c = float(input("Enter temperature in Celsius: "))
        k = celsius_to_kelvin(c)
        print(f"{c} °C = {k:.2f} K")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()   