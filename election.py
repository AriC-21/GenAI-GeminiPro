from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

## Configure GenAI key
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

def convert_rows_to_df(rows):
    df = pd.DataFrame(rows)
    return df
prompt = [
    """
    You are an expert in converting English queries to SQL queries!
    The SQL database has the name ELECTION and has the following columns:STATE,YEAR,CONSTITUENCY,CONSTITUENCY_NO,CONSTITUENCY_TYPE,CANDIDATE_NAME,CANDIDATE_SEX,PARTY,PARTY_ABBREVIATION,TOTAL_VOTES,ELECTORS.
    For example,\nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM ELECTION;
    \n Example 2 - Tell me all the candidates Andaman & Nicobar Islands in 2014?,
    the SQL command will be something like this SELECT * FROM ELECTION WHERE CONSTITUENCY='Andaman & Nicobar Islands' AND YEAR='2014';
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
    rows = read_sql_query(response,'students.db')
    df = convert_rows_to_df(rows)
    st.table(df)