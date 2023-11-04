import streamlit as st
import pandas as pd

# element write untuk menampilkan sebuah output
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))