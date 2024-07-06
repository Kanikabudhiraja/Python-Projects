# from art import logo
# print(logo)

print("Welcome in Zaika")
menu ={

    "chowmin" : 70,
    "cold drink" :50,
    "chicken rice" :130,
    "biryani":140,
    "roasted chicken":250,
    "pasta":60,
    "cold coffee":60,
    "chole rice":60,
    "sandwich":30
}

next_order= True
while next_order:
    print("Our menu")
    print("------------------------------")
    total_order=0
    for item, price in menu.items():
        print(f"{item}: Rs.{price}")

    order=input("Enter the name of item you want to add in order").lower()
    if order in menu:
        total_order+=menu[order]
        print(f"{order} added in your order")
        another_order= input("Do you want to add another item? press(yes/no)").lower()
        if another_order== 'yes':
            next_order=True
        else:
            next_order=False

    else:
        print(f"{order} is not available")
        another_order= input("Do you want to add another item? press(yes/no)").lower()
        if another_order=='yes':
            next_order=True
        else:
            next_order=False

print(f"Your Total bill is : Rs.{total_order}")