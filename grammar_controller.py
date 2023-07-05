# from tokenise.create_word_object_list import create_word_object_list
# from grammar_check.check_article_noun_gender import check_article_noun_gender_number
import json
import pathlib
import os

def grammar_controller(phrase: str):

    current_dir = pathlib.Path(__file__).parent.resolve()
    dictionary_path = "wordData/wordObjectDictionary.json"
    with open(os.path.join(current_dir, dictionary_path)) as json_file:
        wordObjectDictionary = json.load(json_file)

    word_list = phrase.lower().split()


    word_object_list = []
    for word in word_list:
        if word in wordObjectDictionary:
            word_object_list.append(wordObjectDictionary[word])
        else:
            word_object_list.append([])
    print('word_object_list:', word_object_list)
    return word_object_list

if __name__ == "__main__":
    grammar_controller("faca an bean")

