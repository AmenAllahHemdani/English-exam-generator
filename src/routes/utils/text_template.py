import re

blank = ".........................................................................."

def text(output):
    text = output['reading_text']
    text = text.replace('1- ', '###').replace('2- ', '###').replace('3- ', '###').replace('4- ', '###').replace('5- ', '###').replace('6- ', '###')
    split_paragraph = text.split(sep='###')
    return '\n\n'.join(split_paragraph)

def ex1(comprehension):
    ex1 = comprehension['ex1']
    number = ["a) ","b) ","c) "]
    options = [num + option +'\n' for num,option in zip(number,ex1["options"])]
    result = '1) '+ex1["question"]+'\n  '+ex1["prompt"]+'\n  '+ '  '.join(options)
    return result

def ex2(comprehension,blanks=blank):
    ex2 = comprehension['ex2']
    result = '2) ' + ex2['question'] +'\n'
    nums = ['a','b','c']
    for item in nums:
        result += item + ') ' + ex2[item]['false_statement'] + ". (para " + str(ex2[item]['num_paragraph']) + ') : \n' + blanks + "\n"
    return result

def ex3(comprehension):
    ex3 = comprehension['ex3']
    paragraph = ex3['paragraph']
    split_paragraph = re.split(r'[.,\s]+', paragraph)
    for word in ex3['correct_answer']:
        if word in split_paragraph:
            paragraph = paragraph.replace(word,' ......... ')
    result = '3) '+ex3['question'] + '\n' + paragraph + "\n"
    return result

def ex4(comprehension,blanks=blank):
    ex4 = comprehension['ex4']
    result = '4) '+ ex4['question']+ '\n'
    for a in ['a','b']:
        result += a + ') ' + ex4[a]['word'] + '  (para ' + str(ex4[a]['num_paragraph']) + ')  refers to : ' + blanks[:20] + "\n"
    return result

def ex5(comprehension,blanks=blank):
    ex5 = comprehension['ex5']
    result = '5) '+ ex5['question']+ '\n'
    for a in ['a','b']:
        result += a + ') ' + ex5[a]['synonym'] + '  (para ' + str(ex5[a]['num_paragraph']) + ')  : ' + blanks[:20] + "\n"
    return result

def ex6(comprehension,blanks=blank):
    ex6 = comprehension['ex6']
    result = '6) '+ex6['question'] + '\n' + blank +'\n\n'
    return result