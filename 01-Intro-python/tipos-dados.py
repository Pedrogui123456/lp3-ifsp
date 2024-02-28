# Tipos de dados

# Númerico

# int
idade = 17

# float
altura = 1.85

# Booleano
# True; False
verdade = True
mentira = False
ligado = True
frete_gratis = True

# str = string
# sequência de caracteres
# literal de str
nome = "Pedro"
nome = 'Pedro'

# char
letra = "a"

# multilinhas
frase = """
Óla Pessoal
"""

# interpolação de string
nome = "Sonia"
idade = 23

# f-string
mensagem = f"Bom dia {nome}. Você tem {idade} anos!"

nome = "Cristiano Ronaldo"
print(nome[2])
print(nome[-3])
print(nome[0:3])

# str são objetos
# métodos
print(nome.upper())
print(nome)

# listas
# lista de valores
# pode conter valores de tipos diferentes
# podem ser alteradas (adicionar, remover)
habilidades = ["java", "html", "css"]
print(habilidades[0])

habilidades[0] = "javascript"
print(habilidades)

# adicionar no final
habilidades.append("python")
print(habilidades)

# adicionar em uma posição
habilidades .insert(0, "kotlin")
print(habilidades)

# remove, sort, clear, copy ...

for habilidade in habilidades:
    print(habilidade)


# tuple
# lista de valores
# não pode alterar os valores
opcoes = ("sim", "não", "talvez")
racas_rpg = ("anão", "humano", "elfo")

print(opcoes[1])

# função que retorna estatisticas
# sobre as notas de um aluno
# média, menor nota, maior nota
# entrada: n1, n2, n3 ou notas (list)
# saídas: media, menor nota, maior nota
def estatistica_nota(notas):
    media = sum(notas) / len(notas)
    menor = min(notas)
    maior = max(notas)
    return media, menor, maior

notas = [10.0 , 5.5, 3.2, 1.8]
estatistica = estatistica_nota(notas)
print(estatistica)
print(type(estatistica))

# desempacotamento de tupla
media, menor, maior = estatistica_nota(notas)
print(media, menor, maior)

# set
# conjunto de valores
# não permite valores duplicados
# não é indexado
habilidades = {"java", "python", "css"}
habilidades.add("java")
print(habilidades)

# dict
# dicionário
# palavras
# palavra => definição
# chave => valor
# key => value
nome = "Cristiano Ronaldo"
casado = True
idade = 38

pessoa = {
    "nome": "Cristiano Ronaldo",
    "casado": True,
    "idade": 120
}

print(pessoa["nome"])
print(pessoa["casado"])
print(pessoa["idade"])

pessoa["rico"] = True
print(pessoa)

# None
# null
nulo = None