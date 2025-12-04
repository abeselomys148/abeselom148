income= float(input("enter you income amount: "))
def calculate_tax(income):
    if income <= 1000:
        taxrate = 0.05
        taxowed= income*taxrate
        print(f" you should pay {taxowed} money for the local govenment")
    elif 1000<= income<= 5000:
        taxrate = 0.1
        taxowed= income*taxrate
        print(f" you should pay {taxowed} money for the local govenment")
    elif 5000<= income<= 10000:
        taxrate = 0.15
        taxowed= income*taxrate
        print(f" you should pay {taxowed} money for the local govenment")
    else:
        taxrate = 0.2
        taxowed= income*taxrate
        print(f" you should pay {taxowed} money for the local govenment")
    
calculate_tax(income)
    