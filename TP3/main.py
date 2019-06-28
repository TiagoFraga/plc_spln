import interface
import baseDeConhecimento as base
import prologFunctions as prol
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
                    interface.showMenu_Prolog()
                    opcao2 = int(input("Escolha a sua opcao: "))
                        

            else:
                if opcao == 3:
                    break
                else:
                    print('\nOpcao Invalida!!!\n')


main()
