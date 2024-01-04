import unittest
import sys
sys.path.append("..")
from text_processing.create_objects.check_modifications import check_modifications

class TestCheckModifications(unittest.TestCase):

    test_cases = {
        "seimhu": {
            "modified": [("bhean", "bean"), ("chat", "cat"), ("dhuit", "duit"), ("fhill", "fill"), ("mhoill", "moill"), ("Phóil", "Póil"), ("shíl", "síl"), ("thoil", "toil")],
            "unmodified": ["bean", "cathair", "bhfuil"],
        },
        "uru": {
            "modified": [("mbó", "bó"), ("gcill", "cill"), ("ndán", "dán"),  ("ngrá", "grá"), ("bpáirc", "páirc"), ("dtig", "tig"), ("n-athair", "athair"), ("n-eilifint", "eilifint"), ("n-ithe", "ithe"), ("n-ól", "ól"), ("n-úll", "úll")],
            "unmodified": ["mmó", "rmil", "adteach"],
        },
        "t-vowel": {
            "modified": [("t-easpag", "easpag"), ("t-úll", "úll"), ("t-iasc", "iasc"), ("t-ocras", "ocras"), ("t-éileamh", "éileamh")],
            "unmodified": ["tbean", "etaspag"],
        },
        "ts": {
            "modified": [("tSeapáin", "Seapáin"), ("tsiúr", "siúr")],
            "unmodified": ["tleic"],
        },
        "h-vowel": {
            "modified": [("h-aghaidh", "aghaidh"), ("h-úll", "úll"), ("h-im", "im"), ("h-ocras", "ocras"), ("h-eilifint", "eilifint")],
            "unmodified": ["h-bean", "ahaghaidh"],
        },
    }

    def test_check_modifications(self):
        for case, judgements in self.test_cases.items():
            for word in judgements["modified"]:
                unmodified_word, modification, lenition, eclipsed, prefixT, prefixH = check_modifications(
                    word[0])
                self.assertEqual(word[1].lower(), unmodified_word)
                self.assertIsNotNone(modification, word)
                if case == "seimhu":
                    self.assertTrue(lenition)
                elif case == "uru":
                    self.assertTrue(eclipsed)
                elif case in ["t-vowel", "ts"]:
                    self.assertTrue(prefixT)
                elif case == "h-vowel":
                    self.assertTrue(prefixH)
            for word in judgements["unmodified"]:
                unmodified_word, modification, lenition, eclipsed, prefixT, prefixH = check_modifications(
                    word)
                self.assertEqual(word, unmodified_word)
                self.assertIsNone(modification, word)
                if case == "seimhu":
                    self.assertFalse(lenition)
                elif case == "uru":
                    self.assertFalse(eclipsed)
                elif case in ["t-vowel", "ts"]:
                    self.assertFalse(prefixT)
                elif case == "h-vowel":
                    self.assertFalse(prefixH)


if __name__ == '__main__':
    unittest.main()
