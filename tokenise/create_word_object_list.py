from tokenise.word_in_nouns import word_in_nouns
from models.articles import POSArticle
from models.general import POSWord
from utils.word_lists import vowels, consonants, letters_after_s_not_prefixed_by_t

def create_word_object_list(words):

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
            # noun
            base_word = word
            eclipsed = False
            prefix_t = False
            prefix_h = False


            # is there a seimhu?
            if word[0] in consonants and word[1] == "h":
                eclipsed = True
                base_word = word[0] + word[2:]

            # is there a t before a vowel?
            if word[:2] == "t-" and word[2:] and word[2] in vowels:
                prefix_t = True
                base_word = word[2:]

            # is there a t before a consonant?
            if word[0] == "t" and word[1] in consonants:
                prefix_t = True
                base_word = word[1:]

            # check if in nouns
            nouns = word_in_nouns(word, base_word, eclipsed, prefix_t)
            if len(nouns) > 0:
                word_object.extend(nouns)
            else:   
                word_object.append(POSWord(word=word))
        word_objects.append(word_object)

    return word_objects
