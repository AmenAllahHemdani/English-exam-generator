import json


blank = '.............................................................'


def get_template_writing1(output,topic):
    result_dict = json.loads(output)

    result = '1) ' + result_dict['type'] + '\n ' + result_dict['instructions'] + '\n\n'

    for item, value in result_dict['notes'].items():

        if topic == 1:
            result += "  " + item + ') ' + ' | '.join(value) + '\n'
        else:
            result += "  " + item + ' : ' + value + '\n'
    
    result += ("\n" + blank) * 5
    
    return result


def get_template_writing2(output):
    result_dict = json.loads(output)

    result = "2)Free Writing : " + "\n Topic : " + result_dict['Introduction'] + "\n " + result_dict['prompt'] + "\n"

    result += ("\n" + blank) * 17
    
    return result
