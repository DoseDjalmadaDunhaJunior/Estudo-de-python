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

print("============forma 1================")
#é possivel ver o que repete em ambos

e1 = {'eu', 'você', 'zubumafoo'}
e2 = {'eu', 'tu', 'ele', 'nós'}

e3 = e1.intersection(e2)
print(e3)

print("============forma 2================")
#é possivel ver o que repete em ambos usando &
e4 = e1 & e2
print(e4)

print("====================================")
#ver os diferentes
e5 = e1.difference(e2)
e6 = e2.difference(e1)
print(e5,"\n",e6)