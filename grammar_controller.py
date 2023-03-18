from tokenise.main import tokenise
from grammar_check.main import check_article_noun_gender_number

def grammar_controller(phrase: str, verbose):
    word_list = phrase.split()

    # create a list of list of word objects of all possible words    
    word_objects_list = tokenise(word_list, verbose)

    # for now, just take the first word from each array
    word_object_list = [x[0] for x in word_objects_list]
    
    # print('\n\n --- word_object_list --- \n', word_object_list)

    feedback = check_article_noun_gender_number(word_object_list, verbose)
    
    corrected_word_list = word_list.copy()
    for key in feedback.keys():
        corrected_word_list[key] = feedback[key]
    # # print('corrected_word_list:', corrected_word_list)
    corrected_phrase = ' '.join(corrected_word_list)
    return corrected_phrase

if __name__ == "__main__":
    grammar_controller("an ádh")
