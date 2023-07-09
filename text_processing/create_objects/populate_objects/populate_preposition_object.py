from models.prepositions import POSPreposition, POSDefaultPreposition


def populate_preposition_object(default_word, word_data, default_prepositions_dict):

    default_preposition = default_prepositions_dict.get(default_word)

    if default_preposition is not None:
        disambig = None
        sg1 = None
        sg2 = None
        sg3Masc = None
        sg3Fem = None
        pl1 = None
        pl2 = None
        pl3 = None

        if 'disambig' in default_preposition:
            disambig = default_preposition['disambig']
        if 'sg1' in default_preposition:
            sg1 = default_preposition['sg1']
        if 'sg2' in default_preposition:
            sg2 = default_preposition['sg2']
        if 'sg3Masc' in default_preposition:
            sg3Masc = default_preposition['sg3Masc']
        if 'sg3Fem' in default_preposition:
            sg3Fem = default_preposition['sg3Fem']
        if 'pl1' in default_preposition:
            pl1 = default_preposition['pl1']
        if 'pl2' in default_preposition:
            pl2 = default_preposition['pl2']
        if 'pl3' in default_preposition:
            pl3 = default_preposition['pl3']

        default_preposition_object = POSDefaultPreposition(
            word=default_word,
            disambig=disambig,
            sg1=sg1,
            sg2=sg2,
            sg3Masc=sg3Masc,
            sg3Fem=sg3Fem,
            pl1=pl1,
            pl2=pl2,
            pl3=pl3
        )

        person = None
        case = None
        gender = None

        if 'person' in word_data:
            person = word_data['person']
        if 'case' in word_data:
            case = word_data['case']
        if 'gender' in word_data:
            gender = word_data['gender']

        preposition_object = POSPreposition(
            word=word_data['word'],
            default=default_preposition_object,
            person=person,
            case=case,
            gender=gender,
        )

        return preposition_object

    else:

        return None
