import streamlit as st
import pandas as pd


# opens, reads and counts all-students
def student_number():
    # Opens info file
    file = open("info/all-students.txt")
    # Reads info file into string
    list = file.read()
    # Removes \n from string
    list.strip()
    # Counts words in string
    number = len(list.split())
    # returns the number of words in string -1 "and"
    return number - 1


def allstudents():
    # opens file
    file = open("info/all-students.txt")
    # reads file
    list = file.read()
    # returns file
    return list


def coach_number():
    file = open("info/all-coaches.txt")
    list = file.read()
    number = len(list.split())
    return number - 1


def allcoaches():
    file = open("info/all-coaches.txt")
    list = file.read()
    list.strip()
    return list



# page configuration
st.set_page_config(layout='wide')
c1 = st.columns(3)

# main description
main_des = f"Our program has {student_number()} students: {allstudents()} and {coach_number()} coaches: {allcoaches()}"

# top of site
st.header('PACT robotics program')
st.write(main_des)
st.image('info/images/IMG_0823.jpeg')