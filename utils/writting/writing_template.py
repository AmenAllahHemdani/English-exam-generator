import json


blank = '.............................................................'


def format_writing1(output,topic):
    json_result = json.loads(output)

    result = '1) ' + json_result['type'] + '\n ' + json_result['instructions'] + '\n\n'

    for item, value in json_result['notes'].items():

        if topic == 1:
            result += "  " + item + ') ' + ' | '.join(value) + '\n'
        else:
            result += "  " + item + ' : ' + value + '\n'
    
    return result + ("\n" + blank) * 5 + '\n\n\n' 


def format_writing2(output):
    json_result = json.loads(output)

    return "2)Free Writing : \n Topic : " + json_result['Introduction'] + "\n " + json_result['prompt'] + ("\n" + blank) * 17 + '\n\n' 
