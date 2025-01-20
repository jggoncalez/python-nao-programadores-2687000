# Crie uma lista apenas com elementos numéricos
numbList = [0, 1, 2, 3, 4, 5]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
dataList = ['test', True, [1, 'jan', 1970], 123, False]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(dataList[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(numbList[0:-1:2])

# Remova da lista o último item
dataList.pop()
print(dataList)

# Insira na lista um novo item
numbList.append(6)
print(numbList)

# Remova da lista um item específico
dataList.remove('test')
print(dataList)