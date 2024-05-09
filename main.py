''' 
Requirement: You are tasked to code the vending machine logic out using Python Programming Language. 
In your code, you can have a few drinks as your items with any price (no coin). The customer should be 
able to insert any notes to buy his preferred drinks. The outcome is to release the least amount of notes 
back to the customer.
'''
from collections import Counter

def vending_machine():

    notes_myr = [1,5,10,20,50,100]   
    drinks_stock = {
        1: {"drink_id": "D001", "drink_name": "Coke Cola", "price": 2.00,"stock_left":20}, 
        2: {"drink_id": "D002", "drink_name": "Pepsi", "price": 2.00,"stock_left":20},
        3: {"drink_id": "D003", "drink_name": "Nescafe Ice", "price": 3.00,"stock_left":20},
        4: {"drink_id": "D004", "drink_name": "Lemonade", "price": 2.00,"stock_left":20},
        5: {"drink_id": "D005", "drink_name": "Milo", "price": 4.00,"stock_left":20},
        6: {"drink_id": "D006", "drink_name": "100 Plus", "price": 2.00,"stock_left":20},
        7: {"drink_id": "D007", "drink_name": "Haus Boom", "price": 5.00,"stock_left":20},
        8: {"drink_id": "D008", "drink_name": "Sparkling Juice", "price": 6.00,"stock_left":20}
   }

    print('===================================')
    print('Welcome to AXRAIL vending machine !')
    print('=================================== \n')
    print('Available drinks :\n')
    for drink_id, details in drinks_stock.items():
        print(f"Press {drink_id} to buy: {details['drink_name']}: RM {details['price']:.2f}")
    print('')
    print('=================================== \n')
    price, selected_id = select_drink(drinks_stock)
    quantity = order_quantity(drinks_stock, price, selected_id)
    total_amount = price * quantity
    print('')
    print(('==================================='))
    print("Total price: RM {:.2f}".format(total_amount))
    print(('===================================\n'))
    payment_amount = payment(total_amount)
    balance_amount = balance(total_amount, payment_amount)
    print("Payment received: RM {:.2f}".format(payment_amount))
    print(('\n==================================='))
    print("Balance: RM {:.2f}".format(balance_amount))
    print(('===================================\n'))
    print('Amount of notes received by customer:')
    print(notes_amount(notes_myr,balance_amount))

def select_drink(drinks_stock):
    while True:
        try:
            selected_id = int(input("Please select a drink by entering the number option: "))
            if selected_id in drinks_stock:
                drink_price = drinks_stock[selected_id]["price"]
                return drink_price, selected_id
            else:
                print("Invalid drink ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def order_quantity(drinks_stock, price, selected_id):
    while True:
        try:
            quantity = int(input("Enter the quantity you want to order: "))
            if quantity <= 0:
                print("Invalid input. Quantity must be greater than 0.")
            elif quantity > drinks_stock[selected_id]["stock_left"]:
                print("Invalid input. Quantity exceeds available stock.")
            else:
                return quantity
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def payment(total_amount):
    while True:
        try:
            payment_amount = float(input("Enter the payment amount: RM "))
            if payment_amount < total_amount:
                print("Insufficient payment. Please enter the full amount.")
            else:
                return payment_amount
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def balance(total_amount, payment_amount):
    return payment_amount - total_amount

def notes_amount(list,bal): 
    list.sort(reverse=True) 
    new_list = []
    remaining = bal

    for i in list:
            while remaining >= i:
                new_list.append(i)
                remaining = remaining - i
            if remaining == 0:
                break
    
    count_note = Counter(new_list)
    for note_value,count in count_note.items():
        print (f"RM {note_value}: {count} note(s)")
    

vending_machine()
