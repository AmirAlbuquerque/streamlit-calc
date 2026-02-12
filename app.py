import streamlit as st
from src.backend.calc import add

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora simples")
st.caption("Main: soma. Develop: multiplicação (será adicionada via PR).")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("A", value=0.0, step=1.0)
with col2:
    b = st.number_input("B", value=0.0, step=1.0)

if st.button("Somar"):
    result = add(a, b)
    st.success(f"Resultado: {result}")