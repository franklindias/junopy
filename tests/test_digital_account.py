import time
import unittest
from junopy import digital_account, additional_data
from tests.base_unittest import BaseTest
from tests.resources import digital_account_data_sample


class TestDigitalAccount(BaseTest):
    digital_account = None

    def test01_create_digital_account(self):
        self.__class__._digital_account = digital_account.create(params=digital_account_data_sample.DIGITAL_ACCOUNT)
        self.assertIsNotNone(self.__class__._digital_account['id'])