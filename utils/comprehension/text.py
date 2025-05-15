from utils.comprehension.llm import run_ollama
from utils.comprehension.convert_json import convert_to_json
from utils.comprehension.text_template import format_text, format_exercice1, format_exercice2, format_exercice3, format_exercice4_exercice5, format_exercice6
from utils.comprehension.prompt import PROMPT


def format_text_comprehension(json_result):
    format_result = "Text : " + format_text(json_result) + "\n Reading Comprehention : \n"
    comprehension = json_result['comprehension']
    format_result +=  format_exercice1(comprehension) + format_exercice2(comprehension) + format_exercice3(comprehension) + format_exercice4_exercice5(comprehension, '4', ')  refers to : ', 'word') + format_exercice4_exercice5(comprehension, '5', ')  : ', 'synonym') + format_exercice6(comprehension)
    
    return format_result


def get_format_reading_and_questions(chapter_name):
    string_json_result = run_ollama(PROMPT(chapter_name))
    try:
      json_result = convert_to_json(string_json_result)
    except:
      return 'result of text comprehension can\'t convert to json '

    return format_text_comprehension(json_result)