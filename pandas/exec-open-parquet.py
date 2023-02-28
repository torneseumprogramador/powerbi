
import pandas as pd
df = pd.read_parquet('dados.parquet')
# print(type(df))  # mostra o tipo do objeto <class 'pandas.core.frame.DataFrame'>
# print(df) # mostra as linhas do dataframe
# print(df.head(3)) # mostra 3 linhas do dataframe
# print( df.loc(0) ) # busca informação no DataFrame por indice
# print( df.loc(0)[0]["id"] ) # busca informação no DataFrame por indice e pegando dado de uma coluna
# print(df["nome"]) # mostra somente uma coluna do DataFrame
# print(df[["id", "nome"]]) # mostra duas ou mais colunas do DataFrame
print(df.loc[df["obs"]=="Aluna"]) # filtra dados de um dataFrame por coluna
print(df.loc[df["obs"]=="Aluna", ["id", "nome"]]) # filtra dados de um dataFrame por coluna, limitando colunas



# import pandas as pd
# df = pd.read_csv('dados.csv')
# print(df)