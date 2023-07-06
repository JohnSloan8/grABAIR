from utils.word_lists import vowels, seimhus, urus, consonants

def check_modifications(word):
    base_word = word
    modification = None
    
    # is there a seimhu?
    if word[:2] in seimhus and word[:3] != "bhf":
        base_word = word[0] + word[2:]
        modification = "seimhu"
    
    # is there an urú?
    if word[:2] in urus or word[:3] == "bhf":
        base_word = word[0] + word[2:]
        modification = "uru"

    # is there a t- before a vowel?
    if word[:2] == "t-" and word[2] in vowels:
        base_word = word[2:]
        modification = "t vowel"

    # is there a t before a consonant?
    if word[0] == "t" and word[1] in consonants:
        base_word = word[1:]
        modification = "t consonant"
    
    # is there a h before a vowel?
    if word[0] == "h" and word[1] in vowels:
        base_word = word[1:]
        modification = "h vowel"



    return base_word, modification
