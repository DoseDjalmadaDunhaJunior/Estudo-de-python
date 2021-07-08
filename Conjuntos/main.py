"""
Conjuntos
Mesma coisa de conjuntos na matematica
conjuntos == sets
igual a matematica:
 - não possuem valores duplicados
 - Não possuem valores ordenados
 - não são indexados

Conjuntos são bons para armazenar elementos porem não precisamos
nos importar com a ordenação ou valores e itens duplicados

diferença entre maas e conjutos
 - dicionario tem chave/valor
 - conjunto tem apenas valor

se tem repetição o numero repetido é ignorado
"""

# definindo conjunto
# forma 1
conj = set({1,2,3,4,5,5,6,6,7,8,3})
print(conj)
print(type(conj))

#forma 2

conj = {2,1,26,5,4,8,9,6,2,4,4}
print(conj)

if 3 in conj:
    print("Tem o 3")
else:
    print("Não tem o 3")

conj.discard(1)
print(conj)