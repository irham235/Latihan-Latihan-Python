# Button merupakan widget untuk menampilkan tombol interaktif
# Tombol tersebut dapat digunakan pengguna untuk melakukan aksi tertentu

import streamlit as st 

if st.button('Say hello'):
    st.write('Hello there')