from unittest import TestCase
import greetings_module

class Test_Greeting(TestCase):
    
    def test_should_say_hello(self):
        result = greetings_module.hello()
        self.assertEqual(result, "Hello!")
    
    def test_should_say_hey(self):
        result = greetings_module.hey()
        self.assertEqual(result, "Hey!")