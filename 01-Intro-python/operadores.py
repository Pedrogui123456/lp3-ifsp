# Operadores
# aritméticos
# +, -, *, /, %

nota1 = 2
nota2 = 5
media = (nota1 + nota2) / 2


#potencia
numero = 2 ** 3 # ao cubo
numero = 10 ** 2 # ao quadrado

#operadores lógicos
# and, or, not
# acesso liberado = nao bloqueado, idade > 20, horario comercial 8 e 18

bloqueado = False
idade = 21
hora_atual = 10

horario_comercial = 8 <= hora_atual <= 18
maior_idade = idade > 18

if not bloqueado and maior_idade and horario_comercial:
    print('liberado')
else:
    print('nao liberado')



# operadores de comparação
# >, <, >=, <=, ==, !=

numeros = [1, 2, 3]
numeros2 = [1, 2, 3]

print(numeros == numeros2) # True

#operador is
print(numeros is numeros2) #False

numeros3 = [1, 2]
numeros4 = numeros3
print(numeros3 is numeros4) #True
print(numeros4 is not numeros3) # False

# operador in
print('a' in 'python') #False

prontuarios = ['ap03323', 'ds324342']
prontuario = 'ap03323'
print(prontuario in prontuarios) #True


#sim, não, talvez
opcao = ''
if opcao == 'sim' or opcao == 'nao' or opcao == 'talvez':
    print('opcao valida')
else:
    print('opcao invalida')


opcoes = ('sim', 'nao', 'talvez')
if opcao in opcoes:
    print('opcao valida')
else:
    print('opcao invalida')