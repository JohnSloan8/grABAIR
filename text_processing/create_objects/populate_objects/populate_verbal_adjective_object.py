from models.verbs import POSVerbalAdjective, POSDefaultVerb


def populate_verbal_adjective_object(default_word, word_data, default_verbs_dict):

    default_verb = default_verbs_dict.get(default_word)

    if default_verb is not None:
        disambig = None

        if 'disambig' in default_verb:
            disambig = default_verb['disambig']

        default_verb_object = POSDefaultVerb(
            word=default_word,
            disambig=disambig,
        )

        verbal_adjective_object = POSVerbalAdjective(
            word=word_data['word'],
            default=default_verb_object,
        )

        return verbal_adjective_object

    else:

        return None
