import interface
import baseDeConhecimento as base
from constraint import *
import os


def main():
    while True :
        interface.showMenuPrincipal()
        opcao = int(input("Escolha a sua opcao: "))
        if opcao == 1:
            while True:
                interface.showMenu_Inicializacao()
                opcao2 = int(input("Escolha a sua opcao: "))
                if opcao2 == 1:
                    while(True):
                        interface.showMenu_Constraints()
                        opcao3 = input("Escolha as suas opcao: ")
                        if ',' in opcao3:
                            flags = opcao3.split(',')
                            flags = [int(x) for x in flags]
                            print(base.get_solver_default(flags))
                        else:
                            if int(opcao3) == 6:
                                    break
                            else:
                                num = int(opcao3)    
                                flags = [int(x) for x in str(num)]
                                print(base.get_solver_default(flags))
                else:
                    if opcao2 == 2:
                        while True:
                            interface.showMenu_Constraints()
                            opcao3 = input("Escolha as suas opcao: ")
                            if ',' in opcao3:
                                flags = opcao3.split(',')
                                flags = [int(x) for x in flags]
                                print(base.get_backtracking_solver(flags))
                            else:
                                if int(opcao3) == 6:
                                    break
                                else:
                                    num = int(opcao3)    
                                    flags = [int(x) for x in str(num)]
                                    print(base.get_backtracking_solver(flags))
                    else:
                        if opcao2 == 3:
                            while True:
                                interface.showMenu_Constraints()
                                opcao3 = input("Escolha as suas opcao: ")
                                if ',' in opcao3:
                                    flags = opcao3.split(',')
                                    flags = [int(x) for x in flags]
                                    print(base.get_min_conflit_solver(flags))
                                else:
                                    if int(opcao3) == 6:
                                        break
                                    else:
                                        num = int(opcao3)    
                                        flags = [int(x) for x in str(num)]
                                        print(base.get_min_conflit_solver(flags))
                        else:
                            if opcao2 == 4:
                                while True:
                                    interface.showMenu_Constraints()
                                    opcao3 = input("Escolha as suas opcao: ")
                                    if ',' in opcao3:
                                        flags = opcao3.split(',')
                                        flags = [int(x) for x in flags]
                                        print(base.get_recursive_backtraking_solver(flags))
                                    else:
                                        if int(opcao3) == 6:
                                            break
                                        else:
                                            num = int(opcao3)    
                                            flags = [int(x) for x in str(num)]
                                            print(base.get_recursive_backtraking_solver(flags))
                            else:
                                if opcao2 == 5:
                                    break
                                else:
                                    print('\nOpcao Invalida!!!\n')
        else:
            if opcao == 2:
                while True:
                    interface.showMenu_Adicionar()
                    opcao2 = int(input("Escolha a sua opcao: "))
                    if opcao2 == 1:
                        nome = input("Nome do Filho: ")
                        dataNasc = input("Data de Nascimento(DD-MM-AAAA): ")
                        dataMorte = input("Data de Morte(DD-MM-AAAA): ")
                        if dataMorte == '':
                            dataMorte = '10-10-2100'
                        filho = {
                            "tipo":"filho",
                            "nome": nome,
                            "dataNasc": dataNasc,
                            "dataMorte": dataMorte
                        }
                        base.addFilho(filho)        
                    else:
                        if opcao2 == 2:
                            nome = input("Nome do Pai: ")
                            dataNasc = input("Data de Nascimento(DD-MM-AAAA): ")
                            dataMorte = input("Data de Morte(DD-MM-AAAA): ")
                            if dataMorte == '':
                                dataMorte = '10-10-2100'
                            nFilhos = int(input("Número de Filhos :"))
                            ePais = []
                            for i in range(0, nFilhos):
                                ePai = input("Nome do Filho: ")
                                ePais.append(ePai)
                            pai = {
                                "tipo":"pai",
                                "nome": nome,
                                "dataNasc": dataNasc,
                                "dataMorte": dataMorte,
                                "ePai": ePais
                            }
                            base.addPai(pai)
                        else:
                            if opcao2 == 3:
                                nome = input("Nome do Mae: ")
                                dataNasc = input("Data de Nascimento(DD-MM-AAAA): ")
                                dataMorte = input("Data de Morte(DD-MM-AAAA): ")
                                if dataMorte == '':
                                    dataMorte = '10-10-2100'
                                nFilhos = int(input("Número de Filhos :"))
                                eMaes = []
                                for i in range(0, nFilhos) :
                                    eMae = input("Nome do Filho:")
                                    eMaes.append(eMae)
                                mae = {
                                    "tipo":"mae",
                                    "nome": nome,
                                    "dataNasc": dataNasc,
                                    "dataMorte": dataMorte,
                                    "eMae": eMaes
                                }
                                base.addMae(mae)
                            else:
                                if opcao2 == 4:
                                    nome = input("Nome do Avô: ")
                                    dataNasc = input("Data de Nascimento(DD-MM-AAAA): ")
                                    dataMorte = input("Data de Morte(DD-MM-AAAA): ")
                                    if dataMorte == '':
                                        dataMorte = '10-10-2100'
                                    nFilhos = int(input("Número de Filhos :"))
                                    ePais = []
                                    for i in range(0, nFilhos) :
                                        ePai = input("Nome do Filho: ")
                                        ePais.append(ePai)
                                    eAvos = []
                                    nNetos = int(input("Número de Netos :"))
                                    for i in range(0, nNetos):
                                        eAvo = input("Nome do Neto: ")
                                        eAvos.append(eAvo)
                                    avo_m = {
                                        "tipo":"avo_m",
                                        "nome": nome,
                                        "dataNasc": dataNasc,
                                        "dataMorte": dataMorte,
                                        "ePai": ePais,
                                        "eAvo": eAvos
                                    }
                                    base.addAvo_M(avo_m)
                                else:
                                    if opcao2 == 5:
                                        nome = input("Nome da Avó: ")
                                        dataNasc = input("Data de Nascimento(DD-MM-AAAA): ")
                                        dataMorte = input("Data de Morte(DD-MM-AAAA): ")
                                        if dataMorte == '':
                                            dataMorte = '10-10-2100'
                                        nFilhos = int(input("Número de Filhos :"))
                                        eMaes = []
                                        for i in range(0, nFilhos):
                                            eMae = input("Nome do Filho:")
                                            eMaes.append(eMae)
                                        eAvos = []
                                        nNetos = int(input("Número de Netos :"))
                                        for i in range(0, nNetos):
                                            eAvo = input("Nome do Neto: ")
                                            eAvos.append(eAvo)
                                       
                                        avo_f = {
                                            "tipo":"avo_f",
                                            "nome": nome,
                                            "dataNasc": dataNasc,
                                            "dataMorte": dataMorte,
                                            "eMae": eMaes,
                                            "eAvo": eAvos
                                        }
                                        base.addAvo_F(avo_f)
                                    else:
                                        if opcao2 == 6:
                                            break
                                        else:
                                            print('\nOpcao Invalida!!!\n')
            else:
                if opcao == 3:
                    break
                else:
                    print('\nOpcao Invalida!!!\n')


main()
