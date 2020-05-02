import unittest
from palindrome_permutation import *


class Test(unittest.TestCase):

    dataT = ['ab bbd ad', 's4fadf4ds', 'baccb','tactcoa']
    dataF = ['23ds2', 'hb 627jh=j ()','abcdefghiqwkw','cs']

    def test_true(self):

        # true check
        for test_string in self.dataT:
            result = is_palindrome_permutation(test_string)
            self.assertTrue(result)

        # false check
        for test_string in self.dataF:
            result = is_palindrome_permutation(test_string)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()