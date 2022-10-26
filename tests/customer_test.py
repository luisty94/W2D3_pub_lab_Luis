import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):


    def setUp(self):
        self.customer = Customer("Luis", 57, 0, 55.00)
        self.drink_1 = Drink("Pint", 1, 4.50)
        self.drink_2 = Drink("Larger", 1, 2.00)

    def test_customer_name(self):
        self.assertEqual("Luis", self.customer.name)
        self.assertEqual(55.00, self.customer.wallet)

    def test_buy_drink(self):
        self.customer.buy_drink(self.drink_2.price)
        self.assertEqual(53, self.customer.wallet)
