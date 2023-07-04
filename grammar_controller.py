# from tokenise.create_word_object_list import create_word_object_list
# from grammar_check.check_article_noun_gender import check_article_noun_gender_number
import json


with open("./wordData/wordObjectDictionary.json") as json_file:
    wordObjectDictionary = json.load(json_file)

def grammar_controller(phrase: str):
    word_list = phrase.lower().split()
    print('word_list:', word_list)

    word_object_list = []
    for word in word_list:
        if word in wordObjectDictionary:
            word_object_list.append(wordObjectDictionary[word])
        else:
            word_object_list.append([])

    return word_object_list

if __name__ == "__main__":
    grammar_controller("Chonaic mé an bhean bheag ag rith leis")
