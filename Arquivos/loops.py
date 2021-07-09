nome = "Vai tomar no cu"
lista = [1,2,3,4,5,6,7,8,9]
numeros = range(1, 10)

for i in nome: #iterando sobbre string
    print(i)

print("===========================================")
for i in lista: #iterando lista
    print(i)

print("===========================================")
for i in range(0, 10): #iterando range
    print(i)

print("===========================================")
for indice,letra in enumerate(nome):
    print(nome[indice])

for letra in nome:
    print(letra, end='')

num = int(input("coloca ai quantas vezes o loop deve rodar\n"))
soma = 0
for n in range(1, (num+1)):
    x = int(input(f'Informe o {n}/{num} valor: '))
    soma = soma + x

print(f'a soma é {soma}')