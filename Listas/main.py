# é um vetor ou matriz
type([])

lista1 = [1,2,3,4,5,6]

lista2 = ['p','e','n','i','s']

lista3 = []

lista4 = list(range(11))

lista5 = list("chupa meu penis")

print(lista5)

num = 'a'

if 'a' in lista5:
    print(f"tem numero ou letra {num}")
else:
    print("não ta porra")


print("=====================")
# ordena os valores o .sort()
lista5.sort()
print(lista5)

# conta a quanrtidade de ocorrencias em um vetor
print(lista5.count('p'))

#adcionar elementos no vetor

print("=====================")
print(lista1)
lista1.append(365) #append adciona apenas 1 item por vez
print(lista1)
lista1.append(lista4)
print(lista1)
lista1.extend(list("bom dia companheiro"))
print(lista1)
print("=====================")
# inserir em uma outra posição
print(lista2)
lista2.insert(2, "aqui")
print(lista2)
print("=====================")
# juntar listas
lista6 = lista1 + lista2 + lista3 + lista4 + lista5
print(lista6)

#inverter uma lista
lista6.reverse()
print(lista6)
print(lista6[::-1])

#copiar lista
lista7 = lista1
print("=====================")
print(lista7)

#ver o tamanho de um vetor
print("=====================")
print(len(lista6))

# remover ultimo item de um vetor
print("=====================")
print(lista2)
lista2.pop()
print(lista2)
lista2.pop(2)
print(lista2)

#limpar a lista
print("=====================")
lista1.clear()
lista1 = list(range(20))
print(lista1)

#converter string para lista
print("=====================")
txt = "Um texto aleatorio"
txt = txt.split() # se a divisão fosse outra coisa que não espaço é só colocar dentro do ()
print(txt)

#fazendo o oposto
txt = ' '.join(txt) #poe espaço entre cada string
print(txt)

#iterando sobre listas usando for
print("=====================")
soma = 0
for i in lista1:
    soma = soma + i
    print(soma)

# existe indexação negativa
print("=====================")
vet = ['a','b','c','d','e','f','g']
print(vet[1]) #normal
print(vet[-1]) #negativo

# gerar indice em um for
print("=====================")
for indice, i in enumerate(vet):
    print(indice,i)

# descobrir o indice em uma lista, porem ele pega apenas o 1º
print("=====================")
vet = [1,56,8,7,5,8,24,3,5434,5]
print(vet.index(5)) # busca o valor 5
# caso queira descobrir apartir de um numero especifico
print(vet.index(5,(vet.index(5)+1)))
print(vet.index(5,6)) # busca o valor 5 a partir da posição 6

#podemos procurar em um limite tambem
print(vet.index(5,2,8)) # busca o numero 5 entre a posição 2 e 8

print("=====================")
#slicing
#lista[inicio:fim:passo]

lista1 = [1,2,3,4]
print(lista1[1::]) # inicia do indice 1 até o final

print("=====================")

#soma do valor maximo com o valor minimo

lista1 = [1,2,3,4,5,6,7,8,9]

print(sum(lista1))
print(max(lista1))
print(min(lista1))
print(len(lista1))

print("=====================")
#transformar lista em tupla

print(lista1)
print(type(lista1))
tupla = tuple(lista1)
print(tupla)
print(type(tupla))

print("=====================")


