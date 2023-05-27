#calculadora usando WHILE para fazer um laço finito até que eu use a instrunção de sair
print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione "F" para ENCERRAR o programa!')



while True:
    op = input('Qual operação deseja fazer?: ')
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor'))
        y = int(input('Digite o segundo valor'))

    if (op=='+'):
        res=x+y
        print('Resultado {} + {} = {}'.format(x,y,res))
        continue
    elif (op=='-'):
        res=x-y
        print('Resultado {} - {} = {}'.format(x, y, res))
        continue
    elif (op == '*'):
        res=x*y
        print('Resultado {} * {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res=x/y
        print('Resultado {} / {} = {}'.format(x, y, res))
        continue
    elif (op == 'F'):
        break
    else:
        print('Operação invalida')


print('Encerrando a calculadora.')
