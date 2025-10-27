

with open('exame.txt', 'r') as exame:
    linha = exame.read()
    alunos = linha.split(';')
    for aluno in alunos:
        lista = aluno.split(',')
        exame = input(f'Informe a nota de exame do aluno {lista[0]}: ')
        
        media = (float(exame) + float(lista[1]))/2
        
        