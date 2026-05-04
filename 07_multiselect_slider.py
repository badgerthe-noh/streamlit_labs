import streamlit as st
from datetime import time

st.title('Hands-on Streamlit widget practice 2')

st.divider()

#1. 다중 선택박스 퀴즈
st.subheader('1. Multi-select box QUIZ!')

fruits = st.multiselect(
    'Q1. Select everything its fruits; multiple selection allowed',
    ['Apple', 'Tomato', 'Carrot', 'Banana']
)

correct = {'Apple', 'Banana'} # set는 순서 상관 없음

if set(fruits) == correct:
    st.write('Correct! They are all fruits!')
else:
    st.write('Try again')

st.divider()

st.subheader('2. Number Slider')
score = st.slider('Your score is...',0,100,2)

st.text(f'Score : {score}')

st.divider()

st.subheader('3. Time range slider')

# 시작 시간, 종료 시간 --> 각각 슬라이더로 입력받는다
start_time, end_time = st.slider(
    'Labor time is ...',
    min_value=time(0),
    max_value=time(23),
    value=(time(9),time(18)),
    format='HH:mm'
)

# 선택한 시작 시간과 종료 시각을 텍스트로 출력
st.text(f'Labor time: {start_time}, {end_time}')

