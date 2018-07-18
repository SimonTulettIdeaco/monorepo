import unittest
from CoreModule1.app import app

class TestCoreModule1App(unittest.TestCase):
	
	def test_coreModule1_func(self):
		self.assertEqual(app.coreModule1_func(2), 3)


if __name__ == '__main__':
	unittest.main()
	