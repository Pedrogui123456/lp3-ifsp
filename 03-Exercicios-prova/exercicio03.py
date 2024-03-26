def contar_vogais_consoantes(mensagem):
    vogais = ["a", "e", "i", "o", "u"]
    cont_vogais = cont_consoantes = 0

    for c in range(0, len(mensagem)):
        if mensagem[c] in vogais:
            cont_vogais += 1
        else:
            cont_consoantes += 1

    return f'Vogais: {cont_vogais}; Consoantes: {cont_consoantes}'


print(contar_vogais_consoantes("Pedro"))