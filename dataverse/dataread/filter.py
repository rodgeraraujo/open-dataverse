import pandas as pd

def filterData(csv, type):
    data = pd.read_csv(csv, index_col = 0)
    data.head()

    if(type == "aluno"):
        data.query('curso == "201 - Tecnologia em Análise e Desenvolvimento de Sistemas - Cajazeiras (CAMPUS CAJAZEIRAS)"', inplace = True)
        data.query('situacao != "Cancelado"', inplace = True)
        qunt_alunos = data['matricula'].value_counts().count()
        try:
            for x in range(qunt_alunos):
                aluno = data.iloc[x,x]
                print(aluno)
        except ValueError:
            print("Oops!")