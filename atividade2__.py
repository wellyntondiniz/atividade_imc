
with open('notas.txt', 'r') as arquivo:
    texto = arquivo.read()
    alunos = texto.split(';')
    for aluno in alunos:
        lista = aluno.split(',')
        
        if (lista[0] != ''):
            media = (float(lista[1]) + float(lista[2]) + float(lista[3])) /3
            nome = lista[0]
            if media >= 7:
                with open('aprovados.txt', 'a') as aprovados:
                    aprovados.write(f'{nome};')
            elif media >= 5:
                with open('exame.txt', 'a') as exame:
                    exame.write(f'{nome},{media};')
            else:
                with open('reprovados.txt', 'a') as reprovados:
                    reprovados.write(f'{nome};')
                
            
