# merupakan widget yang memungkinkan pengguna untuk untuk memilih nilai (atau range nilai) dari sebuah range nilai yang telah ditentukan

import streamlit as st 

values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)