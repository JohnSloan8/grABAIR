from tokenise.word_in_nouns import word_in_nouns
from models.articles import POSArticle
from models.general import POSWord
from utils.word_lists import vowels, consonants_take_seimhu, letters_after_s_not_prefixed_by_t

def create_word_object_list(words):

    word_objects = []
    for i, word in enumerate(words):
        number = 'sg'
        if word in ["an", "na"]:
            if word == "an":
                number = "pl"
            article = POSArticle(word=word, number=number)
            word_objects.append(article)
        else:
            # noun
            base_word = word
            eclipsed = False
            prefix_t = False
            prefix_h = False


            # is there a seimhu?
            if word[0] in consonants_take_seimhu and word[1] == "h":
                eclipsed = True
                base_word = word[0] + word[2:]

            # is there a t before an s
            if word[:2] == "t-" and word[2] not in letters_after_s_not_prefixed_by_t and word[2] not in vowels:
                prefix_t = True
                base_word = word[2:]

            # check if in nouns
            nouns = word_in_nouns(word, base_word, eclipsed, prefix_t)
            if len(nouns) > 0:
                word_objects.append(nouns)
            else:   
                word_objects.append(POSWord(word=word))

    return word_objects


if __name__ == "__main__":
    create_word_object_list(["an", "ádh", "mór"])
