from models.verbs import POSVerbalNoun, POSDefaultVerb


def populate_verbal_noun_object(default_word, word_data, default_verbs_dict):

    default_verb = default_verbs_dict.get(default_word)

    if default_verb is not None:
        disambig = None

        if 'disambig' in default_verb:
            disambig = default_verb['disambig']

        default_verb_object = POSDefaultVerb(
            word=default_word,
            disambig=disambig,
        )

        verbal_noun_object = POSVerbalNoun(
            word=word_data['word'],
            default=default_verb_object,
        )

        return verbal_noun_object

    else:

        return None
