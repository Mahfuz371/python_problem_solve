AMOUNT = int(input("Enter sale price:"))
if (AMOUNT > 0):
    if (AMOUNT >= 100):
        dis = AMOUNT*0.10
    elif (AMOUNT < 100):
        dis = AMOUNT*0.05
    print("Discount :",dis)
    print("Net pay :",AMOUNT-dis)
else:
    print("invalid error")
