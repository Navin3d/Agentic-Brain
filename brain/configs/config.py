from dotenv import load_dotenv
load_dotenv(verbose=True)
import os


ATLASSIAN_URL=os.environ.get("ATLASSIAN_URL")
ATLASSIAN_USERNAME=os.environ.get("ATLASSIAN_USERNAME")
ATLASSIAN_TOKEN=os.environ.get("ATLASSIAN_TOKEN")

OLLAMA_EXECUTION_MODEL=os.environ.get("OLLAMA_EXECUTION_MODEL", "qwen2.5-coder:14b")
OLLAMA_PLANNING_MODEL=os.environ.get("OLLAMA_PLANNING_MODEL", "deepseek-r1:14b")
OLLAMA_MODEL=os.environ.get("OLLAMA_MODEL", "gemma4:latest")
