# Exercício 01
def ant_suc(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor


print(ant_suc(22))
print(ant_suc(44))

# Exercício 02
def media(*notas):
    return sum(notas) / len(notas)

print(media(10.0, 7.7, 8.0))

# Exercício 03
compras = (int(input("Digite um numero:")))

if compras >= 0.1 and compras <= 9.99:
    desconto = 0
    valor_total = desconto + compras
elif compras >= 10.0 and compras <= 99.99:
    desconto = 5
    valor_total = 
elif compras >= 100.00 and compras <= 499.99:
    valor_total = compras * 0.10
elif compras >= 500.00:
    valor_total = compras * 0.15

print(valor_total)
  



# Exercício 04

