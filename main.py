# carrinho = ('Mouse', 'Teclado', 'Monitor', 'Monitor')
# print (carrinho[1])
#
# #Funções para tupla
# #Como obter um indice um item em uma tupla
#
# print(carrinho.count('Monitor'))

# vendas = ('Jorge', 'Amanda', 'Miguel', 'Miguel', 'Jorge', 'Miguel', 'Fernando', 'Amanda')
# miguel = vendas.count('Miguel')
# fernando = vendas.index('Fernando')
# print(f'Miguel realizou {miguel} vendas')
# print(f'O indice de fernando é {fernando}')

# Dicionario => chave:valor
# dividas = {
#     'Miguel': 1500,
#     'Joana': 700,
#     'Humberto': 250
# }
# print(dividas)
# print(dividas['Miguel'])

# eu = {
#     'nome': 'Luiz Bruno Alves de Araujo',
#     "profissao": 'Bancario',
#     'idade': 37
# }
# print(eu)
# eu['altura'] = 1.80
# print(eu)
# eu['estadoCivil'] = input('Digite o estado civil: ')
# print(eu)

# lista = {}
# for i in range(3):
#     nome = input('Digite o nome do produto: ')
#     preco = float(input('Digite o preço do produto: '))
#     lista[nome] = preco
# print(lista)

# dividas = {
#     'Miguel': 1500,
#     'Joana': 700,
#     'Humberto': 250
# }
# del dividas['Miguel']
# print(dividas)
#
# Como pecorrer um dicionário?
#
# for i in dividas:
#     print(f'{i} : {dividas[i]}')
#
# for u in dividas.values():
#     print(u)
#
# for a in dividas.items():
#     print(a)
#
# print(dividas.keys())

agenda = {}
while True:
    print('--- AGENDA TELEFONICA ---')
    print('1 - Adicionar contato')
    print('2 - Editar telefone')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - Listar todos')
    print('6 - Sair')
    opcao = input('Selecione uma opção: ')
    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        if nome not in agenda:
            agenda[nome] = input(f'Digite o telefone de {nome}: ')
            print('Telefone adicionado com sucesso!')
        else:
            print(f'{nome} ja está na agenda')
    elif opcao == '2':
        nome = input('Qual contato deseja modificar ?: ')
        if nome in agenda:
            agenda[nome] = input(f'Digite o novo telefone de {nome}: ')
            print(f'{nome} alterado com sucesso')
        else:
            print('Esse contato não existe')
    elif opcao == '3':
        nome = input('Qual contato deseja deletar? : ')
        if nome in agenda:
            del agenda[nome]
            print(f'{nome} apagado com sucesso!')
        else:
            print('Esse contato não existe')
    elif opcao == '4':
        nome = input('Qual contato deseja o telefone? : ')
        if nome in agenda:
            print(f'O telefone de {nome} é {agenda[nome]}')
        else:
            print('Esse contato não existe')
    elif opcao == '5':
        print(f'--- Contatos da Agenda ---')
        for i in agenda:
            print(f'{i} : {agenda[i]}')
    elif opcao == '6':
        print('Programa encerrado')
        break
    else:
        print('Opção invalida')

