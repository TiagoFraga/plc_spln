from pyswip import Prolog

def exec_query(query):
    p = Prolog()
    p.consult('genealogia.pl')
    return list(p.query(query))
    