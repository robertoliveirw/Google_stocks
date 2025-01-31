import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout='wide')  # Deixando a tela em modo wide

# Importando os dados
df = pd.read_csv('data/googlestocks.csv', sep=',', decimal='.')

# Removendo as colunas em branco
df = df.dropna(axis=1, how='all')

# Convertendo a coluna 'Date' para formato datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filtro de data com o slider
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()

# Filtro de data com o slider
start_date, end_date = st.slider(
    "Selecione o intervalo de datas",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),
    format="YYYY-MM-DD"
)

# Filtrando os dados com base nas datas selecionadas
df_filtered = df[(df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)]

# Gerando o gráfico com os dados filtrados
fig_line = go.Figure([go.Scatter(x=df_filtered['Date'], y=df_filtered['Close'])])

# Exibindo o gráfico
st.plotly_chart(fig_line)
