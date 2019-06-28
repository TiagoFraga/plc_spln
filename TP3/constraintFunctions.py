
# avo - neto

def avo_m_neto(avo_m,mae,pai,filho):
    if avo_m["ePai"] == mae["nome"]:
        if mae["eMae"] == filho["nome"]:
            return True
        else:
            return False
    else:
        if avo_m["ePai"] == pai["nome"]:
            if pai["ePai"] == filho["nome"]:
                return True
            else:
                return False
        else:
            return False

def avo_f_neto(avo_f,mae,pai,filho):
    if avo_f["eMae"] == mae["nome"]:
        if mae["eMae"] == filho["nome"]:
            return True
        else:
            return False
    else:
        if avo_f["eMae"] == pai["nome"]:
            if pai["ePai"] == filho["nome"]:
                return True
            else:
                return False
        else:
            return False

# data Nascimento

def dataNasc_avo_m_filho(avo, mae, pai):
    if avo["ePai"] == mae["nome"]:
        return int(mae["dataNasc"].split('-')[2]) > int(avo["dataNasc"].split('-')[2]) + 10
    else:
        if avo["ePai"] == pai["nome"]:
            return int(pai["dataNasc"].split('-')[2]) > int(avo["dataNasc"].split('-')[2]) + 10
        else:
            return False


def dataNasc_avo_f_filho(avo, mae, pai):
    if avo["eMae"] == mae["nome"]:
        return int(mae["dataNasc"].split('-')[2]) > int(avo["dataNasc"].split('-')[2]) + 10
    else:
        if avo["eMae"] == pai["nome"]:
            return int(pai["dataNasc"].split('-')[2]) > int(avo["dataNasc"].split('-')[2]) + 10
        else:
            return False



# Intervalo de Nascimento
def intervalo_mae_filho(mae,filho):
    if mae["eMae"] == filho["nome"]:
        return int(mae["dataNasc"].split('-')[2])+12 <= int(filho["dataNasc"].split('-')[2]) and int(filho["dataNasc"].split('-')[2]) <= int(mae["dataNasc"].split('-')[2])+50
    else:
        return False

def intervalo_avo_f_tio(avo,pai,mae,tio):
    if tio["eIrmao"] == pai["nome"]:
        if avo["eMae"] == pai["nome"]:
            return int(avo["dataNasc"].split('-')[2])+12 <= int(tio["dataNasc"].split('-')[2]) and int(tio["dataNasc"].split('-')[2]) <= int(avo["dataNasc"].split('-')[2])+50
        else:
            return False
    else:
        if tio["eIrmao"] == mae["nome"]:
            if avo["eMae"] == mae["nome"]:
                return int(avo["dataNasc"].split('-')[2])+12 <= int(tio["dataNasc"].split('-')[2]) and int(tio["dataNasc"].split('-')[2]) <= int(avo["dataNasc"].split('-')[2])+50
            else:
                return False
        else:
            return False

def intervalo_avo_m_tio(avo,pai,mae,tio):
    if tio["eIrmao"] == pai["nome"]:
        if avo["ePai"] == pai["nome"]:
            return int(tio["dataNasc"].split('-')[2]) > int(avo["dataNasc"].split('-')[2]) + 10
        else:
            return False
    else:
        if tio["eIrmao"] == mae["nome"]:
            if avo["ePai"] == mae["nome"]:
                return int(tio["dataNasc"].split('-')[2]) > int(avo["dataNasc"].split('-')[2]) + 10
            else:
                return False
        else:
            return False

def intervalo_avo_f_pai_mae(avo,pai,mae):
    if avo["eMae"] == pai["nome"]:
        return int(avo["dataNasc"].split('-')[2])+12 <= int(pai["dataNasc"].split('-')[2]) and int(pai["dataNasc"].split('-')[2]) <= int(avo["dataNasc"].split('-')[2])+50
    else:
        if avo["eMae"] == mae["nome"]:
            return int(avo["dataNasc"].split('-')[2])+12 <= int(mae["dataNasc"].split('-')[2]) and int(mae["dataNasc"].split('-')[2]) <= int(avo["dataNasc"].split('-')[2])+50
        else:
            return False

def intervalo_avo_f_mae(avo,mae):
    if avo["eMae"] == mae["nome"]:
        return int(avo["dataNasc"].split('-')[2])+12 <= int(mae["dataNasc"].split('-')[2]) and int(mae["dataNasc"].split('-')[2]) <= int(avo["dataNasc"].split('-')[2])+50
    else:
        return False

# data Morte
def dataMorte_filho_pais(filho, mae, pai):
    if pai["ePai"] == filho["nome"]:
        if mae["eMae"] == filho["nome"]:
            return (int(mae["dataMorte"].split('-')[2]) > int(filho["dataNasc"].split('-')[2]) and int(pai["dataMorte"].split('-')[2]) > int(filho["dataNasc"].split('-')[2]))
        else:
            return False
    else:
        return False

def dataMorte_avo_mae(avo_m,avo_f, mae):
    if avo_m["ePai"] == mae["nome"]:
        if avo_f["eMae"] == mae["nome"]:
            return (int(avo_f["dataMorte"].split('-')[2]) > int(mae["dataNasc"].split('-')[2]) and int(avo_m["dataMorte"].split('-')[2]) > int(mae["dataNasc"].split('-')[2]))
        else:
            return False
    else:
        return False

def dataMorte_avo_pai(avo_m,avo_f, pai):
    if avo_m["ePai"] == pai["nome"]:
        if avo_f["eMae"] == pai["nome"]:
            return (int(avo_f["dataMorte"].split('-')[2]) > int(pai["dataNasc"].split('-')[2]) and int(avo_m["dataMorte"].split('-')[2]) > int(pai["dataNasc"].split('-')[2]))
        else:
            return False
    else:
        return False

