while True:
    cpf = input('Insira seu CPF (sem espaço e sem pontuação): ')
    cpf_analisado = cpf[:9] # Retirando os últimos digitos do CPF fornecido

    soma_total = 0 # Acumulador do cálculo
    reverter = 10 # Variável para multiplicar de forma decrescente
    
    # verificando se é número
    verificar_numerico = cpf.isnumeric() 
    verificar_qtd = len(cpf)

    if verificar_numerico == False:
        print('Insira apenas números.')
        continue

    if verificar_qtd < 11 or verificar_qtd > 11:
        print('Isso não é um CPF!')
        continue

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

    # Evitando sequência de números. Ex.: 11111111111
    sequencia = cpf_analisado == str(cpf_analisado[0]) * len(cpf)

    if cpf == cpf_analisado and not sequencia:
        print(f'O CPF {cpf_analisado} é Válido')
    else:
        print(f'O CPF {cpf_analisado} é inválido')
    sair = input('Deseja Sair? (S/N): ')

    if sair == 's' or sair == 'S':
        print('Até a próxima!')
        break