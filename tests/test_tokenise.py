import unittest
import sys
sys.path.append("..")
from text_processing.tokenise.main import tokenise, tokenise_sentences, tokenise_words


class TestTokenise(unittest.TestCase):

    test_cases = {
        "tokenise words": [("an bhean bheag", ["an", "bhean", "bheag"])],
        "tokenise sentences":  [("an bhean bheag. Chonaic mé mo mhala", ["an bhean bheag",  "Chonaic mé mo mhala"])],
        "tokenise": [("an bhean bheag. Chonaic mé mo mhala", [["an", "bhean", "bheag"],  ["Chonaic", "mé", "mo",  "mhala"]])]
    }

    def test_tokenise_words(self):
        for words in self.test_cases["tokenise words"]:
            tokenised_words = tokenise_words(words[0])
            self.assertEqual(words[1], tokenised_words)

    def test_tokenise_sentences(self):
        for sentences in self.test_cases["tokenise sentences"]:
            tokenised_sentences = tokenise_sentences(sentences[0])
            self.assertEqual(sentences[1], tokenised_sentences)

    def test_tokenise(self):
        for text in self.test_cases["tokenise"]:
            tokenised = tokenise(text[0])
            self.assertEqual(text[1], tokenised)

if __name__ == '__main__':
    unittest.main()
