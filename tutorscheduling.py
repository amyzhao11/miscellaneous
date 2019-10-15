from gurobipy import *

#sets
Tutes = range(13)
name=['01','02','03','04','05','06','07','09','10','11','13','14','16']
#names have be deanonymised
Lname=['LeadTutor1','LeadTutor2','LeadTutor3','LeadTutor4', 'LeadTutor5']
Tname=['Tutor1','Tutor2','Tutor3','Tutor4','Tutor5','Tutor6','Tutor7','Tutor8','Tutor9','Tutor10','Tutor11','Tutor12','Tutor13','Tutor14']
L = range(5)
T = range(14)
#data
#exact number of sessions per tutor
Lnum = [4,3,3,2,3] #lead tutor
Tnum = [1,1,4,2,1,2,2,1,2,1,1,1,1,1]

#minimum number of lead tutors
minL=[0,1,1,1,1,1,1,1,1,1,1,1,1]
#sessions allocated per tutor
exactTot = [1,3,3,3,2,3,3,3,3,3,3,3,3]

LAvail = [[0,1,1,0,0,0,1,1,1,1,1,1,0], #
          [0,0,1,0,1,1,1,0,1,0,0,0,1], #
          [0,0,0,0,1,1,1,0,0,0,0,0,0], #
          [1,0,0,1,1,0,0,0,0,0,0,0,1],
          [0,0,1,1,0,0,1,0,0,1,0,1,0]]
          
TAvail = [[1,1,1,1,0,0,1,1,0,0,1,1,0],
          [0,0,0,0,0,0,0,1,0,0,0,0,1],
          [0,1,0,1,0,0,0,1,0,1,0,1,0],
          [1,1,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,1,0,1,1],
          [0,0,0,0,0,0,0,0,1,1,1,1,0],
          [1,1,0,0,0,0,0,0,0,0,0,1,0],
          [1,1,1,1,0,0,0,0,0,0,0,0,1],
          [0,1,0,0,0,1,1,0,0,0,0,0,0],
          [0,1,0,0,0,0,0,0,0,0,0,1,1],
          [0,0,1,0,0,0,0,0,1,0,1,0,1],
          [1,1,0,0,1,0,0,1,1,0,0,0,0],
          [0,0,0,0,0,1,0,0,0,0,0,0,1],
          [0,0,0,0,1,1,0,0,0,0,0,0,0]]
     

           
m=Model()

#variables
#X={(i,j): m.addVar(vtype=GRB.BINARY) for i in T for j in P}
LVar = {(tut,l) : m.addVar(vtype=GRB.BINARY) for tut in Tutes for l in L}
TVar = {(tut,t) : m.addVar(vtype=GRB.BINARY) for tut in Tutes for t in T}
        
#constraints
#Make sure we have enough leaders (min)
for tut in Tutes:
    m.addConstr(quicksum(LVar[tut,l] for l in L) >= minL[tut])
#Each tute has exactly number of total tutors
for tut in Tutes:
    m.addConstr(quicksum(LVar[tut,l] for l in L) + quicksum(TVar[tut, t] for t in T) == exactTot[tut])
#Each tutor/Leader has exactly assigned number of sessions
for t in T:
    m.addConstr(quicksum(TVar[tut, t] for tut in Tutes) == Tnum[t])

for l in L:
    m.addConstr(quicksum(LVar[tut, l] for tut in Tutes) == Lnum[l])
    
#Leaders are available
for tut in Tutes:
    for t in T:
        m.addConstr(TVar[tut, t] <= TAvail[t][tut])
    for l in L:
        m.addConstr(LVar[tut, l] <= LAvail[l][tut])

m.optimize()

for tut in Tutes:
    s = 'Tute:' + str(name[tut]) + ',' + 'Leaders:'
    for l in L:
        if LVar[tut,l].X == 1:
            s += str(Lname[l]) + ','
    s += 'Tutors:'
    for t in T:
        if TVar[tut,t].X == 1:
            s += str(Tname[t]) + ','
    print(s)
