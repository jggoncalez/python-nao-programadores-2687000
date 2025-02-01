# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

cursos = {"Python para não programadores", 
          "Fundamentos da Gestão de projetos",
          "Git e Github",
          "Fundamentos API Rest",
          "Fundamentos SQL Server" }

cursoGit = "Git e Github"
cursoCyber = "Cybersegurança"
cursoPy = "Python para não programadores"

cursoNotas = {}

if cursoGit in cursos:
  print(f'O curso "{cursoGit}" está na lista de cursos, por favor dê uma avaliação: ')
  cursoNotas[cursoGit] = int(input("Qual nota você dá para esse curso (de 0 a 5)? "))

if cursoCyber in cursos:
  print(f'O curso "{cursoCyber}" está na lista de cursos, por favor dê uma avaliação: ')
  cursoNotas[cursoCyber] = int(input("Qual nota você dá para esse curso (de 0 a 5)? "))

if cursoGit in cursos:
  print(f'O curso "{cursoPy}" está na lista de cursos, por favor dê uma avaliação: ')
  cursoNotas[cursoPy] = int(input("Qual nota você dá para esse curso (de 0 a 5)? "))

else:
  print("Este curso não está disponível na lista de cursos.")

print(cursoNotas)