import json
import random
from nltk.stem import PorterStemmer


def word_to_base_form(word):
    ps = PorterStemmer()
    stemming = ps.stem(word)

    return stemming


def find_word(paragraph,word):
    word = word.lower()
    paragraph = paragraph.lower()
    i=len(word)-1

    while paragraph.find(word[:i]) == -1 and i>3:
        i-=1
    
    if paragraph.find(word[:i])>-1:
        result = paragraph[paragraph.find(word[:i]):]
        return result[:result.find(' ')]
    else:
        return "not found"


def make_blanks_for_ex1(paragraph,words):

    for word in words:
        if paragraph.find(word)>-1:
            paragraph = paragraph.replace(word,f' ........... ',1)
        else:
            word = find_word(paragraph,word)
            paragraph = paragraph.replace(word,f' ........... ',1)

    return paragraph


def make_blanks_for_ex2(words,paragraph):

    for word in words:
        word = word + ' '

        stemm = word_to_base_form(word.strip())

        if paragraph.find(word)>-1 or paragraph.find(word.strip())>-1:
            paragraph = paragraph.replace(word.strip(),f'({stemm}) ......... ',1)

        else:
            word = find_word(paragraph,word)
            stemm = word_to_base_form(word.strip())
            paragraph = paragraph.replace(word,f'({stemm}) ......... ',1)
    
    return paragraph                    


def return_box(correct,distractors):
    box = correct + distractors[:2]
    random.shuffle(box)
    box = [word.lower() for word in box]

    return box


def generate_ex1(output):
    result_dict = json.loads(output)

    final_result = {'question':"Fill in the blanks with the words from the list. There are two extra words."}

    final_result['Blanks'] = make_blanks_for_ex1(result_dict['paragraph'], result_dict['correct_words'])

    final_result['box'] = return_box(result_dict['correct_words'], result_dict['distractors'])

    result = '1) ' + final_result['question'] + '\n\n  Words :   | ' + ' | '.join(final_result['box']) + ' | \n\n ' + final_result['Blanks']
    
    return result


def generate_ex2(output):
    result_dict = json.loads(output)

    blank = make_blanks_for_ex2(result_dict['words'],result_dict['paragraph'])

    result = '2) ' + result_dict['question'] + '\n\n ' + blank

    return result