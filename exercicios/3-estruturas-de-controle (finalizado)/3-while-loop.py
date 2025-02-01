# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
nivelAtual = 1
nivelFinal = 9

# Crie um while loop que imprima na tela o nível atual
while nivelAtual <= nivelFinal:
  print(f'Seu nível atual é {nivelAtual}')
  nivelAtual += 1

# Insira "else" no while loop anterior.
else:
  print('Parabéns! Você concluiu o curso!')