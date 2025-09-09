import sys # sys ele vai permiti que acesse alguns comandos do sistema
from streamlit.web import cli as stcli 

sys.argv = ["streamlit", "run", "app.py"] # (sys.argv), ele vai criar uma lista para executar o programa na web, ou seja, sem prompt

sys.exit(stcli.main())


# Obs: 
# Pandas, vai o responsável pela manipulação de dados
# Plotly, vai ser o resposável pela biblioteca para contruir gráficos
#(streamlit run app.py)  vai ser responsável para iniciar o aplicativo na web.  