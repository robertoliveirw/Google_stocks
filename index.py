import streamlit as st
import pandas as pd 
import plotly.graph_objects as go

st.set_page_config(layout='wide') # Deixando a tela em modo wide
df = pd.read_csv('data/googlestocks.csv', sep=',', decimal='.') # Importando os dados
df = df.dropna(axis=1, how='all') # Removendo as colunas
df['Date'] = pd.to_datetime(df['Date']) # Tirando a data de string para int

