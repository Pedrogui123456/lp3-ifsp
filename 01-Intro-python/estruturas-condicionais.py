#if, if/else, if/elif/else, ternario, match

#if
# if condicao:
#   codigo do if

idade = 20
if idade >= 18:
    print('maior de idade')

print('fora do if')


#if/else
idade = 20
if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')


#elif
#crianca = 0 12, adolescente = 13 17, adulto = 18 59. idoso = 60+
idade = 30
if idade <= 12:
    print('crianca')
elif idade <= 17:
    print('adolescente')
elif idade <= 59:
    print('adulto')
else:
    print('idoso')


# evitar aninhar ifs

email = ''
senha = ''

if email == 'admin@gmail.com':
    if senha == '123admin':
        print('liberado')
    else:
        print('email ou senha incorretos')
else:
    print('email ou senha incorretos')

if email == 'admin@gmail.com' and senha == '123admin':
    print('liberado')
else:
    print('email ou senha incorretos')



#entrada numero 1, 2, 3...
#saida dia: Domingo, segunda, terça ... sábado

dia = 4
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terça')
elif dia == 4:
    print("Quarta")
else:
    print('Outro')


dias = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sábado'
}
if dia in dias:
    print(dias[dia])
else:
    print('dia invalido')


# ternario
media = 8.0
if media >= 6.0:
    situacao = 'aprovado'
else:
    situacao = 'reprovado'

situacao = 'aprovado' if media >= 6 else 'reprovado'


# match

match dia:
    case 1:
        print('domingo')
    case 2:
        print('SEgunda')
    case 3:
        print('terça')
    case _:
        print('invalido')

#dia util: 2, 3, 4, 5, 6
#fim de semana: 7, 1
match dia:
    case 1 | 7:
        print('fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('dia util')
    case _:
        print('invalido')