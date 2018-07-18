import unittest
from Client2.app import app

class TestClient2App(unittest.TestCase):
	
	def test_client2_func(self):
		self.assertEqual(app.client2_func(2), 3)


if __name__ == '__main__':
	unittest.main()
	