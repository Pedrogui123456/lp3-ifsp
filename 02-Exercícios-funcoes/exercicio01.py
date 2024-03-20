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

def calcular_desconto(compra):
    if 0.01 <= compra < 10:
        desconto = 0
    elif 10 <= compra < 100:
        desconto = 5
    elif 100 <= compra < 500:
        desconto = 10
    else:
        desconto = 15
    return desconto

compra = float(input("Digite o valor da compra: "))

desconto = calcular_desconto(compra)
valor_desconto = compra * (desconto / 100)
valor_total = compra - valor_desconto

print("Valor final com desconto: R$", valor_total)

    
# Exercício 04 e 05
def identificador(codigo):
    if len(codigo) != 7:
        return False
    if codigo[:2] != 'BR':
        return False
    if not codigo[2:6].isdigit():
        return False
    numero = int(codigo[2:6])
    if numero < 1 or numero > 9999:
        return False
    if codigo[-1] != 'X':
        return False
    return True

codigo = input("Digite seu identificador: ")
if identificador(codigo):
    print("Código válido!")
else:
    print("Código inválido!")

# Exercício 06
def calcular_informacoes_aquario(comprimento, altura, largura, temperatura_desejada, temperatura_ambiente):
    volume = (comprimento * altura * largura) / 1000
    potencia_termostato = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
    filtragem_por_hora = 2 * volume  
    return volume, potencia_termostato, filtragem_por_hora

comprimento = float(input("Digite o comprimento do aquário (cm): "))
altura = float(input("Digite a altura do aquário (cm): "))
largura = float(input("Digite a largura do aquário (cm): "))
temperatura_desejada = float(input("Digite a temperatura desejada (°C): "))
temperatura_ambiente = float(input("Digite a temperatura ambiente (°C): "))

volume, potencia_termostato, filtragem_por_hora = calcular_informacoes_aquario(comprimento, altura, largura, temperatura_desejada, temperatura_ambiente)

print("Volume do aquário:", volume, "litros")
print("Potência do termostato necessária:", potencia_termostato, "Watts")
print("Quantidade de filtragem por hora necessária:", filtragem_por_hora, "litros por hora")

# Exercício 07
def calcular_imc(peso, altura):
    return peso / (altura * altura)

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc < 25.0:
        return "Peso normal"
    elif 25.0 <= imc < 30.0:
        return "Excesso de peso"
    elif 30.0 <= imc < 35.0:
        return "Obesidade de Classe 1"
    elif 35.0 <= imc < 40.0:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"

def diferenca_peso_normal(peso, altura):
    imc_atual = calcular_imc(peso, altura)
    peso_normal = 24.9 * altura * altura
    diferenca = peso_normal - peso
    return diferenca

peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
diferenca = diferenca_peso_normal(peso, altura)

print("Seu IMC é:", imc)
print("Você está classificado como:", classificacao)

if diferenca > 0:
    print("Você precisa ganhar", diferenca, "Kg para atingir o peso normal.")
elif diferenca < 0:
    print("Você precisa perder", abs(diferenca), "Kg para atingir o peso normal.")
else:
    print("Você está no peso normal!")
