from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from main import LessonPlanCrew
import asyncio

app = FastAPI()

class Query(BaseModel):
    subject:str
    grade:str 

@app.get("/")
async def heartbeat():
    return {"Lesson Plan":"Welcome To Lesson Plan Agent"}


@app.post('/lessonplan/')
async def lessonplan(query:Query):

    try:
        subject = query.subject
        grade = query.grade
        lesson_plan_crew = LessonPlanCrew(subject=subject, grade=grade)
        response = await lesson_plan_crew.run()
        print("\n\n########################")
        print(f"## Here is the Lesson for {subject} and {grade} ")
        print("########################\n")
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)

