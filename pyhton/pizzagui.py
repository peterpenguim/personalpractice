import json


with open('LNPG/cardapio.json') as json_file:
    data = json.load(json_file)
    cardapio = data['cardapio']

print('PIZZARIA DO GUIGUI'.center(30))
print('-------------------------------')
print('PIZZAS')
for pizza in cardapio[0]['pizzas']:
    print('{} >> {}'.format(pizza['sabor'], pizza['valor']))
print('\n')
print('BEBIDAS')
for bebida in cardapio[1]['bebidas']:
    print('{} >> {}'.format(bebida['nome'], bebida['valor']))
print('-------------------------------')
    