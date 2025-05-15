from difflib import SequenceMatcher
from nltk.stem import PorterStemmer


# def similar_strings(to_compare, to_match):
#     to_compare = to_compare.strip()
#     to_match = to_match.strip()
#     return SequenceMatcher(None, to_compare, to_match).ratio()


def word_to_base_form(word):
    ps = PorterStemmer()
    return ps.stem(word)


# def find_similar_word(input_word, word_list):
#     print(input_word)
#     similarities = {}
#     for current_word in word_list:
#         if cuerrent_word not in ['']
#         similarities[current_word] = similar_strings(input_word, current_word)
#     similarities = dict(sorted(similarities.items(),key=lambda x:x[1],reverse=True))
#     print(similarities)
#     if list(similarities.values())[0] <= 0.1:
#         return "Not found"

#     return similarities[0] 

def  find_similar_word(input_word, word_list):
    base_form = word_to_base_form(input_word)
    base_form_list = []
    for word in word_list:
        base_form_list.append(word_to_base_form(word))
    if base_form in base_form_list:
        return word_list[base_form_list.index(base_form)]
    else: 
        return 'not found'
