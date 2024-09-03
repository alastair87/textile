def load_model(service, name, base_url=None):
    if service == 'openai':
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=name) if base_url is None else ChatOpenAI(model=name, base_url=base_url)
    elif service == 'ollama':
        from langchain_community.chat_models import ChatOllama
        return ChatOllama(model=name) if base_url is None else ChatOllama(model=name, base_url=base_url)
    else:
        raise Exception('Invalid service')