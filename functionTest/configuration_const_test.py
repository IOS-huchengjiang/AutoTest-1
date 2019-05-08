from configuration import const
import unittest

class constTest(unittest.TestCase):
    def test_get__OptionManagerOperator(self):
        # self.assertIsNotNone(const._global_configuration().optionManagerOperator.get("userName"))
        self.assertEqual(const._global_configuration().optionManagerOperator.get("userName"), 'xjd')
        self.assertEqual(const._global_configuration().optionManagerOperator.get("password"), 'xjd12345')


if __name__=='__main__':
    unittest.main()