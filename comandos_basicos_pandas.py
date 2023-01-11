import pandas as pd 
# Mostrando certas quantidade de colunas e de linhas do arquivo:
# pd.set_option('display.max_rows',1)
# pd.set_option('display.max_columns',1)
data = pd.read_csv('db.csv',sep=';')
# Mostrando resumo detalhado do arquivo
print(data.describe())
# Mostrando outras informações do arquivo
print(data.info())
# Mostrando os tipos das colunas do arquivo
print(data.dtypes)
