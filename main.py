from crewai import Crew
from textwrap import dedent
import asyncio
from Agents.lesson_plan_agent import LessonPlanAgents
from Tasks.lesson_plan_tasks import LessonPlanTasks


class LessonPlanCrew:
    def __init__(self, subject, grade) -> None:
        self.subject = subject
        self.grade = grade


    async def run(self):
        agents = LessonPlanAgents()
        tasks = LessonPlanTasks()

        research_analyst_agent = agents.research_analyst()
        teacher_analyst_agent = agents.teacher_analyst()
        supervisor_analyst_agent = agents.supervisor_analyst()

        research_task = tasks.research(agent=research_analyst_agent, subject=self.subject, grade=self.grade)
        teacher_task = tasks.teacher(agent=teacher_analyst_agent, subject=self.subject)
        supervisor_task = tasks.supervisor(agent=supervisor_analyst_agent,subject=self.subject)

        crew = Crew(
            agents=[
                research_analyst_agent,
                teacher_analyst_agent,
                supervisor_analyst_agent,
            ],

            tasks=[
                research_task,
                teacher_task,
                supervisor_task,
            ],
            verbose=True
        )

        result = crew.kickoff()

        return result

# if __name__ == "__main__":

#     print("## Welcome to Lesson Plan")
#     print('----------------------------')

#     subject = input(
#         dedent("""
#         What is subject Name ? """)
#     )

#     grade = input(
#         dedent("""
#         What is grade ? """)
#     )

#     lesson_plan_crew = LessonPlanCrew(subject=subject, grade=grade)
#     result = lesson_plan_crew.run()

#     print("\n\n########################")
#     print(f"## Here is the Lesson for {subject} and {grade} ")
#     print("########################\n")
#     print(result)
