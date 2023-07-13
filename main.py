
from fastapi import FastAPI
from text_processing.tokenise.main import tokenise
from text_processing.create_objects.main import create_objects
from data.load_word_dictionary import load_word_dictionary
import json


app = FastAPI()

all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict = load_word_dictionary()


@app.post("/check")
def check(input: str):
    tokenised_input = tokenise(input)
    print('tokenised input:', tokenised_input)
    objects = create_objects(
        tokenised_input, all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict)

    print('objects:', objects)

    return {"objects"}
