import json
from random import shuffle
from nltk.stem import PorterStemmer

from utils.languages.find_similar_word import find_similar_word


def word_to_base_form(word):
    ps = PorterStemmer()
    return ps.stem(word)


def make_blanks_for_exercice1(words, paragraph):

    for word in words:

        if paragraph.find(word) == -1:
            word = find_similar_word(word, paragraph.split(' '))

        paragraph = paragraph.replace(word, f' ........... ', 1)

    return paragraph


def make_blanks_for_exercice2(words, paragraph):
    for word in words:
        stemming_word = word_to_base_form(word)

        if paragraph.find(word) == -1:
            word = find_similar_word(word, paragraph.split(' '))
            stemming_word = word_to_base_form(word)

        paragraph = paragraph.replace(word, f'({stemming_word}) ......... ', 1)
    
    return paragraph                    


def return_list_of_words(correct,distractors):
    list_of_words = correct + distractors[:2]
    shuffle(list_of_words)

    return [word.lower() for word in list_of_words]


def format_exercice1(output):
    json_result = json.loads(output)

    question = "Fill in the blanks with the words from the list. There are two extra words.\n\n"
    blanks = make_blanks_for_exercice1(json_result['correct_words'], json_result['paragraph'])
    list_of_words = return_list_of_words(json_result['correct_words'], json_result['distractors'])

    return '1) ' + question + '  Words :   | ' + ' | '.join(list_of_words) + ' | \n\n ' + blanks + '\n\n\n'


def format_exercice2(output):
    json_result = json.loads(output)

    blank = make_blanks_for_exercice2(json_result['words'], json_result['paragraph'])

    return '2) ' + json_result['question'] + '\n\n ' + blank + '\n\n\n'