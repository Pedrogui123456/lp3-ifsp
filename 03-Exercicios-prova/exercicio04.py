def simulador_eleicoes():
    candidatos = {"Candidato 1": 0, "Candidato 2": 0, "Candidato 3": 0}

    print("Bem-vindo ao Simulador de Eleições!")
    total_votos = int(input("Quantas pessoas irão votar? "))

    for i in range(total_votos):
        print("\nCandidatos Disponíveis:")
        for candidato in candidatos:
            print(f"- {candidato}")
        
        voto = input("\nDigite o nome do candidato em quem deseja votar: ")
        if voto in candidatos:
            candidatos[voto] += 1
            print("Voto registrado com sucesso!")
        else:
            print("Candidato inválido. Voto não registrado.")

    print("\nResultado da Eleição:")
    for candidato, votos in candidatos.items():
        print(f"{candidato}: {votos} votos")

    vencedor = max(candidatos, key=candidatos.get)
    print(f"\nO vencedor da eleição é: {vencedor} com {candidatos[vencedor]} votos!")

simulador_eleicoes()
