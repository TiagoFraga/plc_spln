import os

def showMenuPrincipal():
    print('\n\n################# Menu #################\n\n')
    print('1 - Obter Soluções')
    print('2 - Adicionar')
    print('3 - Sair\n\n')

def showMenu_Inicializacao():
    print('\n\n################# Escolher Solver #################\n\n')
    print(' 1 - Solver Default')
    print(' 2 - Backtraking Solver')
    print(' 3 - Min Conflit Solver')
    print(' 4 - Recursive Backtracking Solver')
    print(' 5 - Voltar\n\n')

def showMenu_Constraints():
    print('\n\n################# Ativar Restrições #################\n\n')
    print(' 1 - Diferença de Datas de Nascimento entre Pai e Filho')
    print(' 2 - Intervalo de Nascimento entre Mae e Filho')
    print(' 3 - Filho nasce antes da data de Morte dos pais')
    print(' 4 - Avo - Neto')
    print(' 5 - Pai - Filho')
    print(' 6 - Mae - Filho')
    print(' 7 - Casados')
    print(' 8 - Todas Ativas')
    print(' 9 - Nenhumas Restrições')
    print(' 10 - Voltar\n\n')
    print(' Ex: 1,2,3 ou 4 ou 5\n')

def showMenu_Adicionar():
    print('\n\n################# Adicionar #################\n\n')
    print(' 1 - Filho')
    print(' 2 - Pai')
    print(' 3 - Mae')
    print(' 4 - Avô')
    print(' 5 - Avó')
    print(' 6 - Voltar \n\n')

