import streamlit as st
import requests
import json


st.title('Summaries Agent and LessonPlan Agent 📚')
st.subheader("Since I'm using free render(If API idle for 50 sec, it will inactivity.)  for API hosting this takes time to run. So run twice or thrice: ")

with st.form('my_form'):
    subject = st.text_area('Which Subject Summaries? ')
    grade = st.text_area('Which grade of Student? ')
    submitted = st.form_submit_button('Submit')
    if submitted:
        input_data = {'subject':subject, 'grade':grade}
        print(input_data)
        with st.spinner("waiting"):
            response =  requests.post(url='https://lessonplan-obpx.onrender.com/lessonplan/' , data=json.dumps(input_data))

            modified_string = response.text.replace("\\n", "\n")
            st.info(modified_string)
