# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.

nome = input('Insira o seu nome: ')
total_dias = input('Quantos dias você estuda por semana? ')
total_horas = input('Qual a sua média de horas estudada por dia? ')
curso = input ('Qual o nome do curso? ')

total_dias = int(total_dias)
total_horas = int(total_horas)


print(f'Ok, o seu nome é {nome}, você dedica {total_dias} dia(s) por semana, estudando {total_horas} hora(s) por dia no curso, tendo como total {total_dias*total_horas} hora(s) estudada(s) por semana no curso {curso}.')