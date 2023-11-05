# Selain inputan berupa angka dan teks, pada beberapa kasus kita juga membutuhkan input berupa tanggal dari pengguna melalui date input widget

import datetime
import streamlit as st 

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)