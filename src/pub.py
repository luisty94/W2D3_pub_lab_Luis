class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def check_till(self):
        return self.till

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer_age):
        # self.age = customer_age
        return customer_age >= 18