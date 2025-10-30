import streamlit as st                 # Importa o Streamlit: framework para construir apps web de dados.
import pandas as pd                    # Importa o Pandas: manipulação e análise de dados em DataFrames.

st.set_page_config(layout='wide')      # Configura a página para usar toda a largura da janela (layout "wide").
                                       # OBS: por boas práticas, deixe esta linha o mais no topo possível,
                                       # antes de qualquer outro componente visual do Streamlit.

# --- Leitura dos dados --------------------------------------------------------
df_reviews = pd.read_csv("archive/customer reviews.csv")          # Lê o CSV de avaliações dos clientes.
df_top100_books = pd.read_csv("archive/Top-100 Trending Books.csv")  # Lê o CSV com o top 100 de livros.

# --- Seleção do livro no sidebar ---------------------------------------------
books = df_top100_books["book title"].unique()  # Extrai os títulos sem repetição (array de valores únicos).
book = st.sidebar.selectbox("Book", books)      # Cria um select no menu lateral para o usuário escolher o livro.

# --- Filtragem dos DataFrames pelo livro escolhido ---------------------------
df_book =  df_top100_books[df_top100_books["book title"] == book]  # Filtra a linha do livro escolhido no DF principal.
df_reviews_f = df_reviews[df_reviews["book name"] == book]         # Filtra as avaliações somente desse livro.

# --- Extração de campos do livro selecionado ---------------------------------
# Abaixo pegamos valores escalar (uma única célula) das colunas do livro.
# Usamos .iloc[0] porque df_book deve ter apenas 1 linha para o título único; isso retorna o primeiro registro.
book_title = df_book['book title'].iloc[0]
book_genre = df_book['genre'].iloc[0]
book_price = f"$ {df_book['book price'].iloc[0]}"           # Formata o preço como string com cifrão.
book_rating = df_book['rating'].iloc[0]
book_year = df_book['year of publication'].iloc[0]

# --- Cabeçalhos e métricas no layout -----------------------------------------
st.title(book_title)                   # Título principal do app: o título do livro.
st.subheader(book_genre)               # Subtítulo: o gênero do livro.

col1, col2, col3 = st.columns(3)       # Cria 3 colunas lado a lado para exibir KPIs/indicadores.
col1.metric('price', book_price)       # Indicador 1: preço.
col2.metric('rating', book_rating)     # Indicador 2: nota/avaliação média do livro.
col3.metric('year of publication', book_year)  # Indicador 3: ano de publicação.

st.divider()                           # Linha divisória horizontal para separar as seções da página.

# --- Seção de mensagens/avaliações -------------------------------------------
for row in df_reviews_f.values:        # Itera pelas linhas filtradas de avaliações (cada linha vira um array numpy).
    # ATENÇÃO: st.chat_message espera papéis ('user' ou 'assistant').
    # Aqui você está usando row[4] como "papel"; isso só funciona se a coluna 4 contiver esses valores válidos.
    messager = st.chat_message(f'{row[4]}')     # Cria um "balão" de chat com o papel definido na 5ª coluna.
    messager.write (f'**{row[2]}**')            # Escreve em negrito o que está na 3ª coluna (ex.: autor da review).
    messager.write (row[5])                     # Escreve o texto da avaliação (6ª coluna).
