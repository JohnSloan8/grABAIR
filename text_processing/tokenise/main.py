import re
from utils.decorators.timer import timer


sentence_boundaries = r'[.!?]+'
word_boundaries = r'[\s,;]+'
apostrophe_boundaries = r"(m'|d')"


@timer
def tokenise(input):
    apostrophes_split = split_apostrophes(input)
    tokenised_sentences = tokenise_sentences(apostrophes_split)

    tokenised_input = []
    for sentence in tokenised_sentences:
        if sentence == '':
            continue
        else:
            tokenised_sentence = tokenise_words(sentence)
            tokenised_input.append(tokenised_sentence)
    return tokenised_input


def split_apostrophes(input):
    apostrophes_split = re.sub(
        apostrophe_boundaries, r"\1 ", input, flags=re.IGNORECASE)
    return apostrophes_split


def tokenise_sentences(input):
    tokenised_sentences = [t_s.strip()
                           for t_s in re.split(sentence_boundaries, input)]
    return tokenised_sentences


def tokenise_words(sentence):
    tokenised_words = re.split(word_boundaries, sentence)
    return tokenised_words
