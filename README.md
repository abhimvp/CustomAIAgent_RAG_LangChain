# CustomAIAgent_RAG_LangChain

- build your own custom AI agent with Python using Retrieval Augmented Generation (RAG) and LangChain.
- Learning from TechWithTim Youtube channel

# what we do here?

- Query information about one of github repositories
- make an AI Agent that acts like a coding or github assistant
  ![alt text](images/image.png)
  ![alt text](images/image-1.png)

# Installation/Setup

- Create a virtual environment to install the various packages that we need - `python -m venv github` - github is name of our virtual environment
- activate the virtual environment - `source github/scripts/activate` - windows cmd - for mac it is - `source github/bin/activate` & we see github prefix in our terminal as follows

```
(github)
abhis@Tinku MINGW64 ~/Desktop/AIAgents/CustomAIAgent_RAG_LangChain (main)
$
```

- let's install different packages:
  - `python-dotenv` for loading in environment variables
  - `requests` module to send requests to github API to get different issues
  - `langchain` package - to write our agent
  - `langchain-astradb` - use this as vector store provider
  - `google_generativeai`
  - `langchainhub`
  - command - `pip install python-dotenv requests langchain langchain-astradb google_generativeai langchainhub`
