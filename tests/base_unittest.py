import unittest
import junopy


class BaseTest(unittest.TestCase):
    client_id = "EQ9Y2UmU8OInoywP"
    client_secret = "1mOGjcp,N:?*pV}bAQVqYYB:hm%Bgs6b"
    resource_token = "324DAD7F20FE43BF4FA57950016DCEEC5380D244FA658AE4B63C5B7B93295B50"
    
    def setUp(self):
        junopy.utils.handler_request.authenticate(
            client_id=self.client_id, 
            client_secret=self.client_secret,
            resource_token=self.resource_token,
            sandbox=True
        )