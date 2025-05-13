from src.routes.utils.llm import run_ollama
from src.routes.utils.convert_json import convert_json
from src.routes.utils.text_template import text, ex1, ex2, ex3, ex4, ex5, ex6

def Text_comprehension(output):
    result = "Text : " + text(output) + "\n\n\n Reading Comprehention : \n"

    comprehension = output['comprehension']

    exercices = [ex1(comprehension),ex2(comprehension),ex3(comprehension),ex4(comprehension),ex5(comprehension),ex6(comprehension)]
    for ex in exercices:
        result += "\n" + ex
    return result


def generate_reading_and_questions(chapter_name, model="mistral"):

    prompt = f"""
You are an educational assistant generating high school-level reading comprehension exercises. Based on a given chapter title, follow the steps below and output the result as a **valid JSON object**. Each part must be under its respective key in the final JSON. Do NOT include markdown or extra text. Only return the JSON.

---

Keys in the final JSON:
Top-Level JSON Keys:
Top-level JSON structure:
{{
  "reading_text": "...",
  "comprehension": {{
    "ex1": {{...}},
    "ex2": {{...}},
    "ex3": {{...}},
    "ex4": {{...}},
    "ex5": {{...}},
    "ex6": {{...}}
  }}
}}
---

STEP 1: Generate a Reading Text
- Write a narrative passage (400-500 words, 5 paragraphs) suitable for high school students.
- The text should reflect someone's personal experience and relate clearly to the given chapter title.
- Use academic English in storytelling form.
- Number each paragraph clearly like this:
  1- ...
  2- ...
  3- ...
  4- ...
  5- ...

---

STEP 2: Create exam-style questions based on the passage:

"ex1":
- Key: "ex1"
- Instructions:
  - Include ONLY THREE options: ONE of them clearly correct and the TWO others are in the same context but they must be not clearly invalid.
  - Write ONLY THREE Options. 
  - Don't give a general options like 'education','school", ...
- Format:
  {{
    "question": "Tick √ the most appropriate option:",
    "prompt": "The text is mainly about:",
    "options": [ "..." , "..." , "..." ]
  }}

"ex2":
- Key: "ex2"
- Write 3 false statements from different paragraphs and give corrected versions with paragraph numbers
- Format:
  {{
    "question": "Correct the following false statements with details from the text:",
    "a": {{
      "false_statement": "...",
      "num_paragraph": ...,
      "correction": "(...)"
    }},
    "b": {{
      "false_statement": "...",
      "num_paragraph": ...,
      "correction": "(...)"
    }},
    "c": {{
      "false_statement": "...",
      "num_paragraph": ...,
      "correction": "(...)"
    }}
  }}

"ex3":
- Key: "ex3"
- Instructions:
  - Add a "question" field: "Complete the following paragraph with 2 words from the text:"
  - Write a new paragraph with 15 words inspired by the text.
  - Choose 2 words from different paragraphs of the text and in the same time this two words include into the new paragraph .
  - The Choosens words must NOT be at the beginning of sentences and must NOT be adjacent, they must be one at the first sentence and the other at the last sentences.
- Format:
  {{
    "question": "Complete the following paragraph with 2 words from the text:",
    "paragraph": (the new paragraph witout blanks) ,
    "correct_answer": ["...", "..."]
  }}

"ex4":
- Key: "ex4"
- Instructions:
  - Select 2 non-obvious one pronouns and one metaphorical words/short sentence from different paragraphs.
  - Avoid simple pronouns like "I" or "he".
- Format:
  {{
    "question": "What do the following words refer to in the text?",
      "a": {{
        "word": "...",
        "num_paragraph": ...,
        "refers_to": "(...)"
      }},
      "b:" {{
        "word": "...",
        "num_paragraph": ...,
        "refers_to": "(...)"
      }}
    ]
  }}

"ex5":
- Key: "ex5"
- Instructions:
  - Select 2 high-level vocabulary words from DIFFERENTS paragraphs in the text.
  - For each, provide ONE synonym that does NOT appear in the text.
  - Don't write more than one word in the synonym, just one.
- Format:
  {{
    "question": "Find words in the text meaning nearly the same as:",
    "a": {{
      "word_in_text": "...",
      "num_paragraph": ...,
      "synonym": "(...)"
    }},
    "b": {{
      "word_in_text": "...",
      "num_paragraph": ...,
      "synonym": "(...)"
    }}
  }}

"ex6":
- Key: "ex6"
- Instructions:
  - The question must be about opinion relatedwith the text like for exemple "if you are in place of ... do you ... ".

- Format:
  {{
    "question": "Give a personal, justified answer to the following question:"
  }}

---

IMPORTANT:
- Leave all student answers as "(...)".
- Ensure that every exercise has a clearly labeled "question" field.
- Ensure that all syntax is valid JSON.
- Return ONLY a single parsable JSON object.

Chapter title: "{chapter_name}"

Ensure the output is valid JSON. Do NOT include any explanation or extra formatting. Only return the JSON.
    
    """

    json_result = run_ollama(prompt, model=model)

    try:
      output = convert_json(json_result)
    except:
      return 'result of text comprehension can\'t convert to json'

    return Text_comprehension(output)
