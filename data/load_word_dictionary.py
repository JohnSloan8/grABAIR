import json
from config import ROOT_DIR
import os
from utils.decorators.timer import timer


@timer
def load_word_dictionary():

    with open(os.path.join(ROOT_DIR, 'data',  'wordObjectDictionary.json')) as f:
        all_words_dict = json.load(f)
        
    with open(os.path.join(ROOT_DIR, 'data', 'defaults', 'nouns_default.json')) as f:
        default_nouns_dict = json.load(f)

    with open(os.path.join(ROOT_DIR, 'data', 'defaults', 'adjectives_default.json')) as f:
        default_adjectives_dict = json.load(f)

    with open(os.path.join(ROOT_DIR, 'data', 'defaults', 'possessives_default.json')) as f:
        default_possessives_dict = json.load(f)

    with open(os.path.join(ROOT_DIR, 'data', 'defaults', 'prepositions_default.json')) as f:
        default_prepositions_dict = json.load(f)

    with open(os.path.join(ROOT_DIR, 'data', 'defaults', 'pronouns_default.json')) as f:
        default_pronouns_dict = json.load(f)

    with open(os.path.join(ROOT_DIR, 'data', 'defaults', 'verbs_default.json')) as f:
        default_verbs_dict = json.load(f)

    return all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict