import streamlit as st

st.set_page_config(page_title="Simulador Biorreactor 3D", layout="wide")

st.title("Simulador Biorreactor 3D con Sensores")

# Incrustar el HTML
st.components.v1.iframe("simulador_streamlit.html", height=700)
