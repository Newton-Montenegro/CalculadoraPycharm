#calculadora usando WHILE para fazer um laço finito até que eu use a instrunção de sair
print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')



while True:
    op = input('Qual operação deseja fazer?')
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
    elif (op == 'f'):
        break
    else:
        print('Operação invalida')


print('Encerrando o Programa.')
print ('Thank you for all!')
print ('Thank you for all two!')