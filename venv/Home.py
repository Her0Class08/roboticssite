import streamlit as st
import pandas as pd


# opens, reads and counts all-students
def student_number():
    file = open("info/all-students.txt")
    list = file.read()
    list.strip()
    number = len(list.split())
    return number


def allstudents():
    file = open("info/all-students.txt")
    list = file.read()
    list.strip()
    return list


def allcoaches():
    file = open("info/all-coaches.txt")



# page configuration
st.set_page_config(layout='wide')
c1 = st.columns(3)

# main description
main_des = f"Our program has {student_number()} students: {allstudents()}"

# top of site
st.header('PACT robotics program')
st.write(main_des)
