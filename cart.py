class Cart:
    def __init__(self, name, price,quantity, description):
        self.name = name
        self.price=price
        self.quantity=quantity
        self.description=description
    

    def update_item(self,name,price,quantity,description):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.description=description
        print("Items Updated Successfully")
    
    def info(self):
        print("Item Name:",self.name)
        print("Quantity:",self.quantity)
        print("price:",self.price)
        print("description:",self.description)

mobile=Cart("apple",120500,10,"17 pro max with 128gb storage")

laptop=Cart("dell",95000,5,"dell i5 generation")



mobile.update_item("iphone 17promax",165000,15,"17pro max with 516gb")
mobile.info()
