pedidos = []
while True:
    print('\n1.Cadastrar pedido\n'+
            '2.Listar pedido de uma mesa\n'+
            '3.Listar todos os pedidos\n'+
            '4.Valor apurado\n'+
            '5.Sair\n')
    op = int(input('Opção >> '))
    if op == 1:
        mesa = int(input('Mesa >> '))
        pizza = input('Pizza >> ')
        bebida = input('Bebida >> ')
        valor = float(input('Valor >> '))
        pedido = (mesa,pizza,bebida,valor)
        pedidos.append(pedido)
    elif op == 2:
        num_mesa = int(input('Mesa >> '))
        for pedido in pedidos:
            if num_mesa in pedido:
                print(pedido)
    elif op == 3:
        print(pedidos)
    elif op == 4:
        soma = 0
        for pedido in pedidos:
            soma = soma + pedido[3]
        print(soma)
    elif op == 5:
        break
print('Tchau')