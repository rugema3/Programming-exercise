"""stockproduct model."""
#!/usr/bin/env python3

import uuid

class StockItem():
    """Define StockItem class."""

    def __init__(self, item_name, price, category, quantity = 0, item_id=uuid.uuid4()):
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


    def add_stock(self):
        """Define add_stock method."""
        self.quantity = self.quantity + quantity 
        return self.quantity


#item_id = uuid.uuid4()
item_name = input("please enter the item name: ")
price = int(input("Please enter the price of the item: "))
category = input("Please enter the item category: ")
quantity = int(input("Please enter the quantity: "))

a = StockItem(item_name, price, category)
print(a.add_stock())
print(a.item_id)
print(a.price)
print(a.category)
print(a.item_name)
        




