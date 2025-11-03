choice = int(input("enter 1 to convert meter to feet, enter 2 to convert feet into meter, enter 3 to convert celisius to fahrenheit and enter 4 to convert farhanheit into celisius: "))
measurement = float(input("Enter your measurement: "))

if choice == 1:
    value = measurement * 3.281
    print(value)
elif choice == 2:
    value = measurement / 3.281
    print(value)
elif choice == 3:
    value = (measurement * 9/5) + 32
    print(value)
elif choice == 4:
    value = (measurement - 32) * 5/9
    print(value)
else:
    print("please choose the right number")
