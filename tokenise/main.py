from tokenise.word_in_nouns import word_in_nouns
from models.articles import POSArticle
from models.general import POSWord
from tokenise.check_modifications import check_modifications

def tokenise(words, verbose):

    word_objects = []
    for i, word in enumerate(words):
        word_object = []
        number = 'sg'
        if word in ["an", "na"]:
            if word == "na":
                number = "pl"
            article = POSArticle(word=word, number=number)
            word_object.append(article)
        else:
            base_word, eclipsed, prefix_t, prefix_h = check_modifications(word)
    
            # check if in nouns
            nouns = word_in_nouns(word, base_word, eclipsed, prefix_t)
            
            if len(nouns) > 0:
                word_object.extend(nouns)
            else:   
                word_object.append(POSWord(word=word))
        word_objects.append(word_object)

    if verbose:
        print('\n\n --- word_objects --- \n', word_objects)

    return word_objects
