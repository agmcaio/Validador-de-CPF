continuar = True

while continuar == True:
    cpf = input('Insira seu CPF (sem espaço e sem pontuação): ')
    cpf_analisado = cpf[:-2] # Retirando os últimos digitos do CPF fornecido

    soma_total = 0 # Acumulador do cálculo
    reverter = 10 # Variável para multiplicar de forma decrescente
    verificar = cpf.isnumeric() # verificando se é número

    if verificar == False:
        print('Insira apenas números.')
        break

    for i in range(19):
        if i > 8: 
            i -= 9

        soma_total += int(cpf[i]) * reverter #Cálculo matemático para validar CPF.

        reverter -= 1 # Começando a multiplicar pelo 10 de forma decrescente
        if reverter < 2:
            reverter = 11
            digito = 11 - (soma_total % 11)

            if digito > 9:
                digito = 0

            soma_total = 0
            cpf_analisado += str(digito)

    if cpf == cpf_analisado:
        print(f'O CPF {cpf_analisado} é Válido')
    else:
        print(f'O CPF {cpf_analisado} é inválido')
    
    sair = input('Deseja Sair? (S/N): ')

    if sair == 's'.upper():
        break