import json
from models.nouns import POSNoun
from config import ROOT_DIR
import os

f = open(os.path.join(ROOT_DIR, 'wordData', 'defaults', 'noun_variations.json'))
nouns = json.load(f)


def word_in_nouns(word, base_word, eclipsed=False, prefixT=False, prefix_h=False, plural=False):

    hits = [POSNoun(**x, submitted=word, eclipsed=eclipsed, prefixT=prefixT)
            for x in nouns if x['word'] == base_word]

    if word[0] == "h":
        hits.extend([POSNoun(**x, submitted=word, eclipsed=eclipsed, prefixT=prefixT,
                    prefixH=True) for x in nouns if x['word'] == base_word[1:]])

    return hits
