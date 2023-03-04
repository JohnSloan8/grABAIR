from word_in_nouns import word_in_nouns
from models import POSArticle, POSWord
from word_lists import vowels, consonants_take_seimhu, letters_after_s_not_prefixed_by_t

def create_word_object_list(words):

    word_objects = []
    for i, word in enumerate(words):
        if word in ["an", "na"]:
            number = 'sg' if word == "an" else "pl"
            article = POSArticle(word=word, number=number)
            word_objects.append(article)
        else:
            base_word = word
            seimhu = False
            prefix_t = False

            # is there a seimhu?
            if word[0] in consonants_take_seimhu and word[1] == "h":
                seimhu = True
                base_word = word[0] + word[2:]

            # is there a t before an s
            if word[0] == "t" and word[1] not in letters_after_s_not_prefixed_by_t:
                prefix_t = True
                base_word = word[1:]

            # check if in nouns
            nouns = word_in_nouns(base_word, seimhu, prefix_t)
            print('nouns:', nouns)
            if len(nouns) > 0:
                word_objects.append(nouns[0])
            else:   
                word_objects.append(POSWord(word=word))

    return word_objects


if __name__ == "__main__":
    create_word_object_list(["an", "ádh", "mór"])
