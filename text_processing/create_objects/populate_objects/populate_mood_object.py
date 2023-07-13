from models.moods import POSMood, POSDefaultMood


def populate_mood_object(default_word, word_data, default_verbs_dict):

    default_verb = default_verbs_dict.get(default_word)

    if default_verb is not None:
        disambig = None

        if 'disambig' in default_verb:
            disambig = default_verb['disambig']

        default_mood_object = POSDefaultMood(
            word=default_word,
            disambig=disambig,
        )

        mood = None
        person = None

        if 'mood' in word_data:
            mood = word_data['mood']
        if 'person' in word_data:
            person = word_data['person']

        mood_object = POSMood(
            word=word_data['word'],
            default=default_mood_object,
            mood=mood,
            person=person
        )

        return mood_object

    else:

        return None
