from constraint import *


def init():
    problem = Problem()
    return problem

def carregamento_por_ficheiro(file,p):
    p.consult(file)

def getResults(problem):
    return problem.getSolutions()

def addVariavel(nome,variavel,problem):
    problem.addVariable(nome, [variavel])

def addConstraint(intervenientes,constraint,problem):
    problem.addConstraint(constraint)