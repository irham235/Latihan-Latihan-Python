# merupakan widget yang digunakan untuk menampilkan sebuah checklist untuk pengguna

import streamlit as st 

agree = st.checkbox('I agree')

if agree:
    st.write('Welcome to MyApp')