from langchain_ollama import ChatOllama

from brain.configs import config


planning_llm = ChatOllama(
    model=config.OLLAMA_PLANNING_MODEL,
)

execution_llm = ChatOllama(
    model=config.OLLAMA_EXECUTION_MODEL,
)

llm = ChatOllama(
    model=config.OLLAMA_MODEL,
)
