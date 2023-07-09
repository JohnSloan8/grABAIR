from models.nouns import POSNoun, POSDefaultNoun


def populate_noun_object(unmodified_word, default_word, lenition, eclipsed, prefixT, prefixH, word_data, default_nouns_dict):

    default_noun = default_nouns_dict.get(default_word)
    if default_noun is not None:

        declension = None
        disambig = None
        isProper = None
        isImmutable = None
        isDefinite = None
        allowArticledGenitive = None

        if 'declension' in default_noun:
            declension = default_noun['declension']
        if 'disambig' in default_noun:
            disambig = default_noun['disambig']
        if 'isProper' in default_noun:
            isProper = default_noun['isProper']
        if 'isImmutable' in default_noun:
            isImmutable = default_noun['isImmutable']
        if 'isDefinite' in default_noun:
            isDefinite = default_noun['isDefinite']
        if 'allowArticledGenitive' in default_noun:
            allowArticledGenitive = default_noun['allowArticledGenitive']

        default_noun_object = POSDefaultNoun(
            word=default_word,
            declension=declension,
            disambig=disambig,
            isProper=isProper,
            isImmutable=isImmutable,
            isDefinite=isDefinite,
            allowArticledGenitive=allowArticledGenitive
        )

        number = None
        case = None
        gender = None
        strength = None

        if 'number' in word_data:
            number = word_data['number']
        if 'case' in word_data:
            case = word_data['case']
        if 'gender' in word_data:
            gender = word_data['gender']
        if 'strength' in word_data:
            strength = word_data['strength']

        noun_object = POSNoun(
            word=word_data['word'],
            unmodified_word=unmodified_word,
            default=default_noun_object,
            number=number,
            case=case,
            gender=gender,
            strength=strength,
            lenition=lenition,
            eclipsed=eclipsed,
            prefixT=prefixT,
            prefixH=prefixH
        )

        return noun_object
    else:
        return None
