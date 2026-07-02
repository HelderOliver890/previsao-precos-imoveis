import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load("modelo_imoveis.pkl")

st.title("Previsão do Valor do Aluguel")

area = st.number_input("Área (m²)", min_value=20, value=80)
bedrooms = st.number_input("Quartos", min_value=1, value=2)
garage = st.number_input("Vagas de garagem", min_value=0, value=1)
total = st.number_input("Valor Total (R$)", min_value=0.0, value=3000.0)

entrada = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "garage": [garage],
    "total": [total]
})

if st.button("Prever aluguel"):
    previsao = modelo.predict(entrada)
    st.success(f"Aluguel estimado: R$ {previsao[0]:,.2f}")
