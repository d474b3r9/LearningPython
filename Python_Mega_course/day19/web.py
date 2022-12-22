import streamlit as st
import functions
# streamlit run web.py

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This todo app is to increase productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input("", placeholder="Add new todos ...")