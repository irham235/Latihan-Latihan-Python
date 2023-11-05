# Selain button dan checkbox, terkadang kita juga membutuhkan radio button untuk menghasilkan web app yang interaktif.
# merupakan widget yang memungkinkan pengguna untuk memilih satu dari beberapa pilihan yang ada

import streamlit as st 

genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)