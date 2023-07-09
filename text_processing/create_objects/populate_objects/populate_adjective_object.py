from models.adjectives import POSAdjective, POSDefaultAdjective


def populate_adjective_object(unmodified_word, default_word, lenition, word_data, default_adjectives_dict):

    default_adjective = default_adjectives_dict.get(default_word)

    if default_adjective is not None:
        declension = None
        disambig = None
        sgNom = None
        sgGenMasc = None
        sgGenFem = None
        plNom = None
        graded = None

        if 'declension' in default_adjective:
            declension = default_adjective['declension']
        if 'disambig' in default_adjective:
            disambig = default_adjective['disambig']
        if 'sgNom' in default_adjective:
            sgNom = default_adjective['sgNom']
        if 'sgGenMasc' in default_adjective:
            sgGenMasc = default_adjective['sgGenMasc']
        if 'sgGenFem' in default_adjective:
            sgGenFem = default_adjective['sgGenFem']
        if 'plNom' in default_adjective:
            plNom = default_adjective['plNom']
        if 'graded' in default_adjective:
            graded = default_adjective['graded']

        default_adjective_object = POSDefaultAdjective(
            word=default_word,
            declension=declension,
            disambig=disambig,
            sgNom=sgNom,
            sgGenMasc=sgGenMasc,
            sgGenFem=sgGenFem,
            plNom=plNom,
            graded=graded
        )

        number = None
        case = None
        gender = None
        graded = False

        if 'number' in word_data:
            number = word_data['number']
        if 'case' in word_data:
            case = word_data['case']
        if 'gender' in word_data:
            gender = word_data['gender']
        if 'graded' in word_data:
            graded = word_data['graded']

        adjective_object = POSAdjective(
            word=word_data['word'],
            unmodified_word=unmodified_word,
            default=default_adjective_object,
            number=number,
            case=case,
            gender=gender,
            graded=graded,
            lenition=lenition,
        )

        return adjective_object

    else:

        return None
