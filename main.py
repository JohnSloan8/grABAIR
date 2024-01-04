
from fastapi import FastAPI
from text_processing.tokenise.main import tokenise
from text_processing.create_objects.main import create_objects
from data.load_word_dictionary import load_word_dictionary
from grammar_check.check_noun_phrases import check_noun_phrases
import json

app = FastAPI()

all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict = load_word_dictionary()

@app.post("/check")
def check(input: str):
    tokenised_input = tokenise(input)
    print('tokenised input:', tokenised_input)
    sentences_objects = create_objects(
        tokenised_input, all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict)
    print('sentences_objects :', sentences_objects)

    # just first sentence for now to simplify
    NPOutput = check_noun_phrases(sentences_objects[0])
    print('NPOutput :', NPOutput)

    return {
        "tokenised_input:": tokenised_input,
        "sentences_objects:": sentences_objects,
        "NPOutput:": NPOutput
    }
