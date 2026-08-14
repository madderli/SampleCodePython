import unittest
from HelloWorldApp import get_hello_message

class TestHelloWorldApp(unittest.TestCase):
    def test_get_hello_message(self):
        expected_message = "Hello, World!"
        actual_message = get_hello_message()
        self.assertEqual(actual_message, expected_message)

if __name__ == "__main__":
    unittest.main()