#gotta finish this
# POINT OF SALE

from inventory import inventory

customer_cart = []
sub_total = []
sales_tax = 0.07

def cashier():
    print("\n ------------ WECOME TO THE STORE ------------ ")
    print(f"There are {len(inventory)} items for sale:")
    print(inventory)
    user_answer = input("\nWhat do you wish to buy?\n>> ").lower()
    while user_answer != "buy":
        if user_answer in inventory:
            customer_cart.append(user_answer)
            user_answer = input("Item added to cart. Next item to add? or " \
                "Type 'buy' to complete your order!.\n>> ").lower()
        elif user_answer == "inventory":
            print(inventory)
            print("There are: " + str(len(inventory)) + " items for sale.")
            user_answer = input("\nWhat do you wish to buy?\n>> ").lower()
        else:
            user_answer = input("Sorry, we do not have that item. Next item? or " \
                "Type 'buy' to complete your order!.\n>> ").lower()



#----loop for customer placing items in cart -----
while True:
    cashier()
    print("\n\n  ------ Shopping Cart ------\n", customer_cart)
    response = input("\n\nDo you wish to buy anything else? (yes/no)\n>> ").lower()
    if response == "yes":
        cashier()
        print("\n\n  ------ Shopping Cart ------\n", customer_cart)
        for items in customer_cart:
            sub_total.append(inventory[items])
        total_tax = sum(sub_total) * sales_tax
        total_due = total_tax + sum(sub_total)   
    elif response == "stop" or response == "shutdown" or response == "quit":
        break
    else:
        for items in customer_cart:
            sub_total.append(inventory[items])
        total_tax = sum(sub_total) * sales_tax
        total_due = total_tax + sum(sub_total)


##----customer checkout ------
    print(f"\n\nSubtotal: ${round(sum(sub_total), 2)}")
    print(f"Tax: ${round(total_tax, 2)}")
    print(f"Your total amount: ${round(total_due, 2)}")
    payment = float(input("Amount you're paying? "))
    result = total_due - payment
    result = round(result, 2)

    if result != 0 and result > 0:
        print(f"Sorry, you still owe ${result} to complete your purchase!\n")
        result = 0 
        customer_cart = []
        sub_total = []
    elif result < 0:
        print(f"Paid in full. Your change is ${abs(result)}\n")
        result = 0
        customer_cart = []
        sub_total = []
    else:
        print("Paid in full! Have a good day!\n")
        result = 0
        customer_cart = []
        sub_total = []


