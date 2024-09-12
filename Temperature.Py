print("1.fahrenheit to celsius")
print("2.celsius to fahrenheit")
Choice = input("choose conversion (1 or 2):")
if Choice == "1":
    fahrenheit = float(input("Enter temperature in fahrenhite:"))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
elif Choice == "2":
    celsius = float(input("Enter temperature in celsius:"))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
else:
    print("invalid choice, please 1 or 2")

