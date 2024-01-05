import unittest
import sys
sys.path.append("..")
from text_processing.tokenise.main import tokenise


class TestTokenise(unittest.TestCase):

    test_cases = [("an bhean bheag", ["an", "bhean", "bheag"])]

    def test_tokenise(self):
        for test_case in self.test_cases:
            tokenised = tokenise(test_case[0])
            self.assertEqual(test_case[1], tokenised)

if __name__ == '__main__':
    unittest.main()
