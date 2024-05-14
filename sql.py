from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure GenAI key
os.environ["GOOGLE_API_KEY"] == st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql_query,db):
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return rows

prompt = [
    """
    You are an expert in converting English queries to SQL queries!
    The SQL database has the name STUDENTS and has the following columns: NAME, CLASS, SECTION.
    For example,\nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS;
    \n Example 2 - Tell me all the students studying in Gen AI class?,
    the SQL command will be something like this SELECT * FROM STUDENTS WHERE CLASS='Gen AI';
    also the SQL code should not have ``` in beginning or end and sql word in output.
    """
]

# st.set_page_config(page_title="SQL Query Generator")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ",key='input')
submit = st.button("Ask the Question")

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    # st.write(response)
    # if "sql" in response:
    #     st.write("Executing the SQL Query")
    #     read_sql_query(response,'students.db')
    # else:
    #     st.write("Please ask a valid SQL question")
    st.subheader("The Response is: ")
    rows = read_sql_query(response)
    for row in rows:
        print(row)
        st.write_stream(row)