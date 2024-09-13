print("1:sum 2:Sub 3:Mult 4:Div")
choice = input("Enter your choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(f"the result is: {num1 + num2}")
    elif choice == '2':
        print(f"the result is: {num1 - num2}")
    elif choice == '3':
        print(f"the result is: {num1 * num2}")
    elif choice == '4':
        print(f"the result is: {num1 / num2}")
else:
    print("Invalid entry")
