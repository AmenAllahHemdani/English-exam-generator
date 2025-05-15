from random import choice

from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from utils.languages.language_template import format_exercice1, format_exercice2
from utils.languages.prompt import PROMPT_EXERCICE1, PROMPT_EXERCICE2
from utils.constant.embedder import embedder
from utils.constant.llm import llm
from utils.constant.constant import chapters


def get_random_context(number_of_exercice):
  vector_store = FAISS.load_local("data/language", embedder, allow_dangerous_deserialization=True)
  all_documents = vector_store.similarity_search("", k=78) 
  chapter = choice(chapters)
  context_exemple = [doc for doc in all_documents if doc.metadata.get("ex") == number_of_exercice and doc.metadata.get("chap") == chapter][:5]
  
  return "\n".join([doc.page_content for doc in context_exemple])   


def generate_exercice(prompt,number_of_exercice):
    context = get_random_context(number_of_exercice)
    QA_PROMPT = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(llm=llm, prompt=QA_PROMPT)

    return llm_chain.run(context=context)


def get_format_languages():
    exercice1 = generate_exercice(PROMPT_EXERCICE1, "ex1")
    exercice2 = generate_exercice(PROMPT_EXERCICE2, "ex2")

    return "\nLanguages : \n\n" + format_exercice1(exercice1) + format_exercice2(exercice2)