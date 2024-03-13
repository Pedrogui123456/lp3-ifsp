# Funções
# Modularizar o programa
# Reuso
# Manutenabilidade (correção de erros e novas funcionalidades)


# Declaração
def ola_mundo():
    print("Olá mundo")

# Chamada
ola_mundo()

# Função sem retorno
# Side efect - Efeito colateral
def imprimir_mensagem(nome):
    print(f"Bom dia, {nome}")


imprimir_mensagem('José')

# Função com retorno
# Função pura
def mensagem(nome):
    return(f"Bom dia, {nome}")

print(mensagem("Maria"))

# Parametros e argumentos
def somar(numero1, numero2):
    return numero1 + numero2

numero = 3.0
somar(10.0, numero)

# somar(10.0, somar(2,3))
# somar(10.0, 5)
# 15

# Escopo de variáveis
def media(nota1, nota2, nota3):
    total = nota1 + nota2 + nota3
    return total / 3

# print(total)

# Prametros com valor padrão
def mensagem(nome, mensagem='Bom dia'):
    return f"(mensagem), {nome}."

mensagem('Marcos', 'Bom dia')
mensagem('Kátia', 'Boa noite')
mensagem('Pedro')

# Argumentos nomeados
print('Óla', '123', 'teste', sep='@', end='\n\n' )
print('TESTE')

mensagem(nome='Lucas', mensagem='Boa tarde')
mensagem(mensagem='Boooa tarde', nome='Lucas')

# docstring
# comentário de documentação

def somar(n1, n2):
    '''
    Função que soma dois números

    :param n1: primeiro número
    :param n2: segundo número
    :return: soma dos números
    '''
    return n1 + n2

def media(*notas):
    return sum(notas) / len(notas)
   
print(media(10.0, 7.8, 8.8))
print(media(10.0, 7.8, 8.8, 7.0))
print(media(10.0))

