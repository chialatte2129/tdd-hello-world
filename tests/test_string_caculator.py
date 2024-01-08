from unittest import TestCase
from tdd_hello_world import string_caculator

class Test_String_Caculator(TestCase):
    
    def test_should_return_zero(self):
        result = string_caculator.run("")
        self.assertEqual(result, 0)
    
    def test_should_return_4(self):
        result = string_caculator.run("4")
        self.assertEqual(result, 4)

    def test_should_return_3(self):
        result = string_caculator.run("1,2")
        self.assertEqual(result, 3)

    def test_should_return_45(self):
        result = string_caculator.run("1,2,3,4,5,6,7,8,9")
        self.assertEqual(result, 45)

    def test_should_return_6_with_newline(self):
        result = string_caculator.run("1\n2,3")
        self.assertEqual(result, 6)

    def test_should_return_3_with_customer_separator(self):
        result = string_caculator.run("//;\n1;2")
        self.assertEqual(result, 3)
    
    def test_should_return_3_with_customer_separator(self):
        result = string_caculator.run("1,-1,-3")
        self.assertEqual(result, 3)
    

  