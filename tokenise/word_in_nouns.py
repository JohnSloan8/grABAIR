import json
from models.nouns import POSNounVariation

f = open('./wordData/noun_variations.json')
nouns = json.load(f)

def word_in_nouns(word, base_word, eclipsed=False, prefixT=False, prefix_h=False, plural=False):

    hits = [POSNounVariation(**x, submitted=word, eclipsed=eclipsed, prefixT=prefixT) for x in nouns if x['word'] == base_word]

    if word[0] == "h":
        hits.extend([POSNounVariation(**x, submitted=word, eclipsed=eclipsed, prefixT=prefixT, prefixH=True) for x in nouns if x['word'] == base_word[1:]])
    
    print(f'got {len(hits)} hits for nouns for: {word}')

    return hits
    