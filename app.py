import streamlit as st
from src.backend.calc import add, multiply, division

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

st.title("🧮 Calculadora simples")
st.caption("Main: soma. Develop: soma + multiplicação.")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("A", value=0.0, step=1.0)
with col2:
    b = st.number_input("B", value=0.0, step=1.0)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Somar"):
        st.success(f"Resultado: {add(a, b)}")

with c2:
    if st.button("Multiplicar"):
        st.success(f"Resultado: {multiply(a, b)}")

with c3:
    if st.button("Dividir"):
        st.success(f"Resultado: {division(a, b)}")