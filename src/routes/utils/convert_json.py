import json

def convert_json(output):
    clean_output = output.replace('\n','')
    clean_output = clean_output.replace('\'','`')
    cleaned = clean_output.strip()

    parsed = json.loads(cleaned)

    return parsed