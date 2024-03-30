import streamlit as st
import requests
import json


st.title('Summaries Agent and LessonPlan Agent 📚')

with st.form('my_form'):
    subject = st.text_area('Which Subject Summaries? ')
    grade = st.text_area('Which grade of Student? ')
    submitted = st.form_submit_button('Submit')
    if submitted:
        input_data = {'subject':subject, 'grade':grade}
        print(input_data)
        with st.spinner("waiting"):
            response =  requests.post(url='https://lessonplan-obpx.onrender.com/lessonplan/' , data=json.dumps(input_data))

            st.info(response.text)