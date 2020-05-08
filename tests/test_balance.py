import time
import unittest
from junopy import balance
from tests.base_unittest import BaseTest


class TestBalance(BaseTest):
    def test01_get_balance(self):
        _balance = balance.detail()
        self.assertIsNotNone(_balance.get("balance", None))

if __name__ == '__main__':
    unittest.main()