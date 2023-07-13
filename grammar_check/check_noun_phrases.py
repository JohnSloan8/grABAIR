from models.nouns import POSNoun


def check_noun_phrases(sentence):

    indexes_of_nouns = []
    for i, word_object_list in enumerate(sentence):
        for word in word_object_list:
            if type(word) == POSNoun:
                if i not in indexes_of_nouns:
                    indexes_of_nouns.append(i)

    return indexes_of_nouns
