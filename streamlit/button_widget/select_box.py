# merupakan widget yang memungkinkan pengguna untuk memilih salah satu dari beberapa pilihan yang ada
# erupakan opsi alternatif dari radio button

import streamlit as st 

genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)