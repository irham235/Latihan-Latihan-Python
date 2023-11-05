# Widget ini memungkinkan kita meminta pengguna untuk meng-upload sebuah berkas tertentu ke dalam web app

import streamlit as st 
import pandas as pd

uploaded_file = st.file_uploader('Choose a CSV file')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)