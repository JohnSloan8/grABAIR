from tokenise.create_word_object_list import create_word_object_list
from grammar_check.check_article_noun_gender import check_article_noun_gender_number

def grammar_controller(word_list):
    word_object_list = create_word_object_list(word_list)
    print('word_object_list:', word_object_list)
    article_noun_gender_number = check_article_noun_gender_number(word_object_list)
    print('article_noun_gender_number:', article_noun_gender_number)


if __name__ == "__main__":
    grammar_controller(["an", "adh", "mór"])
