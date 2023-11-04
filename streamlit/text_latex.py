# digunakan untuk menampilkan mathematical expression yang ditulis dalam format LaTeX
import streamlit as st
 
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")