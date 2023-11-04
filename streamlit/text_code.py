# Pada beberapa case, kita harus menampilkan potongan kode ke dalam streamlit app (web app yang dibuat menggunakan streamlit).
# Untuk menjawab hal ini, streamlit telah menyediakan sebuah function bernama code()
import streamlit as st

code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')