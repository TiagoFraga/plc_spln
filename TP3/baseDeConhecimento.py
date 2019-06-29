from constraint import *
import constraintFunctions as const
import json

# Funções de Adicionar

def addFilho(filho):
    file_open = open('teste.json','r')
    data = json.load(file_open)
    if filho in data:
        return False
    else:
        data.append(filho)
        with open('teste.json', 'w') as outfile:  
            json.dump(data, outfile)
        return True

def addPai(pai):
    file_open = open('teste.json','r')
    data = json.load(file_open)
    if pai in data:
        return False
    else:
        data.append(pai)
        with open('teste.json', 'w') as outfile:  
            json.dump(data, outfile)
        return True

def addMae(mae):
    file_open = open('teste.json','r')
    data = json.load(file_open)
    if mae in data:
        return False
    else:
        data.append(mae)
        with open('teste.json', 'w') as outfile:  
            json.dump(data, outfile)
        return True

def addAvo_M(avo):
    file_open = open('teste.json','r')
    data = json.load(file_open)
    if avo in data:
        return False
    else:
        data.append(avo)
        with open('teste.json', 'w') as outfile:  
            json.dump(data, outfile)
        return True

def addAvo_F(avo_f):
    file_open = open('teste.json','r')
    data = json.load(file_open)
    if avo_f in data:
        return False
    else:
        data.append(avo_f)
        with open('teste.json', 'w') as outfile:  
            json.dump(data, outfile)
        return True



def carregarVariaveis(problem):
    file_open = open('teste.json','r')
    data = json.load(file_open)
    listaFilho = []
    listaPai = []
    listaMae = []
    listaAvoM = []
    listaAvoF = []
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
    problem.addVariable("filho", listaFilho)
    problem.addVariable("pai", listaPai)
    problem.addVariable("mae", listaMae)
    problem.addVariable("avo_m", listaAvoM)
    problem.addVariable("avo_f",listaAvoF)


# Solvers
def get_solver_default(flags):
    problem = Problem()

    carregarVariaveis(problem)

    # 1 - Restrição entre diferença de Datas de Nascimento entre Pai e Filho
    if 1 in flags or 8 in flags:
        problem.addConstraint(const.dataNascimento_pai_filho,("pai","filho"))
        problem.addConstraint(const.dataNascimento_avo_m_filho,("avo_m", "pai","mae"))

    # 2 - Intervalo de Nascimento entre Mae e Filho
    if 2 in flags or 8 in flags:
        problem.addConstraint(const.dataNascimento_mae_filho,("mae", "filho"))
        problem.addConstraint(const.dataNascimento_avo_f_filho,("avo_f", "pai","mae"))
    
    # 3 - Filho nasce antes da Data de Morte
    if 3 in flags or 8 in flags:
        problem.addConstraint(const.dataMorte_pai_filho,("pai","filho"))
        problem.addConstraint(const.dataMorte_mae_filho,("mae","filho"))
        problem.addConstraint(const.dataMorte_avo_m_filho,("avo_m","pai","mae"))
        problem.addConstraint(const.dataMorte_avo_f_filho,("avo_f","pai","mae"))

    # 4 - Avo - Neto
    if 4 in flags or 8 in flags:
        problem.addConstraint(const.avo_neto,("avo_m","avo_f","filho"))

    # 5 - Pai - Filho
    if 5 in flags or 8 in flags:
        problem.addConstraint(const.pai_filho,("pai","filho"))
        problem.addConstraint(const.avo_m_filho,("avo_m","pai","mae"))

    # 6 - Mae - Filho
    if 6 in flags or 8 in flags:
        problem.addConstraint(const.mae_filho,("mae","filho"))
        problem.addConstraint(const.avo_f_filho,("avo_f","pai","mae"))
    
    # 7 - Casados 
    if 7 in flags or 8 in flags:
        problem.addConstraint(const.casado_pai_mae,("pai","mae"))
        problem.addConstraint(const.casado_avo_m_avo_f,("avo_m","avo_f"))

    results = problem.getSolutions()
    if results == []:
        return 'Não foram obtidos resultados com estas restrições'
    else: 
        return results

def get_backtracking_solver(flags):
    problem = Problem(BacktrackingSolver())

    carregarVariaveis(problem)
    
    # 1 - Restrição entre diferença de Datas de Nascimento entre Pai e Filho
    if 1 in flags or 8 in flags:
        problem.addConstraint(const.dataNascimento_pai_filho,("pai","filho"))
        problem.addConstraint(const.dataNascimento_avo_m_filho,("avo_m", "pai","mae"))

    # 2 - Intervalo de Nascimento entre Mae e Filho
    if 2 in flags or 8 in flags:
        problem.addConstraint(const.dataNascimento_mae_filho,("mae", "filho"))
        problem.addConstraint(const.dataNascimento_avo_f_filho,("avo_f", "pai","mae"))
    
    # 3 - Filho nasce antes da Data de Morte
    if 3 in flags or 8 in flags:
        problem.addConstraint(const.dataMorte_pai_filho,("pai","filho"))
        problem.addConstraint(const.dataMorte_mae_filho,("mae","filho"))
        problem.addConstraint(const.dataMorte_avo_m_filho,("avo_m","pai","mae"))
        problem.addConstraint(const.dataMorte_avo_f_filho,("avo_f","pai","mae"))

    # 4 - Avo - Neto
    if 4 in flags or 8 in flags:
        problem.addConstraint(const.avo_neto,("avo_m","avo_f","filho"))

    # 5 - Pai - Filho
    if 5 in flags or 8 in flags:
        problem.addConstraint(const.pai_filho,("pai","filho"))
        problem.addConstraint(const.avo_m_filho,("avo_m","pai","mae"))

    # 6 - Mae - Filho
    if 6 in flags or 8 in flags:
        problem.addConstraint(const.mae_filho,("mae","filho"))
        problem.addConstraint(const.avo_f_filho,("avo_f","pai","mae"))
    
    # 7 - Casados 
    if 7 in flags or 8 in flags:
        problem.addConstraint(const.casado_pai_mae,("pai","mae"))
        problem.addConstraint(const.casado_avo_m_avo_f,("avo_m","avo_f"))
    
    results = problem.getSolutions()
    if results == []:
        return 'Não foram obtidos resultados com estas restrições'
    else: 
        return results

def get_min_conflit_solver(flags):
    problem = Problem(MinConflictsSolver())

    carregarVariaveis(problem)

     # 1 - Restrição entre diferença de Datas de Nascimento entre Pai e Filho
    if 1 in flags or 8 in flags:
        problem.addConstraint(const.dataNascimento_pai_filho,("pai","filho"))
        problem.addConstraint(const.dataNascimento_avo_m_filho,("avo_m", "pai","mae"))

    # 2 - Intervalo de Nascimento entre Mae e Filho
    if 2 in flags or 8 in flags:
        problem.addConstraint(const.dataNascimento_mae_filho,("mae", "filho"))
        problem.addConstraint(const.dataNascimento_avo_f_filho,("avo_f", "pai","mae"))
    
    # 3 - Filho nasce antes da Data de Morte
    if 3 in flags or 8 in flags:
        problem.addConstraint(const.dataMorte_pai_filho,("pai","filho"))
        problem.addConstraint(const.dataMorte_mae_filho,("mae","filho"))
        problem.addConstraint(const.dataMorte_avo_m_filho,("avo_m","pai","mae"))
        problem.addConstraint(const.dataMorte_avo_f_filho,("avo_f","pai","mae"))

    # 4 - Avo - Neto
    if 4 in flags or 8 in flags:
        problem.addConstraint(const.avo_neto,("avo_m","avo_f","filho"))

    # 5 - Pai - Filho
    if 5 in flags or 8 in flags:
        problem.addConstraint(const.pai_filho,("pai","filho"))
        problem.addConstraint(const.avo_m_filho,("avo_m","pai","mae"))

    # 6 - Mae - Filho
    if 6 in flags or 8 in flags:
        problem.addConstraint(const.mae_filho,("mae","filho"))
        problem.addConstraint(const.avo_f_filho,("avo_f","pai","mae"))
    
    # 7 - Casados 
    if 7 in flags or 8 in flags:
        problem.addConstraint(const.casado_pai_mae,("pai","mae"))
        problem.addConstraint(const.casado_avo_m_avo_f,("avo_m","avo_f"))

    results = problem.getSolution()
    if results == None:
        return 'Não foram obtidos resultados com estas restrições'
    else: 
        return results

def get_recursive_backtraking_solver(flags):
    problem = Problem(RecursiveBacktrackingSolver())

    carregarVariaveis(problem)

    # 1 - Restrição entre diferença de Datas de Nascimento entre Pai e Filho
    if 1 in flags or 8 in flags:
        problem.addConstraint(const.dataNascimento_pai_filho,("pai","filho"))
        problem.addConstraint(const.dataNascimento_avo_m_filho,("avo_m", "pai","mae"))

    # 2 - Intervalo de Nascimento entre Mae e Filho
    if 2 in flags or 8 in flags:
        problem.addConstraint(const.dataNascimento_mae_filho,("mae", "filho"))
        problem.addConstraint(const.dataNascimento_avo_f_filho,("avo_f", "pai","mae"))
    
    # 3 - Filho nasce antes da Data de Morte
    if 3 in flags or 8 in flags:
        problem.addConstraint(const.dataMorte_pai_filho,("pai","filho"))
        problem.addConstraint(const.dataMorte_mae_filho,("mae","filho"))
        problem.addConstraint(const.dataMorte_avo_m_filho,("avo_m","pai","mae"))
        problem.addConstraint(const.dataMorte_avo_f_filho,("avo_f","pai","mae"))

    # 4 - Avo - Neto
    if 4 in flags or 8 in flags:
        problem.addConstraint(const.avo_neto,("avo_m","avo_f","filho"))

    # 5 - Pai - Filho
    if 5 in flags or 8 in flags:
        problem.addConstraint(const.pai_filho,("pai","filho"))
        problem.addConstraint(const.avo_m_filho,("avo_m","pai","mae"))

    # 6 - Mae - Filho
    if 6 in flags or 8 in flags:
        problem.addConstraint(const.mae_filho,("mae","filho"))
        problem.addConstraint(const.avo_f_filho,("avo_f","pai","mae"))
    
    # 7 - Casados 
    if 7 in flags or 8 in flags:
        problem.addConstraint(const.casado_pai_mae,("pai","mae"))
        problem.addConstraint(const.casado_avo_m_avo_f,("avo_m","avo_f"))

    results = problem.getSolutions()
    if results == []:
        return 'Não foram obtidos resultados com estas restrições'
    else: 
        return results