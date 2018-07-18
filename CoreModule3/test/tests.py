import unittest
from CoreModule3.app import app

class TestCoreModule3App(unittest.TestCase):
	
	def test_coreModule3_func(self):
		self.assertEqual(app.coreModule3_func(2), 3)


if __name__ == '__main__':
	unittest.main()
	