# importando bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px


# lendo o arquivo csv
df_car_data = pd.read_csv('vehicles.csv')

st.header('Vehiculos')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando histograma para conjunto de dados')

    hist_df_car_data = px.histogram(df_car_data, x="odometer")

    st.plotly_chart(hist_df_car_data, use_container_width=True)


scatter_button = st.button('Criar grafico de dispersao')

if scatter_button:
    st.write('Criando grafico de dispersao')

    scatter_df_car_data = px.scatter(df_car_data, x="odometer", y="price")

    st.plotly_chart(scatter_df_car_data, use_container_width=True)
