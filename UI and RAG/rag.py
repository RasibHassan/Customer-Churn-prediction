import os
import streamlit as st
from langchain.chains import create_sql_query_chain
from langchain_google_genai import GoogleGenerativeAI
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
load_dotenv() 

# Database connection parameters
db_user = "root"
db_password = "Rasibh231"
db_host = "localhost"
db_name = "telco_churn"

# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

# Initialize SQLDatabase
db = SQLDatabase(engine, sample_rows_in_table_info=3)

# Initialize LLM
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=os.environ["GOOGLE_API_KEY"]) # type: ignore

# Create SQL query chain
chain = create_sql_query_chain(llm, db)

def execute_query(question):
    try:
        # Generate SQL query from question
        
        response = chain.invoke({"question": question})
        if "SQLQuery:" in response:
            response = response.replace("SQLQuery:", "").strip()
        else:
            response = response.strip('```sql\n').strip('\n```')
        print(response)
        # Execute the query
        result = db.run(response)
                
        # Return the query and the result
        return response, result
    except ProgrammingError as e:
        st.error(f"An error occurred: {e}")
        return None, None

# Streamlit interface
st.title("Question Answering App")

# Input from user
question = st.text_input("Enter your question:")

def generate_text(question,result,llm):
    text = llm.invoke(f'here is following its generated answer now write answer in short text form \n Question: {question}\nAnswer: {result}', max_length=100)
    return text

if st.button("Execute"):
    if question:
        cleaned_query, query_result = execute_query(question)
        
        if cleaned_query and query_result is not None:

            st.write("RESPONSE:",generate_text(question,query_result,llm))
        else:
            st.write("No result returned due to an error.")
    else:
        st.write("Please enter a question.")
        