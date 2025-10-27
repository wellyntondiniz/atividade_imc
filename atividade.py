lista_pessoas = []

continuar_coleta = True

while continuar_coleta:
    nome = input('Informe seu nome:')
    peso = float(input('Informe seu peso:'))
    idade = int(input('Informe sua idade:'))
    altura = float(input('informe sua altura:'))
    
    imc = peso / (altura * altura)
    
    resultado = ""
    
    if imc < 16:
        resultado = 'Baixo peso Grau I'
    elif imc < 16.99:
        resultado = 'Baixo peso Grau II'
    elif imc < 18.49:
        resultado = 'Baixo peso Grau III'
    elif imc < 24.99:
        resultado = 'Peso adequado'
    elif imc < 29.99:
        resultado = 'Sobrepeso'
    elif imc < 34.99:
        resultado = 'Obesidade grau I'
    elif imc < 39.99:
        resultado = 'Obesidade grau II'
    else:
        resultado = 'Obesidade grau III'

    lista_pessoas.append([nome, peso, idade, altura, imc, resultado])

    continuar_coleta = input("Deseja continuar? S/N: ").upper().capitalize() == "S" 
    
for pessoa in lista_pessoas:
    print(pessoa[0] + " - " + str(pessoa[2]) + " anos - " + pessoa[5])
    
    
