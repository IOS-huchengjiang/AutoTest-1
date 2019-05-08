from baseLib.operationManagerAPI import authentication
import unittest
from configuration import const

class authenticationTest(unittest.TestCase):
    def test001(self):
        returnTuple = authentication.login(const._global_configuration().optionManagerOperator)
        print(returnTuple)
