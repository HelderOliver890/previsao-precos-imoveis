import streamlit as st
import pandas as pd
import joblib

#Carregar Modelo Treinado
modelo = joblib.load("modelo_imoveis.pkl")

st.title("Previsão de Preço de Imóveis")

st.write("Preencha os dados do imóvel.")

#Entradas do Usuário
area = st.number_input("Área (m²)", min_value=20, value=100)
quartos = st.number_input("Número de quartos", min_value=1, value=2)
banheiros = st.number_input("Número de banheiros", min_value=1, value=2)
vagas = st.number_input("Número de vagas", min_value=0, value=1)

#DataFrame com os Dados de Entrada
entrada = pd.DataFrame({
    "Area": [area],
    "Quartos": [quartos],
    "Banheiros": [banheiros],
    "Vagas": [vagas]
})

#Botão para Prever
if st.button("Prever preço"):
    preco = modelo.predict(entrada)
    st.success(f"Preço estimado: R$ {preco[0]:,.2f}")
