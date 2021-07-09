'''
Mapas e dicionarios são a mesma coisa
são representados por {}
'''

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

#para interar sobre dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

print("===============================");
print(receita.keys())
# essa é uma forma mais recomendada
for chave in receita.keys():
    print(receita[chave])


print("===============================");
#acessando valores
print(receita.values())
for valor in receita.values():
    print(valor)

