# merupakan widget yang digunakan agar user dapat memilih lebih dari satu pilihan dari sekumpulan pilihan yang ada

import streamlit as st 

genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)