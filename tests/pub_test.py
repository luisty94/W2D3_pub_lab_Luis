import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):


    def setUp(self):
        self.pub = Pub("Drunks", 1000.00)

    def test_pub_has_name(self):
        self.assertEqual("Drunks", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(1002.50, self.pub.till)

    def test_customer_buys_drink(self):
        self.customer = Customer("Luis", 57, 0, 55.00)
        self.drink_1 = Drink("Pint", 1, 4.50)
        self.customer.buy_drink(self.drink_1.price)
        self.assertEqual(50.50, self.customer.wallet)
        self.pub.increase_till(self.drink_1.price)
        self.assertEqual(1004.50, self.pub.till)

    def test_check_age(self):
        self.customer = Customer("Luis", 57, 0, 55.00)
        customer_is_old_enough = self.pub.check_age(self.customer.age)
        self.assertEqual(True, customer_is_old_enough)

    def test_drunk(self):
        self.customer = Customer("Luis", 57, 0, 55.00)
        self.drink_1 = Drink("Pint", 2, 4.50)
        self.drink_2 = Drink("Larger", 1, 2.00)
        drunkenness = self.customer.drunk(self.drink_1.alcohol_level, self.drink_2.alcohol_level)
        self.assertEqual(3, drunkenness)

    





        