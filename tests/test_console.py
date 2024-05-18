import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up the console for testing."""
        self.console = HBNBCommand()

    def test_help_show(self):
        """Test the 'help show' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
            self.assertIn("Show an individual instance of a class", f.getvalue())

    def test_create(self):
        """Test the 'create' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        """Test the 'show' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"show User {user_id}")
                self.assertIn(user_id, f.getvalue())

    def test_destroy(self):
        """Test the 'destroy' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"destroy User {user_id}")
                self.console.onecmd(f"show User {user_id}")
                self.assertIn("** no instance found **", f.getvalue())

    def test_all(self):
        """Test the 'all' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("all User")
                self.assertIn(user_id, f.getvalue())

    def test_update(self):
        """Test the 'update' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd(f"update User {user_id} name \"John Doe\"")
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"show User {user_id}")
                self.assertIn("John Doe", f.getvalue())

    def test_count(self):
        """Test the 'count' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd("count User")
                self.assertEqual(f.getvalue().strip(), "3")

if __name__ == '__main__':
    unittest.main()
