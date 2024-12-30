import unittest
from src.app import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(1, 2), 3) 
        self.assertEqual(app.add(1, -2), -1)
        self.assertEqual(app.add(-1, -2), -3)
        self.assertEqual(app.add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
