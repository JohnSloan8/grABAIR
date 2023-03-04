from create_word_object_list import create_word_object_list
from check_article_noun_gender import check_article_noun_gender

def grammar_controller(word_list):
    word_object_list = create_word_object_list(word_list)
    article_noun_gender = check_article_noun_gender(word_object_list)
    print('article_noun_gender feedback:', article_noun_gender)

if __name__ == "__main__":
    grammar_controller(["an", "bean", "mór"])
