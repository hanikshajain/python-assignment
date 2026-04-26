temperature/
│── __init__.py
│── celsius_to_fahrenheit.py
│── fahrenheit_to_celsius.py
│── celsius_to_kelvin.py
main.py

def convert(celsius):
    return (celsius * 9/5) + 32

def convert(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert(celsius):
    return celsius + 273.15

    # This file makes 'temperature' a package

    from temperature import celsius_to_fahrenheit
from temperature import fahrenheit_to_celsius
from temperature import celsius_to_kelvin

print("Temperature Conversion Menu:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit.convert(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius.convert(f))

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    print("Kelvin:", celsius_to_kelvin.convert(c))

else:
    print("Invalid choice!")