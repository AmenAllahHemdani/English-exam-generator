import ollama

def run_ollama(prompt, model="mistral"):
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']