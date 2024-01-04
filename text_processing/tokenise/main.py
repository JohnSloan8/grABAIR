import re
from utils.decorators.timer import timer


sentence_boundaries = r'[.!?]+'
word_boundaries = r'[\s,;:]+'
apostrophe_boundaries = r"(m'|d')"


@timer
def tokenise(input):
    sentence_with_apostrophes_split = split_apostrophes(input)
    tokenised_sentence = tokenise_words(sentence_with_apostrophes_split)
    return tokenised_sentence


def split_apostrophes(input):
    apostrophes_split = re.sub(
        apostrophe_boundaries, r"\1 ", input, flags=re.IGNORECASE)
    return apostrophes_split


def tokenise_words(sentence):
    tokenised_words = re.split(word_boundaries, sentence)
    return tokenised_words
