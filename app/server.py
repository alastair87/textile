from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from app.chain_loader import build_chains

from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser

import os

#os.environ["OPENAI_API_KEY"] = ''

# model = ChatOpenAI(model="gpt-4o")

#model = ChatOllama(model="mistral-nemo:latest", num_ctx=32768)

model = ChatOllama(model="mistral-nemo:latest", num_ctx=2048)

chains = build_chains(model)

def meta(model):
    return { 'text': chains['extract_ideas']} | { 'text': chains['extract_wisdom']} | { 'text': chains['extract_insights'] } | { 'text': chains['summarize'] } | chains['summarize'] | model | StrOutputParser()

# print(chains)

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
for label, chain in chains.items():
    add_routes(app, chain, path="/" + label)
# 
add_routes(app, meta(model), path="/meta")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
