# Função para calcular a média de uma lista de notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para determinar se o aluno está aprovado
def verificar_aprovacao(media):
    return media >= 7
