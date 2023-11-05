# merupakan elemen layout yang memungkinkan kita untuk mengatur tampilan pada konten utama ke dalam beberapa kolom sesuai kebutuhan
# Untuk membuat column dalam streamlit app, kita harus membuat object dari setiap kolom terlebih dahulu.

import streamlit as st

st.title('Belajar Analisis Data')
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.header("Kolom 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
    
with col2:
    st.header("Kolom 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Kolom 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")    