import pandas as pd
import psycopg2

csv = "csv/alunos.csv"

data = pd.read_csv(csv, index_col = 0)

data.head()

# data.set_index("curso.nome", inplace = True) 

data.query('curso == "201 - Tecnologia em Análise e Desenvolvimento de Sistemas - Cajazeiras (CAMPUS CAJAZEIRAS)"', inplace = True)
data.query('situacao != "Cancelado"', inplace = True)

# print(data.loc[: , "matricula"])
# print(data[[:"matricula", "curso"]])

# data.loc[:,"matricula"].mean()
# print(data.iloc[0])
# print(data.count())
qunt_alunos = data['matricula'].value_counts().count()

try:
    for x in range(qunt_alunos):
        aluno = data.iloc[x,x]
        print(aluno)
except ValueError:
    print("Oops!")


# print(data[:100])