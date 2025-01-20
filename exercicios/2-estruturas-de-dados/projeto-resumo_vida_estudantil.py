# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcorridos, total de cursos realizados e (apenas) o primeiro e último curso.

eData = {}

eData['nome'] = input('Insira o seu nome: ')
eData['anoLink'] = int(input('Em qual ano você conheceu o Linkedin? '))
cursos = input('Quais cursos você já realizou na plataforma "Linkedin Learning"? Por favor, separe com vírgula (, ')
eData['anoAtual'] = int(input('Qual ano atualmente estamos? '))

eData['cursos'] = cursos.split(', ')

print(f"Olá {eData['nome']}, você conhece o Linkedin desde {eData['anoLink']}. E nesses {eData['anoAtual'] - eData['anoLink']} anos, você realizou {len(eData['cursos'])} cursos, sendo o primeiro o curso '{eData['cursos'][0]}' e o mais recente '{eData['cursos'][-1]}'.")