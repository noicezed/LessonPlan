import os
from crewai import Agent, Task
from langchain.agents import tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY"] = 'AIzaSyAlm8Ka3K-WdlR0cI4aCB0-BUB0nre2OZ4'
llm = ChatGoogleGenerativeAI(model="gemini-pro")


class WikiSearch:

    @tool("Scrape wikipedia content")
    def search_wikipedia(subject:str) -> str :
        """Useful to scrape and summarize a website content"""
        wikipedia_search = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        content = wikipedia_search.run(subject)

        summaries = []

        content = [content[i:i + 2000] for i in range(0, 5, 2000)]

        for chunks in content:

            agent = Agent(
                role='Head Research',
                goal="You're great Research about lesson plan for student \
                    you can summarries any content for student",

                backstory="You're a great Researcher for student at school \
                    you need to summaries content for student for their lesson plan",

                allow_delegation=False,
                llm=llm,)

            task = Task(
                agent=agent,
                description=f"""Analyze and summarize the content below, make sure to include 
                        the most relevant information in the summary, return only the summary 
                        nothing else.If any inapporpiate content or adult please remove it which 
                        affect children mind.If you think content is sensor or porngraphy directly reponse 
                        'You're children this not age to see this'.
                        You are a world class researcher, who can do detailed research on any topic and produce facts based results; 
                        you do not make things up, you will try as hard as possible to gather facts & data to back up the research
                        Please make sure you complete the objective above with the following rules:
                        1/ You should do enough research to gather as much information as possible about the objective
                        2/ You should not make things up, you should only write facts & data that you have gathered
                        3/ After scraping & search, you should think "is there any new things i should search & scraping based on 
                        the data I collected to increase research quality?" If answer is yes, continue; But don't do this more 
                        than 3 iteratins.
                        \n\nCONTENT\n----------\n{chunks}""")

            summary = task.execute()
            summaries.append(summary)

        return "\n\n".join(summaries)

