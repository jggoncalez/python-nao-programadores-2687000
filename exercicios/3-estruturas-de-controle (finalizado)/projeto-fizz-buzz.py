# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números
# 2. Crie um for loop para percorrer todos os elementos da lista
# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"

numbList = list(range(15))
print(numbList)

for number in numbList:
  if number %3 == 0 and number / 5:
    numbList[number] = 'FizzBuzz'

  elif number %3 == 0:
    numbList[number] = 'Fizz'

  elif number %5 == 0:
    numbList[number] = 'Buzz'

  else:
    {}

print(numbList)