import unittest
from grammar_controller import grammar_controller

class TestDefArticleNounGender(unittest.TestCase):

  words_to_test = {
    "t-easpag": ["easpag"], 
    "bainisteoir": ["bhainisteoir"], 
    "sagart": ["tsagart", "shagart"], 
    "duine": ["dhuine"], 
    "tionscadal": ["dtionscadal", "thionscadal"], 
    "iris": ["t-iris"], 
    "bhean": ["bean"], 
    "tsiúr": ["siúr"], 
    "deirfiúr": ["dheirfiúr"], 
    "tine": ["thine"]
  }
  def test_def_article_noun_gender_correct(self):
    for key in self.words_to_test:
      print('key: ', key)
      self.assertEqual(grammar_controller("an " + key), "an " + key)

  # def test_def_article_noun_gender_incorrect(self):
  #   for key, val in self.words_to_test.items():
  #     for word in val:
  #       self.assertEqual(grammar_controller("an " + word), "an " + key)

if __name__ == '__main__':
  unittest.main()