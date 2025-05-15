from random import randint

from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain

from utils.writting.writing_template import format_writing1, format_writing2
from utils.writting.prompt import options, PROMPT2
from utils.constant.embedder import embedder
from utils.constant.llm import llm



def get_context(chapter):
  vector_store = FAISS.load_local("data/writing", embedder, allow_dangerous_deserialization=True)
  documents = vector_store.similarity_search(chapter, k=5) 
  context = "\n".join([doc.page_content for doc in documents])
  
  return context


def generate_exercice(prompt, context):
    QA_PROMPT = PromptTemplate.from_template(prompt)
    llm_chain = LLMChain(llm=llm, prompt=QA_PROMPT)

    return llm_chain.run(context=context)


def get_format_writing(chapter):
    i = randint(0,1)

    writing1 = generate_exercice(options[i], chapter)
    writing2 = generate_exercice(PROMPT2, get_context(chapter))

    return "\nWriting : \n\n" + format_writing1(writing1,i) + format_writing2(writing2)
