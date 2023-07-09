from utils.word_lists import vowels, seimhus, urus, consonants, letters_after_s_not_prefixed_by_t


def check_modifications(word):
    word = word.lower()
    unmodified_word = word
    modification = None
    lenition = False
    eclipsed = False
    prefixT = False
    prefixH = False

    # is there a seimhu?
    if word[:2] in seimhus and word[:3] != "bhf":
        unmodified_word = word[0] + word[2:]
        modification = "seimhu"
        lenition = True

    # is there an urú?
    # consonant
    if word[:2] in urus:
        unmodified_word = word[1:]
        modification = "uru"
        eclipsed = True

    # bhf and vowels
    if word[:3] == "bhf" and word != "bhfuil" or word[0] == "n" and word[1] == "-" and word[2] in vowels:
        unmodified_word = word[2:]
        modification = "uru"
        eclipsed = True

    # is there a t- before a vowel?
    if word[:2] == "t-" and word[2] in vowels:
        unmodified_word = word[2:]
        modification = "t-vowel"
        prefixT = True

    # is there a t before an s?
    if word[0] == "t" and word[1] == "s" and word[2] not in letters_after_s_not_prefixed_by_t:
        unmodified_word = word[1:]
        modification = "ts"
        prefixT = True

    # is there a h before a vowel?
    if word[:2] == "h-" and word[2] in vowels:
        unmodified_word = word[2:]
        modification = "h-vowel"
        prefixH = True

    return unmodified_word, modification, lenition, eclipsed, prefixT, prefixH
