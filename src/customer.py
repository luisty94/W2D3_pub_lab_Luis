
class Customer:

    def __init__(self, name, age, drunkenness, wallet):
        self.name = name
        self.age = age
        self.drunkenness = drunkenness
        self.wallet = wallet
        self.drinks_bought = []

    # def buy_drink(self, drink):
    #     self.wallet -= drink.price
    #     self.drinks_bought.append(drink)

    def buy_drinks(self, drinks):
        for drink in drinks:
            self.wallet -= drink.price
        self.drinks_bought.append(drinks)

    def drink(self, drinks):
        for drink in drinks:
            self.drunkenness += drink.alcohol_level
        return self.drunkenness

    



   
            
