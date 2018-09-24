y = int(input("Enter any Year: "))
if y % 4 == 0 and y % 100 != 0:
    print(y, "is a Leap Year")
elif y % 100 == 0:
    print(y, "isn't a Leap Year")
elif y % 400 ==0:
    print(y, "is a Leap Year")
else:
    print(y, "isn't a Leap Year")
