from models import POSArticle
from word_lists import vowels, consonants_take_seimhu, letters_after_s_not_prefixed_by_t

def check_article_noun_gender(word_object_list):
    print('\n---in check_article_noun_gender---\n')

    feedback = []
    for i, word_object in enumerate(word_object_list):
        if i > 0 and type(word_object_list[i - 1]) == POSArticle:

            if word_object_list[i-1].word == "an":
            print('word_object to check:', word_object)
            if word_object.gender == "masc":
                if word_object.case == "nom":
                    if word_object.word[0] in vowels:
                        feedback.append("need to add 't-'")
                    if word_object.number == "pl":
                        feedback.append("should be singular")
                else:
                    feedback.append("not nom case. Case is:", word_object.case)
            elif word_object.gender == "fem":
                if word_object.case == "nom":
                    if word_object.word[0] in consonants_take_seimhu:
                        if not word_object.eclipsed:
                            feedback.append("need to add a seimhu")
                    elif word_object.word[0] == "s":
                        if not word_object.prefixT:
                            feedback.append("need to add 't'")
        elif word_object_list[i-1].word == "na":
            
    return feedback

if __name__ == "__main__":
    check_article_noun_gender(["an", "ádh", "mór"])
