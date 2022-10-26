 
class Customer:

    def __init__(self, name, age, drunkenness, wallet):
        self.name = name
        self.age = age
        self.drunkenness = drunkenness
        self.wallet = wallet
        self.drinks_bought = []

    def buy_drink(self, price):
        self.wallet -= price

    def drunk(self, alcohol_consumed):
        return self.drunkenness + alcohol_consumed



   
            
