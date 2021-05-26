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

# ordena os valores o .sort()
lista5.sort()
print(lista5)

# conta a quanrtidade de ocorrencias em um vetor
print(lista5.count('p'))

#adcionar elementos no vetor

print(lista1)
lista1.append(365) #append adciona apenas 1 item por vez
print(lista1)
lista1.append(lista4)
print(lista1)
lista1.extend([1,2,3,4,5,6,7,8,9,11,11,115,51,1,51,1,1,65161])
print(lista1)