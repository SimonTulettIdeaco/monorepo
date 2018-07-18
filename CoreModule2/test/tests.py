import unittest
from CoreModule2.app import app

class TestCoreModule2App(unittest.TestCase):
	
	def test_coreModule2_func(self):
		self.assertEqual(app.coreModule2_func(2), 3)


if __name__ == '__main__':
	unittest.main()
	