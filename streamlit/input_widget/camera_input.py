# camera input widget yang dapat digunakan untuk meminta user mengambil gambar melalui webcam sekaligus mengunggahnya.

import streamlit as st 

picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)