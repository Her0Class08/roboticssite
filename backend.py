import streamlit as st
# import pandas as pd

# sl means student list
# opens, reads and counts all-students
sl = open("info/all-students.txt")
allstudents = sl.read()
allstudentsgood = allstudents.strip()
studentnumber = len(allstudents.split())

# for debugging
if __name__ == '__main__':
    print(allstudentsgood)