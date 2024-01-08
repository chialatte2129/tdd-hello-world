from unittest import TestCase
from tdd_hello_world import leap_year

class Test_Leap_Year(TestCase):
    
    def test_should_is_not_leap_year(self):
        result = leap_year.run(5)
        self.assertEqual(result, "is not")
    
    def test_should_be_leap_year(self):
        result = leap_year.run(4)
        self.assertEqual(result, "is")

    def test_should_not_be_leap_year_by_a_hundred(self):
        result = leap_year.run(200)
        self.assertEqual(result, "is not")

    def test_should_not_be_leap_year_by_four_hundred(self):
        result = leap_year.run(400)
        self.assertEqual(result, "is")

    def test_should_not_be_leap_year_by_1997(self):
        result = leap_year.run(1997)
        self.assertEqual(result, "is not")
    
    def test_should_be_leap_year_by_1996(self):
        result = leap_year.run(1996)
        self.assertEqual(result, "is")
    
    def test_should_be_leap_year_by_1600(self):
        result = leap_year.run(1600)
        self.assertEqual(result, "is")

    def test_should_not_be_leap_year_by_1800(self):
        result = leap_year.run(1800)
        self.assertEqual(result, "is not")