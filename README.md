# CustomAIAgent_RAG_LangChain

- build your own custom AI agent with Python using Retrieval Augmented Generation (RAG) and LangChain.
- Learning from TechWithTim Youtube channel

# what we do here?

- Query information about one of github repositories - `https://github.com/techwithtim/Flask-Web-App-Tutorial/issues`
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
  - `langchain-astradb` - use this as vector store db provider comes from datastax
  - `google_generativeai`
  - `langchainhub`
  - command - `pip install python-dotenv requests langchain langchain-astradb google_generativeai langchainhub`
  - `python -m pip install -U black` - python code formatter - shift+alt+F to use
  - `pip freeze > requirements.txt` - store the installed packages/libraries info
  - Important : `pip install -U langchain-google-genai` - to work with Gemini LLM via langchain can be found in langchain documentation : https://python.langchain.com/api_reference/google_genai/index.html#

- let's get different tokens and credentials that we need for this project into `.env` - in this file we store all of the sensitive credentials that we're going to need as we connect to various apis , databases & Gemini Model 1.0 pro
- create a new token in our github profile - https://github.com/settings/tokens
- go to https://astra.datastax.com/ after creating your profile
- We're going to be building a RAG application - Retrieval Augmented Generation
  - Means our AI Agent is going to have access to in this case a database called vector store database & where it can really quickly look up in query information
  - now datastax will be providing that database through their product knows as astra-db - which is a very fast vector db that allows us to really lookup information based on similarity
  - Now AI Agent will utilize this vector database , it's going to query for a certain piece of information & then it can look up based on similarity & then return that data w.r.t query to our model so it can utilize it and give us some results based on it
- The above is basic setup of RAG
  - Usually we are using a vector store database and the way this works is we have vectorized information that allows us to search for information based on
    - context
    - similarity
  - that's much faster and more effiecient than using a traditional sql database
- we need to get all these .env variables :

```
GITHUB_TOKEN="" from https://github.com/settings/tokens
ASTRA_DB_API_ENDPOINT="" from https://astra.datastax.com/
ASTRA_DB_APPLICATION_TOKEN="" from https://astra.datastax.com/
<!-- ASTRA_DB_KEYSPACE="" -->
GOOGLE_API_KEY="" from https://aistudio.google.com/apikey
```

# Fetching Github issues

- `python github.py`

# Connect with llm and vector store and fetch similaritu with our input

# Writing the Agent

- provide the vector store as a tool to the agent & it can decide when it needs to use it
- Build another tool which is a python function which saves the note

# End Result :

```
$ python main.py
C:\Users\abhis\Desktop\AIAgents\CustomAIAgent_RAG_LangChain\github\Lib\site-packages\langchain\_api\module_import.py:87: LangChainDeprecationWarning: Importing GuardrailsOutputParser from langchain.output_parsers is deprecated. Please replace the import with the following:
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
  warnings.warn(
Do you want to update the issues? (y/N): n
Ask a question about github issues (or 'q' to quit): hey can tell me about issues related to flashing messages


> Entering new AgentExecutor chain...

Invoking: `github_search` with `{'query': 'issues related to flashing messages'}`


fix error method=sha256

form update

Update auth.pyfixed new user issue line 58 to pbkdf2:sha256I found one result about issues related to flashing messages: fix error method=sha256.

> Finished chain.
I found one result about issues related to flashing messages: fix error method=sha256.
Ask a question about github issues (or 'q' to quit): hey can tell me about issues related to flash messages


> Entering new AgentExecutor chain...

Invoking: `github_search` with `{'query': 'issues related to flash messages'}`


form update

fix error method=sha256

FLASH MESSAGES NOT SHOWING IN LOGIN PAGEmy auth.py and login.html file doesnt haave any error. the signup page flash messages work but login page flash messages are not showing. and even after pressing login button nothing happens. plss help  I found one result on GitHub related to flash messages:

form update

fix error method=sha256

FLASH MESSAGES NOT SHOWING IN LOGIN PAGE
my auth.py and login.html file doesnt haave any error. the signup page flash messages work but login page flash messages are not showing. and even after pressing login button nothing happens. plss help

> Finished chain.
I found one result on GitHub related to flash messages:

form update

fix error method=sha256

FLASH MESSAGES NOT SHOWING IN LOGIN PAGE
my auth.py and login.html file doesnt haave any error. the signup page flash messages work but login page flash messages are not showing. and even after pressing login button nothing happens. plss help
Ask a question about github issues (or 'q' to quit): hey that's great thanks!


> Entering new AgentExecutor chain...
You're welcome! Is there anything else I can help you with today?

> Finished chain.
You're welcome! Is there anything else I can help you with today?
Ask a question about github issues (or 'q' to quit): can u save a note saying hello world


> Entering new AgentExecutor chain...

Invoking: `note_tool` with `{'note': 'hello world'}`


Note saved successfullyOK. I have saved a note saying hello world. Is there anything else I can help you with?

> Finished chain.
OK. I have saved a note saying hello world. Is there anything else I can help you with?
Ask a question about github issues (or 'q' to quit): hey can you summazrize few issues from github related to Flask and save the summary as a new note


> Entering new AgentExecutor chain...
What do you want me to search for on GitHub?

> Finished chain.
What do you want me to search for on GitHub?
Ask a question about github issues (or 'q' to quit): hey can you summarize a few issues from github related to flask and then s
ave the summary as a new note


> Entering new AgentExecutor chain...

Invoking: `github_search` with `{'query': 'flask'}`
responded: Sure, I can do that.

Let me quickly summarize a few issues from github related to Flask.



form update

Flask Web Dev course

ImportError: cannot import name 'create_app' from 'website'pls help me out
Invoking: `note_tool` with `{'note': 'flask error on form update'}`


Note saved successfullyOk, I have saved a note about the flask error on form update. Anything else?

> Finished chain.
Ok, I have saved a note about the flask error on form update. Anything else?

```
