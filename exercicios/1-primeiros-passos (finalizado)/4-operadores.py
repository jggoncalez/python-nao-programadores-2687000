ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
print(f'Gerlaine tem',ano_formatura-ano_nascimento,'anos de idade.')

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento>ano_formatura)
print(1092 <= 1010)
print(ano_nascimento == 1989)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print((ano_nascimento > ano_formatura) and (ano_formatura != 2010))
print((ano_formatura >= 300) or (ano_nascimento == 0))
print(not(ano_nascimento < ano_formatura))