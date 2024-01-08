import unittest
import sys
sys.path.append("..")
from text_processing.create_objects.main import create_objects
from data.load_word_dictionary import load_word_dictionary
from utils.word_lists import vowels, consonants
all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict = load_word_dictionary()

def is_nominative(word_object):
    return word_object.case == 'nom'

def is_noun(word_object):
    return word_object.POS == 'NOUN'

def is_singular(word_object):
    return word_object.number == 'sg'

class TestArticleNounGender(unittest.TestCase):

    # gender : {word: (correct, (incorrect options))}
    test_cases = {
        "feminine": {
            "iris": ("iris", ("t-iris")), # journal
            "bean": ("bhean", ("bean", "tbean")), # woman
            "siúr": ("tsiúr", ("siúr", "shiúr")), # sister
            "deirfiúr": ("deirfiúr", ("dheirfiúr")), # sister
            "tine": ("tine", ("thine"))
        },
        "masculine": {
            "easpag": ("t-easpag", ("easpag")), # bishop
            "bainisteoir": ("bainisteoir", ("bhainisteoir")), # manager
            "sagart": ("sagart", ("tsagart")), # priest
            "duine": ("duine", ("dhuine")), # person
            "tionscadal": ("tionscadal", ("thionscadal")) # project
        }
    }

    def test_article_noun_gender_masculine(self):
        for word, attempts in self.test_cases["masculine"].items():
            word_objects = create_objects(
        [attempts[0]], all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict)
            sing_nom_nouns = [word_object for word_object in word_objects[0] if is_nominative(word_object) and is_noun(word_object) and is_singular(word_object)]
            self.assertEqual(len(sing_nom_nouns), 1)
            
            # got one word which is a noun, singular and nominative
            word_object = sing_nom_nouns[0]
            
            # "start with a vowel should have a t-"
            if word_object.word[0] in vowels:
                self.assertTrue(word_object.prefixT)
            else:
                # all other modifications should be false
                self.assertFalse(word_object.prefixH or word_object.lenition or word_object.eclipsed or word_object.prefixH or word_object.prefixT)
            # if word_object.gender == 'fem':
            #     # "start with a consonant should be lenited"
            #     if word_object.word[0] in consonants:
            #         self.assertTrue(word_object.lenition)
            #     else:
              

    # def test_article_noun_gender_incorrect(self):
    #     for word in self.test_cases["incorrect"]:
    #         word_objects = create_objects(
    #     [word], all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict)
    #         sing_nom_nouns = [word_object for word_object in word_objects[0] if is_nominative(word_object) and is_noun(word_object) and is_singular(word_object)]
    #         self.assertEqual(len(sing_nom_nouns), 1)
            
    #         # got one word which is a noun, singular and nominative
    #         word_object = sing_nom_nouns[0]
            
    #         # masculine
    #         if word_object.gender == 'masc':
    #             # "start with a vowel whould have a t-"
    #             if word_object.word[0] in vowels:
    #                 self.assertFalse(word_object.prefixT)
    #             else:
    #                 self.assertTrue(word_object.prefixH or word_object.lenition or word_object.eclipsed or word_object.prefixH or word_object.prefixT)


if __name__ == '__main__':
    unittest.main()
