import os
from langchain.agents import Tool
from langchain import hub
from langchain_community.utilities import PythonREPL, WikipediaAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool

python_repl = PythonREPL()
os.environ["GOOGLE_API_KEY"] = os.environ.get('GOOGLE_API_KEY')
prompt = hub.pull("hwchase17/react")
wikipedia = WikipediaAPIWrapper()

template = """
Answer the question based on the context below. If the
question cannot be answered using the information provided answer
with "Please give me more context to subject".
Develop a detailed lesson plan for {subject} tailored for {gradelevel} students. The lesson plan should include the following components:
Age: Specify the age group of the students for whom the lesson is intended.
Lesson Duration: Indicate the estimated duration of the lesson.
Number of Students: Specify the number of students participating in the lesson.
Rationale: Provide a brief explanation of why this lesson is important and relevant to the students.
Objectives: Clearly outline the learning objectives that the lesson aims to achieve.
Lesson:
Introduction: Engaging opening to the lesson.
Background Knowledge: Review of relevant concepts or previous learning.
Performance: Describe the expected performance outcomes from the students.
Key Events: Highlight key activities or milestones in the lesson.
Materials: List the materials and resources required for the lesson.
Class Practice: Include interactive activities or exercises for student participation.
Assessment: Outline the assessment methods to measure student understanding and progress.

"""
prompt_template = PromptTemplate(
    input_variables=['subject', 'greadelevel'],
    template=template
)

user_prompt = prompt_template.format(
        subject = "The Civil War",
        gradelevel = '4 grade'
    )

tools = [

]
wikipedia_tool = Tool(
    name='wikipedia',
    func= wikipedia.run,
    description="Useful for when you need to look up a topic, country or person on wikipedia"
)
tools.append(wikipedia_tool)

llm = ChatGoogleGenerativeAI(model="gemini-pro")
agent = create_react_agent(
    tools=tools,
    llm=llm,
    prompt=prompt,
    
)
agent_executor = AgentExecutor(agent=agent, tools=tools, max_iterations=3, verbose=True)
output = agent_executor.invoke({"input": user_prompt})
