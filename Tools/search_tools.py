import os
from crewai import Agent, Task
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI



class DuckGo:
    @tool("Search Internet Content")
    def search_internet(query:str) -> str:
        """Useful to search the internet about a a given topic and return relevant results"""
        duckduckgo_search = DuckDuckGoSearchRun()
        content = duckduckgo_search.run(query)

        return content


        