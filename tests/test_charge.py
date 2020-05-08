import time
import unittest
from junopy import charge, additional_data
from tests.base_unittest import BaseTest
from tests.resources import charge_data_sample


class TestDigitalAccount(BaseTest):
    def test01_create_charge(self):
        self.__class__._charge = charge.create(params=charge_data_sample.CHARGE)
        self.assertIsNotNone(self.__class__._charge['_embedded']['charges'][0]['id'])

    def test02_list_charge(self):
        all_charges = charge.list()
        self.assertIsNotNone(all_charges)

    def test03_details_charge(self):
        details = charge.details(str(self.__class__._charge['_embedded']['charges'][0]['id']))
        self.assertEqual(self.__class__._charge['_embedded']['charges'][0]['id'], details['id'])

    def test04_cancel_charge(self):
        details = charge.cancel(str(self.__class__._charge['_embedded']['charges'][0]['id']))
        self.assertEqual(details.status_code, 204)

if __name__ == '__main__':
    unittest.main()