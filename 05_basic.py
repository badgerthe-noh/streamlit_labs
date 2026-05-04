import streamlit as st
import pandas as pd

df_menu = df_menu = pd.DataFrame({
    "메뉴명": ["아메리카노", "카페라떼", "카푸치노", "말차라떼"],
    "가격": [4500, 5000, 5500, 6000]
})

# 데이터프레임 출력
st.dataframe(df_menu, height=170, width='stretch') # 전체 너비로 늘리기 

st.dataframe(df_menu, height=200, width='content') # 실제 원본 너비

st.dataframe(df_menu, 400, 180) # 너비 400, 높이 180 픽셀

st.divider() # 구분선

#테이블
st.table(df_menu)