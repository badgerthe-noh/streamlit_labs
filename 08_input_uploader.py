import streamlit as st

# 1. 텍스트 입력창
string1 = st.text_input(
    'Favorite Pokemon???', # 입력 레이블
    placeholder='Type your favorite Pokemon!', # 안내글
    max_chars=32 # 최대 입력 글자 개수 제한
)
#입력값이 있으면 화면에 출력 (값이 채워져 있으면 참, 비어있으면 거짓)
if string1:
    st.text(f'Your answer is {string1}.')

# 2. 비밀번호 입력창 만들기
string2 = st.text_input(
    'Which food do you hate???', #입력창 레이블
    placeholder='Type one of the food you most hate!', #안내문구
    max_chars=32,
    type='password' # 입력값이 비밀번호 형태로
)

if string2:
    st.text(f'Your answer is {string2}.')

st.divider()

# 3. 파일 업로더
file = st.file_uploader(
    'Choose a file', # 업로드 문구 레이블
    type='csv', # 확장자 제한 (csv만)
    accept_multiple_files=False # 한번에 하나의 파일만 업로드 가능하게 
)

# 판다스의 데이터프레임 형태로 읽어 표 출력
import pandas as pd

if file is not None: 
    df = pd.read_csv(file)
    st.write(df) # database나 table을 써도 무관

    