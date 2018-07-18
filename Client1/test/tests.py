import unittest
from Client1.app import app

class TestClient1App(unittest.TestCase):
	
	def test_client1_func(self):
		self.assertEqual(app.client1_func(2), 3)


if __name__ == '__main__':
	unittest.main()
	