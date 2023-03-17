from tokenise.create_word_object_list import create_word_object_list
from grammar_check.check_article_noun_gender import check_article_noun_gender_number

def grammar_controller(phrase: str):
    word_list = phrase.split()
    word_objects_list = create_word_object_list(word_list)
    # for now, just take the first word from each array
    word_object_list = [x[0] for x in word_objects_list]
    print('word_object_list:', word_object_list)
    article_noun_gender_number = check_article_noun_gender_number(word_object_list)
    # print('article_noun_gender_number:', article_noun_gender_number)
    corrected_word_list = word_list.copy()
    for key in article_noun_gender_number.keys():
        corrected_word_list[key] = article_noun_gender_number[key]
    # # print('corrected_word_list:', corrected_word_list)
    corrected_phrase = ' '.join(corrected_word_list)
    return corrected_phrase

if __name__ == "__main__":
    grammar_controller("an ádh")
