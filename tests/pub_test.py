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
        self.drink_1 = Drink("Pint", 1, 4.50)
        self.pub.increase_till([self.drink_1])
        self.assertEqual(1004.50, self.pub.till)

    def test_customer_buys_drink(self):
        self.customer = Customer("Luis", 57, 0, 55.00)
        self.drink_1 = Drink("Pint", 1, 4.50)
        self.drink_2 = Drink("Larger", 1, 2.00)
        self.customer.buy_drinks([self.drink_1, self.drink_2])
        self.assertEqual(48.50, self.customer.wallet)
        self.pub.increase_till([self.drink_1, self.drink_2])
        self.assertEqual(1006.50, self.pub.till)

    def test_check_age(self):
        self.customer = Customer("Luis", 57, 0, 55.00)
        customer_is_old_enough = self.pub.check_age(self.customer.age)
        self.assertEqual(True, customer_is_old_enough)

    def test_drunk(self):
        self.customer = Customer("Luis", 57, 0, 55.00)
        self.drink_1 = Drink("Pint", 2, 4.50)
        self.drink_2 = Drink("Larger", 1, 2.00)
        self.customer.drink([self.drink_1, self.drink_2])
        self.assertEqual(3, self.customer.drunkenness)

    def test_serve_drinks(self):
        self.customer = Customer("Luis", 57, 0, 55.00)
        self.drink_1 = Drink("Pint", 2, 4.50)
        self.drink_2 = Drink("Larger", 1, 2.00)
        self.pub.serve_drinks(self.customer,[self.drink_1, self.drink_2])
        self.assertEqual(48.50, self.customer.wallet)

    def test_serve_drinks_refuse(self):
        self.customer = Customer("Ewa", 68, 16, 20.00)
        self.drink_3 = Drink("Sherry", 3, 4.00)
        self.pub.serve_drinks(self.customer, self.drink_3)
        self.assertEqual(20.00, self.customer.wallet)


    





        