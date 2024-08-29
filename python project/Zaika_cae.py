#form art import logo
print(logo)
print("welcome in Zaik")
menu = {
        "chomin" : 
    }
print("our menu")
print("_________________________")
for item, price in menu.items():
    print(f"{item} : Rs{Price}")

order = ("Enter the name of item you want add in order").lower()
if item in menu:
    total_order += menu[item]
    print(f"{item} add in your order")
else:
    print(f"{item} is not available")
    another_order = input("Do you want add another item? press(yes/no").lower()
    if another_order =='yes':
        next_order=True
    else:
        print(f"{item} is not available ")