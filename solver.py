from math import fabs

def solve(q, w, e, r):
    reactant1 = q
    charge1 = fabs(int(w))

    reactant2 = e
    charge2 = fabs(int(r))

    value1 = charge2
    value2 = charge1

    ratio = value1 / value2
    solved = False
    while solved==False:
        max = 3
        for i in range(1, max+1):
            for j in range(1, max+1):
                print(i)
                print(j)
                if((i*value1)/(j*value2)==ratio):
                    return "Solved", i, j, value1, value2, reactant1, reactant2
        if(max<100):
            max+=1
        else:
            return "Error", "-1", "-1" ,"-1", "-1", "-1", "-1"

def format(coefficient1, coefficient2, charge1, charge2, reactant1, reactant2):
    if(coefficient1==1):
        coefficient1 = ""
    if(coefficient2==1):
        coefficient2=""
    HTML = f"{coefficient1}{reactant1}<sub>{int(charge1)}</sub>{coefficient2}{reactant2}<sub>{int(charge2)}</sub>"
    return HTML




