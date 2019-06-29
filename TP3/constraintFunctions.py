

# 1 - Restrição entre diferença de Datas de Nascimento entre Pai e Filho

def dataNascimento_pai_filho(pai,filho):
    if filho["nome"] in pai["ePai"]:
        return int(filho["dataNasc"].split('-')[2]) > int(pai["dataNasc"].split('-')[2]) + 13
    else:
        return False 

def dataNascimento_avo_m_filho(avo,pai,mae):
    if pai["nome"] in avo["ePai"]:
        return int(pai["dataNasc"].split('-')[2]) > int(avo["dataNasc"].split('-')[2]) + 13
    else:
        if mae["nome"] in avo["ePai"]:
            return int(mae["dataNasc"].split('-')[2]) > int(avo["dataNasc"].split('-')[2]) + 13
        else:
            return False 

# 2 - Restrição entre diferença de Datas de Nascimento entre Mae e Filho
def dataNascimento_mae_filho(mae,filho):
    if filho["nome"] in mae["eMae"]:
         return int(mae["dataNasc"].split('-')[2])+12 <= int(filho["dataNasc"].split('-')[2]) and int(filho["dataNasc"].split('-')[2]) <= int(mae["dataNasc"].split('-')[2])+50
    else:
        return False 

def dataNascimento_avo_f_filho(avo,pai,mae):
    if pai["nome"] in avo["eMae"]:
        return int(avo["dataNasc"].split('-')[2])+12 <= int(pai["dataNasc"].split('-')[2]) and int(pai["dataNasc"].split('-')[2]) <= int(avo["dataNasc"].split('-')[2])+50
    else:
        if mae["nome"] in avo["eMae"]:
            return int(avo["dataNasc"].split('-')[2])+12 <= int(mae["dataNasc"].split('-')[2]) and int(mae["dataNasc"].split('-')[2]) <= int(avo["dataNasc"].split('-')[2])+50
        else:
            return False 

# 3 - Não pode estar morto quando o filho nasce 

def dataMorte_pai_filho(pai,filho):
    if filho["nome"] in pai["ePai"]:
        return int(pai["dataMorte"].split('-')[2]) > int(filho["dataNasc"].split('-')[2])
    else:
        return False

def dataMorte_mae_filho(mae,filho):
    if filho["nome"] in mae["eMae"]:
        return int(mae["dataMorte"].split('-')[2]) > int(filho["dataNasc"].split('-')[2])
    else:
        return False

def dataMorte_avo_m_filho(avo,pai,mae):
    if pai["nome"] in avo["ePai"]:
        return int(avo["dataMorte"].split('-')[2]) > int(pai["dataNasc"].split('-')[2])
    else:
        if mae["nome"] in avo["ePai"]:
            return int(avo["dataMorte"].split('-')[2]) > int(mae["dataNasc"].split('-')[2])
        else:
            return False

def dataMorte_avo_f_filho(avo,pai,mae): 
    if pai["nome"] in avo["eMae"]:
        return int(avo["dataMorte"].split('-')[2]) > int(pai["dataNasc"].split('-')[2])
    else:
        if mae["nome"] in avo["eMae"]:
            return int(avo["dataMorte"].split('-')[2]) > int(mae["dataNasc"].split('-')[2])
        else:
            return False


# 5 - Avo-Neto

def avo_neto(avo_m,avo_f,filho):
    if filho["nome"] in avo_m["eAvo"]:
        if filho["nome"] in avo_f["eAvo"]:
            return True
        else:
            return False
    else:
        return False

# 6 - Pai - Filho 

def pai_filho(pai,filho):
    if filho["nome"] in pai["ePai"]:
        return True
    else:
        return False

def avo_m_filho(avo,pai,mae):
    if pai["nome"] in avo["ePai"]:
        return True
    else:
        if mae["nome"] in avo["ePai"]:
            return True
        else:
            return False

# 7 - Mae - Filho 

def mae_filho(mae,filho):
    if filho["nome"] in mae["eMae"]:
        return True
    else:
        return False

def avo_f_filho(avo,pai,mae):
    if pai["nome"] in avo["eMae"]:
        return True
    else:
        if mae["nome"] in avo["eMae"]:
            return True
        else:
            return False

# 8 - Casado Pai - Mae 

def casado_pai_mae(pai,mae):
    if pai["ePai"] == mae["eMae"]:
        return True
    else:
        return False 

def casado_avo_m_avo_f(avo_m,avo_f):
    if avo_m["ePai"] == avo_f["eMae"]:
        return True
    else:
        return False