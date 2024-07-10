""" Calculadora """
cond = True
while cond:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digiite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print(f'Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    if sair is True:
        break