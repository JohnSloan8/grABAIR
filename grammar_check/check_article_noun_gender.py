from models.articles import POSArticle
from models.nouns import POSNounVariation
from utils.word_lists import vowels, consonants_take_seimhu, letters_after_s_not_prefixed_by_t

def check_article_noun_gender_number(word_object_list):
    print('\n---in check_article_noun_gender---\n')

    feedback = []
    for i, word_objects in enumerate(word_object_list):
        for word_object in word_objects:
            if i > 0 and type(word_object_list[i - 1]) == POSArticle and type(word_object_list[i]) == POSNounVariation:
                if word_object_list[i-1].word == "an":
                    if word_object.gender == "masc":
                        if word_object.case == "nom":
                            if word_object.submitted[0] in vowels:
                                feedback.append("need to add 't-'")
                            if word_object.number == "pl":
                                feedback.append("should be singular")
                        else:
                            feedback.append(f"not nom case. Case is: {word_object.case}")
                    elif word_object.gender == "fem":
                        if word_object.case == "nom":
                            if word_object.submitted[0] in consonants_take_seimhu:
                                if not word_object.eclipsed:
                                    feedback.append("need to add a seimhu")
                            elif word_object.submitted[0] == "s":
                                if not word_object.prefixT:
                                    feedback.append("need to add 't'")
                elif word_object_list[i-1].word == "na":
                    if word_object.case == "nom":
                        if word_object.submitted[0] in vowels:
                            feedback.append("need to add 'h' for plural vowels")
            
    return feedback

if __name__ == "__main__":
    check_article_noun_gender_number(["an", "ádh", "mór"])
