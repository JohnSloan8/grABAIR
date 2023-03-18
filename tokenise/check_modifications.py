from utils.word_lists import vowels, consonants

def check_modifications(word):
    base_word = word
    eclipsed = False
    prefix_t = False
    prefix_h = False
    # is there a seimhu?
    if word[0] in consonants and word[1] == "h":
        eclipsed = True
        base_word = word[0] + word[2:]

    # is there a t- before a vowel?
    if word[:2] == "t-" and word[2:] and word[2] in vowels:
        prefix_t = True
        base_word = word[2:]

    # is there a t before a consonant?
    if word[0] == "t" and word[1] in consonants:
        prefix_t = True
        base_word = word[1:]

    return base_word, eclipsed, prefix_t, prefix_h
