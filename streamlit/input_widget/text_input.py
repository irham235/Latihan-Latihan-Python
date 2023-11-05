# Text input merupakan widget yang digunakan untuk memperoleh inputan berupa single-line text

import streamlit as st

name = st.text_input(label='Nama lengkap', value='')
st.write('Nama:', name)