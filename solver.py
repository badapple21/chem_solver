from math import fabs


def solve(q, w, e, r, t, y):
    reactant1 = q
    charge1 = fabs(int(w))
    print(charge1)

    reactant2 = e
    charge2 = fabs(int(r))
    print(charge2)

    amount1 = int(t)
    amount2 = int(y)

    value1 = charge2
    value2 = charge1

    ratio = value1 / value2
    solved = False
    while solved == False:
        max = 300
        for i in range(0, max+1):
            for j in range(0, max+1):
                print(f"")
                if (i*amount1 == charge1) and (j*amount2 == charge2):
                    return "Solved", i, j, value1, value2, reactant1, reactant2
        if(max < 100):
            max += 1
        else:
            return "Error", "-1", "-1", "-1", "-1", "-1", "-1"


def format(coefficient1, coefficient2, charge1, charge2, reactant1, reactant2, amount1, amount2):

    if(coefficient1 == 1):
        coefficient1 = ""
    if(coefficient2 == 1):
        coefficient2 = ""
    if(amount1 == 1):
        amount1 = ""
    if(amount2 == 1):
        amount2 = ""

    HTML = f"{coefficient1}{reactant1}<sub>{int(amount1)}</sub> + {coefficient2}{reactant2}<sub>{int(amount2)}</sub> -> {reactant1}<sub>{int(charge1)}</sub>{reactant2}<sub>{int(charge2)}</sub>"
    return HTML
