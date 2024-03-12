# for, while (break/continue)

#for
for letra in 'Hello world':
    print(letra)

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)


#range
for c in range(0, 5):
    print(c)


# while
contador = 0
while contador < 5:
    print('contador')
    contador += 1

#break 
comando = ''
while True:
    comando = input('Digite o comando: ')
    
    if comando == 'sair':
        break


# continue

numeros = [-10, 3, 0, 5, -2]
for numero in numeros:
    if numero <= 0:
        continue
    print(numero)


# compreensão de listas
numeros = [1, 2, 3, 4, 5]
quadrados = []
for numero in numeros:
    quadrados.append(numero ** 2)


quadrados = [numero ** 2 for numero in numeros]

numeros = [-3, 0, -5, 1, 2, 4]
positivos = [numero for numero in numeros if numero > 0]