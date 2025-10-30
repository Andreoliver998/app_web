import streamlit as st

import pandas as pd


# Obs:
#Pandas trabalha de forma tabular, ou seja, todas as análises em tabalas semelhantes ao execel.
import plotly.express as px 
#visualização interativa simplificada

st.set_page_config(layout='wide') #(layout = "wide"), umas das modalidades do streamlit, para uma visão melhor da tabela da web.
#Configura a página para usar layout largo

df_reviews = pd.read_csv("archive/customer reviews.csv") #(pd.read), quer dizer que o pandas vai ler todo o aquivo, ou seja, dentro da váriavel df_reviews.

df_top100_books = pd.read_csv("archive/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"] .max() #pd vai pegar o maior valor da colona "book price"
price_min = df_top100_books["book price"] .min() #pd vai pegar o menor valor da coluna "book price"
max_price = st.sidebar.slider("Variáriação de Preço", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books
fig = px.bar(df_books["year of publication"] .value_counts())
fig2 = px.histogram(df_top100_books["book price"])

col1, col2 = st.columns(2)


col1.plotly_chart (fig)
col2.plotly_chart (fig2)


