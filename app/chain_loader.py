from app.pattern_loader import patterns

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def __create_chain(content, model):
    return ChatPromptTemplate.from_template(content['system'] + '{text}') | model | StrOutputParser()

def build_chains(model):
    chains = {}
    for label, content in patterns.items():
        chains[label] = __create_chain(content, model)
    return chains