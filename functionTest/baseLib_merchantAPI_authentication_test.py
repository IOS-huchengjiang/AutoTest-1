from baseLib.merchantAPI import authentication
import unittest
from configuration import const

class authenticationTest(unittest.TestCase):
    # def test_sendMerchantSMS(self):
    #     returnTuple = authentication.sendMerchantSMS(const._global_configuration().merchantAdmin)
    #     print(returnTuple)

    def test_Login(self):
        returnTuple = authentication.sendMerchantSMS(const._global_configuration().merchantAdmin)
        response = authentication.login(const._global_configuration().merchantAdmin, returnTuple)
        print(response)