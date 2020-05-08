import time
import unittest
from junopy import card
from tests.base_unittest import BaseTest
from tests.resources import card_data_sample


class TestDigitalAccount(BaseTest):
    def test01_tokenize_card(self):
        self.__class__.card = card.tokenize(params=card_data_sample.CARD)
        self.assertIsNotNone(self.__class__.card['id'])

if __name__ == '__main__':
    unittest.main()