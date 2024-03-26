import random

def escolher_palavra():
    palavras = ["banana", "abacaxi", "morango", "laranja", "uva", "maça"]  # Lista de palavras
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = ["_"] * len(palavra)  # Lista para armazenar as letras corretas adivinhadas
    tentativas_maximas = 6  # Número máximo de tentativas
    tentativas = 0  # Contador de tentativas

    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra secreta.")

    while tentativas < tentativas_maximas and "_" in letras_certas:
        print("\nPalavra: " + " ".join(letras_certas))  # Exibe a palavra com as letras adivinhadas
        letra = input("Digite uma letra: ").lower()

        if len(letra) == 1 and letra.isalpha():
            if letra in palavra:
                print("Letra correta!")
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        letras_certas[i] = letra
            else:
                print("Letra incorreta.")
                tentativas += 1
        else:
            print("Por favor, digite uma única letra válida.")

    if "_" not in letras_certas:
        print("\nParabéns! Você venceu! A palavra era:", palavra)
    else:
        print("\nVocê perdeu! A palavra correta era:", palavra)

jogar_forca()
