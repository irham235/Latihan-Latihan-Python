# Text area merupakan widget yang memungkinkan pengguna untuk menginput multi-line text.

import streamlit as st 

text = st.text_area('Feedback')
st.write('Feedback: ', text)