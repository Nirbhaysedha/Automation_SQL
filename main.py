import streamlit as st
from langchain_helper import get_few_shot_db_chain
image_path=r"/Users/nirbhaysedha/Desktop/palm_sql_gpt/kpmg-logo-1.webp"

st.markdown("<h1 style='color:Deepskyblue;'>KPMG QUERY WIZARD</h1>", unsafe_allow_html=True)

st.image(image_path, width=100)

question = st.text_input("Question: ")

user=st.text_input("enter the user name")
password=st.text_input("enter the password",type="password")
host=st.text_input("enter the host name")
dbname=st.text_input("enter the database name")

if question:
    chain = get_few_shot_db_chain(user,password,host,dbname)
    response = chain.run(question)

    st.markdown("<h2 style='color: white;'>Retrieved answer is:</h2>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: white;'>{response}</h2>", unsafe_allow_html=True)











