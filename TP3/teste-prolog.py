# from constraint import *

# filho = {
#     "nome" : "joao",
#     "idade": 10,
# }

# filho2 = {
#     "nome": "alberto",
#     "idade": 11
# }



# pai = {
#     "nome": "jose",
#     "idade" : 50
# }

# avo = {
#     "nome" : "alberto",
#     "idade" : 70
# }

# def ePai(x,y):
#     if y == False:
#         x["ePai"] = "Desconhecido"
#     else:
#         x['ePai'] = y["nome"]


# ePai(pai,filho)
# ePai(avo,False)

# problem = Problem()
# problem.addVariable("filho", [filho,filho2])
# problem.addVariable("pai", [pai])
# problem.addVariable("avo",[avo])

# problem.addConstraint(lambda filho, pai: filho["idade"] < pai["idade"] - 10,
#                           ("filho", "pai"))

# problem.addConstraint(lambda pai, avo: pai["idade"] < avo["idade"]-10, ("pai","avo"))

# problem.addConstraint(lambda avo,filho,pai: avo["ePai"] == pai["nome"] and pai["ePai"] == filho["nome"],("avo","filho","pai"))

# print(problem.getSolutions())


import json
file_open = open('teste.json','r')
data = json.load(file_open)
print(data)




# def main():
#     p = Prolog()

#     father = Functor("father", 2)
#     mother = Functor("mother", 2)    
#     assertz = Functor("assertz", 1)

#      call(assertz(father("john", "mich")))
#      call(assertz(father("john", "gina")))
#      call(assertz(father("hank", "cloe")))
#      call(assertz(mother("jane", "mich")))
#      call(assertz(mother("jane", "gina")))

#      p.assertz("father(john,mich)")
# #     p.assertz("father(john,gina)")
# #     p.assertz("mother(jane,mich)")

# #     X = Variable(); Y = Variable(); Z = Variable()

# #     listing = Functor("listing", 1)
# #     call(listing(father))

# #     # print(list(p.query("listing(father))")))

# #     # q = Query(father("john",Y), mother(Z,Y))
# #     # while q.nextSolution():
# #     #     print(Y.value, Z.value)
# #     #     print(X.value, "is the father of", Y.value)
# #     #     print(Z.value, "is the mother of", Y.value)
# #     # q.closeQuery()    # Newer versions of SWI-Prolog do not allow nested queries

# #     print("\nQuery with strings\n")
# #     for s in p.query("father(X,Y),mother(Z,Y)"):
# #         print(s["X"], "is the father of", s["Y"])
# #         print(s["Z"], "is the mother of", s["Y"]) 
# #         print(s["Y"], s["Z"])

# #     print("running the query again")
# #     q = Query(father(X, Y))
# #     while q.nextSolution():
# #         print(X.value, "is the father of", Y.value)

    
# if __name__ == "__main__":
#      main()
