import streamlit as st
from PIL import Image

st.title('サプーアプリ')
st.caption('これはサプーの動画用アプリです。')

image = Image.open('./data/image01.png')
st.image(image,width=200)