# Declare 4 variáveis do tipo numérica
x = 0
y = 4
z = 12
a = 5

# Crie uma estrutura condicional para comparar dois números
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
# Insira outras condições na estrutura condicional usando o elif
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"

if (x > y) and (a > y):
  print(f'O valor {x} e {a} são maiores que {y}.')

elif (z > a) or (a > x):
  print(f'O valor {z} é maior que {a} ou {a} é maior que {x}.')

else:
  print('Nenhuma condição é verdadeira')

if (x < y) and (z > a):
  print(f'O valor {x} é menor que {y} e {z} é maior que {a}.')
else:
  print('Nenhuma condição é verdadeira.')
