import re

blank = ".........................................................................."

def format_text(output):
    text = "\n\n"
    for num_paragraph, paragraph in output['reading_text'].items():
        text += num_paragraph + '- ' + paragraph + '\n\n'
    
    return text


def format_exercice1(comprehension):
    exercice1 = comprehension['ex1']
    number = ["a) ","b) ","c) ","d) "]
    options = [num + option + '\n' for num, option in zip(number, exercice1["options"])]

    return '1) ' + exercice1["question"] + '\n  ' + exercice1["prompt"] + '\n  ' + '  '.join(options) + "\n\n"


def format_exercice2(comprehension):
    exercice2 = comprehension['ex2']
    result = '2) ' + exercice2['question'] + '\n'
    for item in ['a','b','c']:
        result += item + ') ' + exercice2[item]['false_statement'] + ". (para " + str(exercice2[item]['num_paragraph']) + ') : \n' + blank + "\n"

    return result + '\n'


def format_exercice3(comprehension):
    exercice3 = comprehension['ex3']
    paragraph = exercice3['paragraph']
    split_paragraph = re.split(r'[.,\s]+', paragraph)
    for word in exercice3['words_choosen']:
        if paragraph.find(word) > -1:
            paragraph = paragraph.replace(word, ' ......... ')
        elif word in split_paragraph:
            paragraph = paragraph.replace(word, ' ......... ')

    return '3) ' + exercice3['question'] + '\n' + paragraph + "\n\n"


def format_exercice4_exercice5(comprehension,number_of_exercice,message,word):
    exercice = comprehension['ex'+number_of_exercice]
    result = number_of_exercice + ') ' + exercice['question'] + '\n'
    for a in ['a','b']:
        result += a + ') ' + exercice[a][word] + '  (para ' + str(exercice[a]['num_paragraph']) + message + blank[:20] + "\n"

    return result + "\n\n"


def format_exercice6(comprehension,blank=blank):
    exercice6 = comprehension['ex6']

    return '6) ' + exercice6['question'] + '\n' + exercice6['prompt'] + '\n' + blank + '\n\n'
