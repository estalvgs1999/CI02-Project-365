
import unittest
from is_unique import *


class Test(unittest.TestCase):

    dataT = ['abcd', 's4fad', '','abcdef%@+']
    dataF = ['23ds2', 'hb 627jh=j ()','abcdefghiqwkw','  ']

    def test_unique(self):

        # true check
        for test_string in self.dataT:
            result = is_unique(test_string)
            self.assertTrue(result)
        # false check
        for test_string in self.dataF:
            result = is_unique(test_string)
            self.assertFalse(result)

    def test_unique_nDS(self):
    
        # true check
        for test_string in self.dataT:
            result = is_unique_nDS(test_string)
            self.assertTrue(result)

        # false check
        for test_string in self.dataF:
            result = is_unique_nDS(test_string)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

