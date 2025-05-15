import json

def convert_to_json(string_json):
    clean_json_structure = string_json.replace('\n','').replace('\'','`').strip()

    return json.loads(clean_json_structure)

 