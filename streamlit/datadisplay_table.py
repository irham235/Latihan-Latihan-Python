# menggunakan function table()untuk menampilkan data ke dalam streamlit app
# a dapat digunakan untuk menampilkan data dalam bentuk static table

import pandas as pd
import streamlit as st 
 
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)