from random import randint

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from src.routes.utils.writing_template import get_template_writing1, get_template_writing2

embedder = HuggingFaceEmbeddings()
vector_store = FAISS.load_local(
    "data/writing", embedder, allow_dangerous_deserialization=True
)

llm = Ollama(model="mistral:7b-instruct")


def get_context(vector_store,chapter):
    documents = vector_store.similarity_search(chapter, k=5) 
    
    context = "\n".join([doc.page_content for doc in documents])
    
    return context



biography = """
You are an educational assistant creating writing exercises for high school-level students. Output a valid JSON object.

Follow these instructions when generating the activity:

- Start with this instruction at the top of the task:
  Use the notes below to write a biography of [Full Name].
- Then present bullet-point notes with the following information (choose a notable figure or use the one provided):
 - Birth: City, Country / Date / Nationality
 - Education: Degree / Field / Year / Country or University
 - Field of Interest: Main profession(s) / Special roles / Institutions
 - Awards: Type / Year / Reason(s) / Collaborators (if any)

Do not write the biography. Only provide the instruction and the bullet-point notes.

JSON Format:
{{
    "type": "biography",
    "instructions": "Use the notes below to write a biography of FULL NAME :",
    "notes": {{
      "Birth": "...",
      "Education": "...",
      "Field of interest": "...",
      "Awards": "...",
      "Death": "..."
    }}
}}

Ensure the output is valid JSON. Do NOT include any explanation or extra formatting. Only return the JSON.
context : {context}

"""

Guided = """
You are a high school English writing assistant.

Your task is to generate a **Guided Writing task**. Provide a list of connected notes, key words, or short phrases (at least 5), related to the chapter theme. The student will turn these ideas into a coherent paragraph using their own words. 

- Each note should be 2 to 3 words max.
- All notes should relate logically to a single topic.
- The notes must remain in the given order.
- Do not write complete sentences or explanations.

**style** must match this example:

**Example: Guided Writing**  
Develop the following notes into full sentences by adding what is necessary so as to obtain a coherent paragraph. Do not change the order of the words:  
a) The internet / enable / fast access / information around / world.  
b) It / the cheap / means / accessing / information.  
c) The internet / define / as a tool / link up all / the people / world.  
d) But it can act / weapon / against us.  


---

**CHAPTER**: {context}

JSON Format:
{{
    "type": "Guided Writing",
    "instructions": "Develop the following notes into full sentences by adding what is necessary so as to obtain a coherent paragraph. Do not change the order of the words.",
    "notes": {{
      "a": "list of words of each notes of sentence a without related words like (for,to ,at)",
      "b": "list of words of each notes of sentence b without related words like (for,to ,at)",
      "c": "list of words of each notes of sentence c without related words like (for,to ,at)",
      "d": "list of words of each notes of sentence d without related words like (for,to ,at)"
    }}
}}

Ensure the output is valid JSON. Do NOT include any explanation or extra formatting. Only return the JSON.

"""

prompt2 = """
You are an expert English exam writer.

Your task is to generate **one writing exam prompt** for high school students, based on set of **retrieved example documents**, 
each containing a short writing prompt already used in exams.

Follow these rules strictly:

- The writing task must be either:
  - a **letter** (formal or informal), or
  - an **article** (for a school newspaper, magazine, or blog).

- The prompt must:
  - Clearly relate to the **theme of the chapter**
  - Be **short, clear, and simple (between 15 and 30 words)** — no sub-points, no bullet lists, no long explanations
  - Be suitable for high school level writing
  - Be inspired by the **retrieved page_content** (without copying or expanding it)
  - Don't ask the student to write more than 15 lines in the prompt 

## Do not include:
- Bullet points
- Paragraphs of explanation
- Multiple ideas in one prompt
- Long background stories

---

**Input Example:**

{context}

---

## OUTPUT FORMAT (JSON):
Return the result using this exact structure:

{{"Introduction": Your generated an Introduction for topic here,
  "prompt" : Your generated prompt here
}}

"""

options = [biography,Guided]

def generate(prompt,chapter):
    QA_PROMPT = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(llm=llm, prompt=QA_PROMPT)
    output = llm_chain.run(context=chapter)

    return output

def generate_writing(chapter):
    i = randint(0,1)
    prompt = options[i]
    print(i)

    writing1 = generate(prompt, chapter)
    writing2 = generate(prompt2, get_context(vector_store,chapter))

    template_writing1 = get_template_writing1(writing1,i)
    template_writing2 = get_template_writing2(writing2)

    result = "\nWriting : " + '\n\n' + template_writing1 + '\n\n\n' + template_writing2 + '\n\n'

    return result
