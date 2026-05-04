import streamlit as st

st.title('Simple Streamlit QUIZ!')

# 1. 체크박스 --> 여러개 동시 선택 또는 하나도 선택 안해도 됨
agree = st.checkbox('Q1. Python is programming language.(Check if correct)')
if agree: #체크를 하면 참, 안하면 거짓
    st.write('You are correct!')

st.divider()

# 2. 라디오 버튼  -> 하나만 꼭 선택을 해야 함
person = st.radio(
    'Q2. Gender?',
    ['Male', 'Female']
)
if person == 'Male':
    st.write('You are a male')
else: 
    st.write('You are a woman')

st.divider()

# 3. 단일 선택 박스
transport = st.selectbox(
    'Q3. What is the fastest transportation?',
    ['Train','Car','Plane','Ship']
)
if transport == 'Plane':
    st.write('Correct! Plane is the fastest!')
else:
    st.write('Incorrect! Plane is the fastest!')