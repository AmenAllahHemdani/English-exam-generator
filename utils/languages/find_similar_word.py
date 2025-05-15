from nltk.stem import PorterStemmer


def word_to_base_form(word):
    ps = PorterStemmer()
    return ps.stem(word)


def  find_similar_word(input_word, word_list):
    base_form = word_to_base_form(input_word)
    base_form_list = []
    for word in word_list:
        base_form_list.append(word_to_base_form(word))
    if base_form in base_form_list:
        return word_list[base_form_list.index(base_form)]
    else: 
        return 'not found'
