# caso o pandas não esteja instalado, rodar os comandos abaixo no servidor linux
# sudo apt install python3-pip
# sudo apt install unixodbc-dev 
# https://learn.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline
# pip install pyodbc


import pandas as pd
import pyodbc

# Lendo o arquivo CSV usando o método read_csv
df = pd.read_csv("dados.csv")

# Criando uma conexão com o SQL Server
conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:dadoscsvdatalake.database.windows.net,1433;Database=dados-csv;Uid=administrador;Pwd=D5m6i2Trh;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

# Loop através de cada linha no DataFrame
for index, row in df.iterrows():
    # Inserindo uma linha na tabela
    conn.execute("INSERT INTO dados (codigo, nome, obs) VALUES (?, ?, ?)", row[0], row[1], row[2])

# Salvando as mudanças
conn.commit()

# Fechando a conexão
conn.close()
