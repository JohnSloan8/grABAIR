from models.possessives import POSPossessive, POSDefaultPossessive


def populate_possessive_object(default_word, word_data, default_possessives_dict):

    default_possessive = default_possessives_dict.get(default_word)

    if default_possessive is not None:
        disambig = None
        mutation = None
        emphasizer = None
        full = None
        apos = None

        if 'disambig' in default_possessive:
            disambig = default_possessive['disambig']
        if 'mutation' in default_possessive:
            mutation = default_possessive['mutation']
        if 'emphasizer' in default_possessive:
            emphasizer = default_possessive['emphasizer']
        if 'full' in default_possessive:
            full = default_possessive['full']
        if 'apos' in default_possessive:
            apos = default_possessive['apos']

        default_possessive_object = POSDefaultPossessive(
            word=default_word,
            disambig=disambig,
            mutation=mutation,
            emphasizer=emphasizer,
            full=full,
            apos=apos
        )

        number = None
        gender = None
        form = None

        if 'number' in word_data:
            number = word_data['number']
        if 'gender' in word_data:
            gender = word_data['gender']
        if 'form' in word_data:
            form = word_data['form']

        possessive_object = POSPossessive(
            word=word_data['word'],
            default=default_possessive_object,
            number=number,
            gender=gender,
            form=form
        )

        return possessive_object

    else:

        return None
