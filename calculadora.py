def calcular():
    print('Calculadora simples')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    opcao = input('Digite o número da opção desejada acima: ')


    if opcao >= '5':
        print('Digite a opção presente na escolha.')
    else:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

    if opcao == '1':
        resultado = num1 + num2
        print(f'A soma de {num1} com {num2} é {resultado} ')
    elif opcao =='2':
        resultado = num1 - num2
        print(f'A subtração de {num1} com {num2} é {resultado} ')
    elif opcao == '3':
        resultado = num1 * num2
        print(f'A multiplicação de {num1} com {num2} é {resultado} ')
    elif opcao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f'A divisão de {num1} com {num2} é {resultado} ')
        else: 
            print('Divisão por zero não é permitido ')
            
calcular()



