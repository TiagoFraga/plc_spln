from constraint import *
import constraintFunctions as const
import json

def carregarVariaveis(problem):
    file_open = open('teste.json','r')
    data = json.load(file_open)
    listaFilho = []
    listaPai = []
    listaMae = []
    listaAvoM = []
    listaAvoF = []
    listaTios = []
    for d in data:
        if d["tipo"] == "filho":
            aux = {
                "nome" : d["nome"],
                "dataNasc": d["dataNasc"],
                "dataMorte": d["dataMorte"]
            }
            listaFilho.append(aux)
        else:
            if d["tipo"] == "pai":
                aux = {
                    "nome" : d["nome"],
                    "dataNasc": d["dataNasc"],
                    "dataMorte": d["dataMorte"],
                    "ePai": d["ePai"]
                }
                listaPai.append(aux)
            else:
                if d["tipo"] == "mae":
                    aux = {
                        "nome" : d["nome"],
                        "dataNasc": d["dataNasc"],
                        "dataMorte": d["dataMorte"],
                        "eMae": d["eMae"]
                    }
                    listaMae.append(aux)
                else:
                    if d["tipo"] == "avo_m":
                        aux = {
                            "nome" : d["nome"],
                            "dataNasc": d["dataNasc"],
                            "dataMorte": d["dataMorte"],
                            "ePai": d["ePai"],
                            "eAvo": d["eAvo"]
                        }
                        listaAvoM.append(aux)
                    else:
                        if d["tipo"] == "avo_f":
                            aux = {
                                "nome" : d["nome"],
                                "dataNasc": d["dataNasc"],
                                "dataMorte": d["dataMorte"],
                                "eMae": d["eMae"],
                                "eAvo": d["eAvo"]
                            }
                            listaAvoF.append(aux)
                        else:
                            if d["tipo"] == "tio":
                                aux = {
                                    "nome" : d["nome"],
                                    "dataNasc": d["dataNasc"],
                                    "dataMorte": d["dataMorte"],
                                    "eIrmao": d["eIrmao"],
                                }
                                listaTios.append(aux)
    problem.addVariable("filho", listaFilho)
    problem.addVariable("pai", listaPai)
    problem.addVariable("mae", listaMae)
    problem.addVariable("avo_m", listaAvoM)
    problem.addVariable("avo_f",listaAvoF)
    problem.addVariable("tio",listaTios)


# Solvers
def get_solver_default(flags):
    problem = Problem()

    carregarVariaveis(problem)

    # 1 - Intervalo de Nascimento entre Pai e Filho
    print(flags)
    if 1 in flags or 4 in flags:
        problem.addConstraint(lambda filho, pai: int(filho["dataNasc"].split('-')[2]) > int(pai["dataNasc"].split('-')[2]) + 10,("filho", "pai"))
        problem.addConstraint(const.dataNasc_avo_m_filho,("avo_m", "pai","mae"))
        problem.addConstraint(const.intervalo_avo_m_tio,("avo_m","pai","mae","tio"))

    # 2 - Intervalo de Nascimento entre Mae e Filho
    if 2 in flags or 4 in flags:
        problem.addConstraint(const.intervalo_mae_filho,("mae", "filho"))
        problem.addConstraint(const.intervalo_avo_f_pai_mae,("avo_f", "pai","mae"))
        problem.addConstraint(const.intervalo_avo_f_tio,("avo_f","pai","mae","tio"))
    
    # 3 - Filho nasce antes da Data de Morte
    if 3 in flags or 4 in flags:
        problem.addConstraint(const.dataMorte_filho_pais,("filho","mae","pai"))
        problem.addConstraint(const.dataMorte_avo_mae,("avo_m","avo_f","mae"))
        problem.addConstraint(const.dataMorte_avo_pai,("avo_m","avo_f","pai"))

    # Não faz sentido

    # problem.addConstraint(const.avo_m_neto,("avo_m","mae","pai","filho"))
    # problem.addConstraint(const.avo_f_neto,("avo_f","mae","pai","filho"))

    results = problem.getSolutions()
    if results == []:
        return 'Não foram obtidos resultados com estas restrições'
    else: 
        return results

def get_backtracking_solver(flags):
    problem = Problem(BacktrackingSolver())

    carregarVariaveis(problem)

    # 1 - Intervalo de Nascimento entre Pai e Filho
    
    if 1 in flags or 4 in flags:
        problem.addConstraint(lambda filho, pai: int(filho["dataNasc"].split('-')[2]) > int(pai["dataNasc"].split('-')[2]) + 10,("filho", "pai"))
        problem.addConstraint(const.dataNasc_avo_m_filho,("avo_m", "pai","mae"))
        problem.addConstraint(const.intervalo_avo_m_tio,("avo_m","pai","mae","tio"))

    # 2 - Intervalo de Nascimento entre Mae e Filho
    if 2 in flags or 4 in flags:
        problem.addConstraint(const.intervalo_mae_filho,("mae", "filho"))
        problem.addConstraint(const.intervalo_avo_f_pai_mae,("avo_f", "pai","mae"))
        problem.addConstraint(const.intervalo_avo_f_tio,("avo_f","pai","mae","tio"))
    
    # 3 - Filho nasce antes da Data de Morte
    if 3 in flags or 4 in flags:
        problem.addConstraint(const.dataMorte_filho_pais,("filho","mae","pai"))
        problem.addConstraint(const.dataMorte_avo_mae,("avo_m","avo_f","mae"))
        problem.addConstraint(const.dataMorte_avo_pai,("avo_m","avo_f","pai"))

    # Não faz sentido

    # problem.addConstraint(const.avo_m_neto,("avo_m","mae","pai","filho"))
    # problem.addConstraint(const.avo_f_neto,("avo_f","mae","pai","filho"))
    
    results = problem.getSolutions()
    if results == []:
        return 'Não foram obtidos resultados com estas restrições'
    else: 
        return results

def get_min_conflit_solver(flags):
    problem = Problem(MinConflictsSolver())

    carregarVariaveis(problem)

    # 1 - Intervalo de Nascimento entre Pai e Filho
    
    if 1 in flags or 4 in flags:
        problem.addConstraint(lambda filho, pai: int(filho["dataNasc"].split('-')[2]) > int(pai["dataNasc"].split('-')[2]) + 10,("filho", "pai"))
        problem.addConstraint(const.dataNasc_avo_m_filho,("avo_m", "pai","mae"))
        problem.addConstraint(const.intervalo_avo_m_tio,("avo_m","pai","mae","tio"))

    # 2 - Intervalo de Nascimento entre Mae e Filho
    if 2 in flags or 4 in flags:
        problem.addConstraint(const.intervalo_mae_filho,("mae", "filho"))
        problem.addConstraint(const.intervalo_avo_f_pai_mae,("avo_f", "pai","mae"))
        problem.addConstraint(const.intervalo_avo_f_tio,("avo_f","pai","mae","tio"))
    
    # 3 - Filho nasce antes da Data de Morte
    if 3 in flags or 4 in flags:
        problem.addConstraint(const.dataMorte_filho_pais,("filho","mae","pai"))
        problem.addConstraint(const.dataMorte_avo_mae,("avo_m","avo_f","mae"))
        problem.addConstraint(const.dataMorte_avo_pai,("avo_m","avo_f","pai"))

    # Não faz sentido

    # problem.addConstraint(const.avo_m_neto,("avo_m","mae","pai","filho"))
    # problem.addConstraint(const.avo_f_neto,("avo_f","mae","pai","filho"))

    results = problem.getSolution()
    if results == None:
        return 'Não foram obtidos resultados com estas restrições'
    else: 
        return results

def get_recursive_backtraking_solver(flags):
    problem = Problem(RecursiveBacktrackingSolver())

    carregarVariaveis(problem)

    # 1 - Intervalo de Nascimento entre Pai e Filho
    
    if 1 in flags or 4 in flags:
        problem.addConstraint(lambda filho, pai: int(filho["dataNasc"].split('-')[2]) > int(pai["dataNasc"].split('-')[2]) + 10,("filho", "pai"))
        problem.addConstraint(const.dataNasc_avo_m_filho,("avo_m", "pai","mae"))
        problem.addConstraint(const.intervalo_avo_m_tio,("avo_m","pai","mae","tio"))

    # 2 - Intervalo de Nascimento entre Mae e Filho
    if 2 in flags or 4 in flags:
        problem.addConstraint(const.intervalo_mae_filho,("mae", "filho"))
        problem.addConstraint(const.intervalo_avo_f_pai_mae,("avo_f", "pai","mae"))
        problem.addConstraint(const.intervalo_avo_f_tio,("avo_f","pai","mae","tio"))
    
    # 3 - Filho nasce antes da Data de Morte
    if 3 in flags or 4 in flags:
        problem.addConstraint(const.dataMorte_filho_pais,("filho","mae","pai"))
        problem.addConstraint(const.dataMorte_avo_mae,("avo_m","avo_f","mae"))
        problem.addConstraint(const.dataMorte_avo_pai,("avo_m","avo_f","pai"))

    # Não faz sentido

    # problem.addConstraint(const.avo_m_neto,("avo_m","mae","pai","filho"))
    # problem.addConstraint(const.avo_f_neto,("avo_f","mae","pai","filho"))

    results = problem.getSolutions()
    if results == []:
        return 'Não foram obtidos resultados com estas restrições'
    else: 
        return results