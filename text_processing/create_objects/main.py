from utils.decorators.timer import timer
from .check_modifications import check_modifications
from .populate_objects.populate_noun_object import populate_noun_object
from .populate_objects.populate_adjective_object import populate_adjective_object
from .populate_objects.populate_verb_object import populate_verb_object
from .populate_objects.populate_verbal_noun_object import populate_verbal_noun_object
from .populate_objects.populate_verbal_adjective_object import populate_verbal_adjective_object
from .populate_objects.populate_mood_object import populate_mood_object
from .populate_objects.populate_possessive_object import populate_possessive_object
from .populate_objects.populate_pronoun_object import populate_pronoun_object
from .populate_objects.populate_preposition_object import populate_preposition_object
from .populate_objects.populate_article_object import populate_article_object


@timer
def create_objects(tokenised_input, all_words_dict, default_nouns_dict, default_adjectives_dict, default_possessives_dict, default_prepositions_dict, default_pronouns_dict, default_verbs_dict):
    sentences_object_list = []
    for sentence in tokenised_input:
        sentence_object_list = []
        for word in sentence:
            word_object_list = []

            if word in ["an", "na"]:
                word_object = populate_article_object(word)
                word_object_list.append(word_object)

            unmodified_word, modification, lenition, eclipsed, prefixT, prefixH = check_modifications(
                word)
            word_data_from_dict = all_words_dict.get(unmodified_word)
            if word_data_from_dict is not None:
                for word_data in word_data_from_dict:
                    print('word_data:', word_data)
                    word_object = None
                    if word_data['type'] == 'noun':
                        word_object = populate_noun_object(
                            unmodified_word, word_data['default'], lenition, eclipsed, prefixT, prefixH, word_data, default_nouns_dict)
                    elif word_data['type'] == 'adjective':
                        word_object = populate_adjective_object(
                            unmodified_word, word_data['default'], lenition, word_data, default_adjectives_dict)
                    elif word_data['type'] == 'verb':
                        word_object = populate_verb_object(
                            unmodified_word, word_data['default'], lenition, eclipsed, word_data, default_verbs_dict)
                    elif word_data['type'] == 'verbal noun':
                        word_object = populate_verbal_noun_object(
                            word_data['default'], word_data, default_verbs_dict)
                    elif word_data['type'] == 'verbal adjective':
                        word_object = populate_verbal_adjective_object(
                            word_data['default'], word_data, default_verbs_dict)
                    elif word_data['type'] == 'mood':
                        word_object = populate_mood_object(
                            word_data['default'], word_data, default_verbs_dict)
                    elif word_data['type'] == 'possessive':
                        word_object = populate_possessive_object(
                            word_data['default'], word_data, default_possessives_dict)
                    elif word_data['type'] == 'pronoun':
                        word_object = populate_pronoun_object(
                            word_data['default'], word_data, default_pronouns_dict)
                    elif word_data['type'] == 'preposition':
                        word_object = populate_preposition_object(
                            word_data['default'], word_data, default_prepositions_dict)
                    if word_object is not None:
                        word_object_list.append(word_object)
            sentence_object_list.append(word_object_list)
        sentences_object_list.append(sentence_object_list)
    return sentences_object_list
