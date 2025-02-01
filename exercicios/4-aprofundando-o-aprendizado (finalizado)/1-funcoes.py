# Crie uma função para selecionar o curso desejado em uma trilha profissional
def curso():
  curso = int(input('''Selecione o curso desejado:
                    1. Gestão de projetos
                    2. Python: formação básica '''))
  return curso
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
def cursoNivel(cursoSelect):

  trilha = {1: {'title': 'Gestão de projetos', 'nivelFinal': 3 }, 2: {'title': 'Python: formação básica', 'nivelFinal': 5}}
  
  cursoAtual = trilha[cursoSelect]['title']
  nivelAtual = 1
  nivelFinal = trilha[cursoSelect]['nivelFinal']

  print(f'Bem-vindo ao curso {cursoAtual}, você começará no nível {nivelAtual}.')

  while nivelAtual <= nivelFinal:
    print(f'Você está no nível {nivelAtual} no {cursoAtual}!')
    nivelAtual += 1

  else:
    print(f'Você finalizou o curso {cursoAtual} com sucesso!')


          
# Execute as funções
course = curso()
cursoNivel(course)
