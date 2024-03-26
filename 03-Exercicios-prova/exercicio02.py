def tabuada():
    num = int(input("Digite um número para saber sua tabuada até 10:"))
    for c in range(0,11):
        print(f"{num} x {c} = {num * c}")

tabuada()