def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            
            if nota >= 0 and nota <= 10: 
                return nota
            else:
                print('Nota inválida!')
                
        except ValueError:
            print('Nota inválida!')

def continuar():
    while True:
        try:
            resposta = input("Deseja continuar? S/N").capitalize()[0]
            print(resposta)
            if (resposta == "N"):
                return False
            elif (resposta == "S"):
                return True
            else:
                print('Resposta inválida!')
        except IndexError:
            print('Resposta inválida!')

while True:
    with open('notas.txt', 'a') as notas:
        nome = input('Informe o nome: ')
        n1 = ler_nota('Informe a nota 1: ')
        n2 = ler_nota('Informe a nota 2: ')
        n3 = ler_nota('Informe a nota 3: ')
        notas.write(f"{nome},{n1},{n2},{n3};")
        
        if not continuar():
            break



    