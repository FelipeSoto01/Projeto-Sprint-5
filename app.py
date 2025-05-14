# importando bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st


# lendo o arquivo csv
vehicles_data = pd.read_csv('vehicles.csv')


def create_hist(data):
    return px.histogram(data, x="odometer")


def create_scatter(data):
    return px.scatter(data, x="odometer", y="price")


st.header('Analise de Veiculos')

choose_graph = st.selectbox('Selecione um tipo de grafico', [
                            'Histograma', 'Grafico de dispersão'])

if choose_graph == 'Histograma':
    st.write('Criando histograma')
    hist = create_hist(vehicles_data)
    st.plotly_chart(hist, use_container_width=True)

elif choose_graph == 'Grafico de dispersão':
    st.write('Criando grafico de dispersão')
    scatter = create_scatter(vehicles_data)
    st.plotly_chart(scatter, use_container_width=True)
