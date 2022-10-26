import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):


    def setUp(self):
        self.drink = Drink("Pint", 1, 4.50)

    def test_drink_name(self):
        self.assertEqual("Pint", self.drink.name)
        self.assertEqual(4.50, self.drink.price)