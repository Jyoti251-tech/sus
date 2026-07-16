import streamlit as st 
from database.mongodb import Student_collection
st.title("Student Register ")

first_name = st.text_input("First_name ")
last_name = st.text_input("last_name ")
email = st.text_input("email ")
course = st.text_input("course")
if st.button("Register student "):
    Student_collection.insert_one({

       "first_name ": first_name,
       "last_name ": last_name,
       "email": email,
       "course_name ": course,
    })
    st.success("student Registered succesfully")
