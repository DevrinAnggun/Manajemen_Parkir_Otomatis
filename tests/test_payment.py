import unittest
from src.payment import Payment

class TestPayment(unittest.TestCase):
    def test_process_payment(self):
        result = Payment.process_payment(5000, "e-wallet")
        self.assertEqual(result, "Payment of 5000 processed via e-wallet")

if __name__ == '__main__':
    unittest.main()
