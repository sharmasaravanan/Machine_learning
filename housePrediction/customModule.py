class D:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def display(self):
        print("You bought %s item" % self.item)

    def calculation(self, price):
        self.price = price
        print("Your bill amount for the item %s is %f" %
              (self.item, self.quantity * self.price))
