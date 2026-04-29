import streamlit as st
from PIL import Image

image = Image.open('input/Yosemite-valley.jpng.webp')

# 이미지 불러오기
st.image(image, caption='Yosemite_image')
st.image(image, caption='width is 100 pxl', width=100)
st.image(image, caption='width is 200 pxl', width=200)

# 화면 채우기
st.image(image, caption='Full Width',width='stretch')

# 이미지 원본 크기
st.image(image, caption='Original Size',width='content')

small_image = image.resize((200,200))
st.image(small_image, caption='Used Stretch', width='stretch')
st.image(small_image, caption='Used Content', width='content')

