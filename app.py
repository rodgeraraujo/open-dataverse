import pandas as pd
import psycopg2

csv = "csv/alunos.csv"

data = pd.read_csv(csv, index_col = 0)

data.head()

# data.set_index("curso.nome", inplace = True) 

data.query('curso == "201 - Tecnologia em Análise e Desenvolvimento de Sistemas - Cajazeiras (CAMPUS CAJAZEIRAS)"', inplace = True)

print(data[:10])