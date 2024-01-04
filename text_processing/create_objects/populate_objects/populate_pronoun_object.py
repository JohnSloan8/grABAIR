from models.pronouns import POSPronoun, POSDefaultPronoun


def populate_pronoun_object(default_word, word_data, default_pronouns_dict):

    default_pronoun = default_pronouns_dict.get(default_word)

    if default_pronoun is not None:
        nom = None
        acc = None

        if 'nom' in default_pronoun:
            nom = default_pronoun['nom']
        if 'acc' in default_pronoun:
            acc = default_pronoun['acc']

        default_pronoun_object = POSDefaultPronoun(
            word=default_word,
            nom=nom,
            acc=acc
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

        pronoun_object = POSPronoun(
            POS="PRONOUN",
            word=word_data['word'],
            number=number,
            gender=gender,
            form=form,
            default=default_pronoun_object
        )

        return pronoun_object

    else:

        return None
