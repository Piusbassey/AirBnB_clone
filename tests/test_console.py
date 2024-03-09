import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
            self.assertIn("EOF  help  quit", output)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(output)

    # Add more test cases for other console commands here

if __name__ == '__main__':
    unittest.main()
