class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def check_till(self):
        return self.till

    def increase_till(self, drinks):
        for drink in drinks:
            self.till += drink.price

    def check_age(self, customer_age):
        # self.age = customer_age
        return customer_age >= 18

    def serve_drinks(self, customer, drinks):
        if customer.drunkenness < 15:
                return customer.buy_drinks(drinks)
        else:
            return "refuse service"


    