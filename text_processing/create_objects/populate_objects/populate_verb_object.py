from models.verbs import POSVerb, POSDefaultVerb


def populate_verb_object(unmodified_word, default_word, lenition, eclipsed, word_data, default_verbs_dict):

    default_verb = default_verbs_dict.get(default_word)

    if default_verb is not None:
        disambig = None

        if 'disambig' in default_verb:
            disambig = default_verb['disambig']

        default_verb_object = POSDefaultVerb(
            word=default_word,
            disambig=disambig,
        )

        tense = None
        dependency = None
        person = None

        if 'tense' in word_data:
            tense = word_data['tense']
        if 'dependency' in word_data:
            dependency = word_data['dependency']
        if 'person' in word_data:
            person = word_data['person']

        verb_object = POSVerb(
            POS="VERB",
            word=word_data['word'],
            unmodified_word=unmodified_word,
            tense=tense,
            dependency=dependency,
            person=person,
            eclipsed=eclipsed,
            lenition=lenition,
            default=default_verb_object
        )

        return verb_object

    else:

        return None
