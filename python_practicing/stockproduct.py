"""stockproduct model."""
#!/usr/bin/env python3

import uuid
item = []
class StockItem():
    """Define StockItem class."""

    def __init__(self, item_id, item_name, price, category, quantity = 0):
        """Define init method.

        Attributes:

        item_id :   The unique identifier of the item in stock.
        item_name:  The name of the item.
        quantity:   The units/quantity of the items.
        price :     The price of the item
        category:   The category of the item.
        """
        self.item_id = item_id
        self.item_name = item_name
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        else:
            self.quantity = quantity
        try:
            if isinstance(price, int):
                self.price = price
        except TypeError as e:
            print("price must be an integer")

        self.category = category


    def add_stock(self, quantity):
        """Define add_stock method."""
        self.quantity = self.quantity + quantity 
        return self.quantity
    def display(self):
        """Define display method."""
        stock_items = f"item_id: {self.item_id}\nitem_name: {self.item_name}\n Quantity: {self.quantity}\ncategory: {self.category}"

        return stock_items

    def checkout(self, quantity):
        """Definig the checkout of stock."""

        self.quantity = self.quantity - quantity
        return self.quantity

    def update_price(self, new_price):
        """Define update method."""
        try:
            new_price = float(new_price)
            self.price = new_price
            print("price updated successfully.")
        except ValueError:
            print("The price must be a number.")




    def __str__(self):
        return f"Item ID: {self.item_id}\nItem Name: {self.item_name}\nPrice: {self.price}\nQuantity: {self.quantity}\nCategory: {self.category}"




while True:
    print("Please select choose what you want to do: ")
    print("1 for add_item")
    print("2 for display")
    print("3 for remove item")
    print("4 for update price")
    print("5 to stop the program.")
    choice = input("Please enter your choice: ")
    if choice == '1':
        while True:
            item_name = input("please enter the item name: ")
            if item_name.lower() == "done":
                print("breaking out of the loop")
                print()
                break
            price = int(input("Please enter the price of the item: "))
            category = input("Please enter the item category: ")
            quantity = int(input("Please enter the quantity: "))
            print()
            item_id=uuid.uuid4()
            a = StockItem(item_id, item_name, price, category, quantity)
            item.append(a)
            #print(a.add_stock(quantity))
            #print(a.item_id)
            #print(a.price)
            #print(a.category)
            #print(a.item_name)
    elif choice == '2':
        for stock_item in item:
            print(stock_item.display())
            #print(item.item_name)
    #checkout products from stock
    elif choice == '3':
        name = input("please enter the name of product: ")
        quantity = int(input("Please enter the quantity to be checked-out: "))
        item_found = False  # Keep track if the item is found
        for stock_item in item:
            if stock_item.item_name == name:
                print(stock_item.checkout(quantity))
                item_found = True  # Set the flag to True if item is found
                break  # Exit the loop once the item is found and checked out
            if not item_found:
                print("Item not in stock.")  # Display if the item is not found in any iteration
    # Loop to update the price
    update_item_name = input("Enter the name of the item to update the price: ")
    for stock_item in item:
        if stock_item.item_name == update_item_name:
            new_price = int(input("Enter the new price: "))
            stock_item.update_price(new_price)
            break
        else:
            print("Item not found in stock.")

    else:




        




