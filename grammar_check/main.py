from models.articles import POSArticle
from models.nouns import POSNoun
from utils.word_lists import vowels, consonants, letters_after_s_not_prefixed_by_t
import json
# from models.nouns import POSDefaultNoun

f = open('./wordData/default_nouns.json')
default_nouns = json.load(f)

def check_article_noun_gender_number(word_object_list, verbose):
    # print('\n---in check_article_noun_gender---\n')

    feedback = {}
    for i, word_object in enumerate(word_object_list):
        # for word_object in word_objects:
            if i > 0 and type(word_object_list[i - 1]) == POSArticle and type(word_object_list[i]) == POSNoun:
                if word_object_list[i-1].word == "an":
                    if word_object.gender == "masc":
                        if word_object.case == "nom":
                            if word_object.word[0] in vowels:
                                if not word_object.prefixT:
                                    feedback[i] = "t-" + word_object.word
                            elif word_object.number == "pl":
                                feedback[i] = default_nouns[word_object.default]["plNom"]
                            elif word_object.eclipsed:
                                feedback[i] = word_object.word
                            elif word_object.prefixT:
                                feedback[i] = word_object.word
                            # feedback[i] = default_nouns[word_object.default]["sgNom"]
                    elif word_object.gender == "fem":
                        if word_object.case == "nom":
                            if word_object.submitted[0] in consonants and word_object.submitted[0] not in ["d", "t", "s"]:
                                if not word_object.eclipsed:
                                    feedback[i] = word_object.word
                            elif word_object.submitted[0] == "s":
                                if not word_object.prefixT:
                                    feedback[i] = "t" + word_object.word
                elif word_object_list[i-1].word == "na":
                    if word_object.case == "nom":
                        if word_object.submitted[0] in vowels:
                            feedback[i] = "h" + word_object.word
    if verbose:
        print('\n\n --- feedback --- \n', feedback)
    return feedback
