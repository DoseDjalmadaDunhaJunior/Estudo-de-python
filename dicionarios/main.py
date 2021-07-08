#dicionarios Não podemos ter chaves repetidas
paises = {'br': 'brasil', 'eua': 'estados unidos', 'py': 'paraguai'}
print(paises)
#ou
paises = dict(br = 'brasil', eua = 'estados unidos', py = 'paraguai')
print(paises)

# acessando elementos
#forma 1

print(paises['br'])

#forma 2

print(paises.get('br'))
print(paises.get('x'))
# da para definir um valor padrão
pais = paises.get('py', 'Não encontrado')
if pais:
    print(f'encontrei o pais {pais}')
else:
    print(f'pais {pais}')

print('br' in paises)

#podemos colocar outras coisas como chaves
localidades = {
    (103.3, 89.1): 'Radios',
    (100.0, 100.1): 'Sei la que merda',
}
print(localidades)

# adicionar elementos em um dicionario
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
receita['abril'] = 350
print(receita)

#outra forma
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# atualizar dados
# forma 1
receita['mai'] = 550
print(receita)

#forma 2
receita.update({'mai': 600})
print(receita)

print("==============================================")
#remover dados
#forma 1, precisa passar a chave
ret = receita.pop('mar')
print(ret)
print(receita)
#forma 2
del receita['fev']
print(receita)

print("==============================================")

carrinho = []
prod = ['ps5', 5000.00]
prod1 = ['god', 150.00]

carrinho.append(prod)
carrinho.append(prod1)

print(carrinho)

#opção 3
carrinho = []

prod = {'nome': "ps5", "quantidade": 1, "preço": 5000.00}
prod1 = {'nome': "god", "quantidade": 1, "preço": 150.00}

carrinho.append(prod)
carrinho.append(prod1)

print(carrinho)


