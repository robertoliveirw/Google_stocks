import streamlit as st
import pandas as pd 
import plotly.express as px

st.set_page_config(layout='wide')
df = pd.read_csv('data/googlestocks.csv', sep=',', decimal='.')
df = df.dropna(axis=1, how='all')

df['Date'] = pd.to_datetime(df['Date'])
df