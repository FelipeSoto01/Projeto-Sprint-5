# Importando bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st


# Carregando arquivo e prevendo erro
try:
    vehicles_data = pd.read_csv('vehicles.csv')
except FileNotFoundError:
    st.error("O arquivo 'vehicles.csv' não foi encontrado.")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("O arquivo está vazio.")
    st.stop()


# Funçoes para criar os graficos

def create_hist(data):
    """
    Esta funçao recebe um dataframe como argumento e 
    cria um histograma de quilometragem, com titulo e nomeando o eixo x.
    """
    return px.histogram(
        data, x="odometer", title='Distribuição de KM',
        labels={"odometer": "Quilometragem (KM)"}
    )


def create_scatter(data):
    """
    Esta funçao recebe um dataframe como argumento e
    cria um grafico de dispersao entre quilometragem e
    preço, adiciona titulo e nomeia os eixos
    """
    return px.scatter(
        data, x="odometer", y="price",
        title='Relação entre KM e Preço',
        labels={"odometer": "Quilometragem (KM)", "price": "Preço (USD)"}
    )


# Interface
st.header('Análise de Veículos Usados')


choose_graph = st.selectbox('Selecione um tipo de gráfico:', [
    'Histograma', 'Gráfico de Dispersão'
])


if choose_graph == 'Histograma':
    st.write('Visualizando o **Histograma de KM:**')
    hist = create_hist(vehicles_data)
    st.plotly_chart(hist, use_container_width=True)

elif choose_graph == 'Gráfico de Dispersão':
    st.write('Visualizando o **Gráfico de Dispersão (Preço vs KM):**')
    scatter = create_scatter(vehicles_data)
    st.plotly_chart(scatter, use_container_width=True)
