#  Python program that converts temperature between Fahrenheit and Celsius

print("Temperature Conversion Program")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
else:
    print("Invalid choice. Please enter 1 or 2.")
