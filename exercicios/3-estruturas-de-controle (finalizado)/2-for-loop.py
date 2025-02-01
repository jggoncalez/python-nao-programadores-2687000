# Crie uma lista
cursos = {"Python para não programadores", 
          "Fundamentos da Gestão de projetos",
          "Git e Github",
          "Fundamentos API Rest",
          "Fundamentos SQL Server" }
# Crie um for loop para imprimir cada elemento dessa lista
for item in cursos:
  print(item)

# Crie um objeto iterável utilizando a função range()
rangeList = range(7)

# Use esse objeto iterável para criar um for loop que imprima na tela a frase "Estou aprendendo uma linguagem de programação."
for numb in rangeList:
  print(f'{numb} - Estou aprendendo uma linguagem de programação.')