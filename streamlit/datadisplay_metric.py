# Function ini dapat membantu kita untuk menampilkan sebuah metrik tertentu beserta detailnya seperti label, value serta besar perubahan nilainya

import streamlit as st
 
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")