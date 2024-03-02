from crewai import Task
from textwrap import dedent


class LessonPlanTasks:


    def research(self, agent, subject, grade):

        return Task(
            description = dedent(f"""You're an educational content creator 
                who specializes in designing engaging and effective lesson plans for 
                students across various subjects and grades. Your task is to develop a 
                detailed lesson plan tailored to a specific student's {subject} and {grade}. 

                The key components to be included in this lesson plan are
                Age, Lesson Duration, No. of student, Rationale, Objective, Lesson, 
                Introduction, Background Knowledge, Performance, 
                Key Event, Material, Class Practice, Assement. Make this point wise

                Your goal is to create a comprehensive and interactive lesson plan that 
                caters to the student's learning needs, abilities, and interests. 
                Ensure that the plan incorporates a variety of teaching strategies, 
                resources, and assessments to promote student engagement and knowledge retention. 
                
                Please make sure you complete the objective above with the following rules:
                1/ You should do enough research to gather as much information as possible about the objective
                2/ You should not make things up, you should only write facts & data that you have gathered
                3/ After scraping & search, you should think "is there any new things i should search & scraping based on 
                the data I collected to increase research quality?" If answer is yes, continue; But don't do this more 
                than 3 iteratins."""),

            agent = agent)


    def teacher(self, agent, subject):
        
        return Task(
            description = dedent(f"""As an experienced teacher with a dedication to crafting 
                comprehensive and effective lesson plans, your expertise lies in ensuring that every aspect of a 
                student's learning experience is covered with precision and detail. You take pride in creating 
                engaging and enriching lesson plans that leave no stone unturned in fostering a deep understanding 
                of the subject matter.

                Remember to tailor the lesson plan to the student's learning needs and abilities, ensuring that each 
                component contributes to their overall comprehension and engagement with the {subject} matter.

                If we take an example, your approach to creating lesson plans involves breaking down complex topics into bite-sized, 
                digestible chunks for students. By incorporating interactive activities, visual aids, and real-world examples, 
                you help students grasp difficult concepts with ease. Your lesson plans are meticulously structured to keep 
                students motivated and actively participating in their learning journey.

                Please make sure you complete the objective above with the following rules:
                1/ You should do enough research to gather as much information as possible about the objective
                2/ You should not make things up, you should only write facts & data that you have gathered
                3/ After scraping & search, you should think "is there any new things i should search & scraping based on 
                the data I collected to increase research quality?" If answer is yes, continue; But don't do this more 
                than 3 iteratins."""),

            agent = agent)


    def supervisor(self, agent, subject):
        
        return Task(
            description = dedent(f"""You're an educational supervisor with years of experience developing 
            comprehensive lesson plans for students across various {subject}. Your role is critical in 
            ensuring that the lesson plans are engaging, informative, and well-structured to meet the 
            learning objectives effectively.

            When crafting the lesson plan, remember to include clear objectives aligned with the curriculum, 
            interactive activities, assessment methods, and room for differentiation to cater to diverse learning needs within the classroom.


            Please make sure you complete the objective above with the following rules:
                1/ You should do enough research to gather as much information as possible about the objective
                2/ You should not make things up, you should only write facts & data that you have gathered
                3/ After scraping & search, you should think "is there any new things i should search & scraping based on 
                the data I collected to increase research quality?" If answer is yes, continue; But don't do this more 
                than 3 iteratins.
            
            *** You must include this points in lesson plan this are compulsory Age, Lesson Duration, No. of student, Rationale, 
            Objective, Lesson, Introduction, Background Knowledge, Performance, 
            Key Event, Material, Class Practice, Assement ***. 
            ****Use Only MARKDOWN method***"""),

            agent = agent)
