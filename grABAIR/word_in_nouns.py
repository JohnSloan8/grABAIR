import json
from models import POSNoun

f = open('./wordData/nouns.json')
nouns = json.load(f)

def word_in_nouns(word, seihmu=False, prefixT=False):
    # bare word
    hits = [POSNoun(**x) for x in nouns if x['word'] == word]

    if (len(hits) == 1):
        if seihmu:
            hits[0].eclipsed=True
        elif prefixT:
            hits[0].prefixT=True
    else:
        print('\n\ngot no hits for nouns\n\n')

    return hits
    