import pandas as pd

filmes = pd.read_excel("Filmes.xlsx")

for index, row in filmes.iterrows():
    nome_filme = row['Filme']
    avaliacao = input(f'Avalie o filme {nome_filme}: ')
    
    filmes.loc[index,'Avaliacao'] = avaliacao
    

filmes.to_excel("filmes_avaliados.xlsx")




