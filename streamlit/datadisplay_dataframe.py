# function yang digunakan untuk menampilkan DataFrame sebagai sebuah tabel interaktif.
#   Pada function ini, kita bisa mengatur ukuran dari table yang ingin ditampilkan menggunakan parameter width dan height

import pandas as pd
import streamlit as st 
 
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)