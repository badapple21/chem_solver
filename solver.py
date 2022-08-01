from math import fabs, prod


def solve(q, w, e, r, t, y):
    reactant1 = q
    charge1 = fabs(int(w))
    reactant2 = e
    charge2 = fabs(int(r))

    amount1 = int(t)
    amount2 = int(y)

    value1 = charge2
    value2 = charge1

    for k in range(2, 10):
        if(value1 % k == 0) and (value2 % k == 0):
            amount1 =  value1  = int(value1/k)
            amount2 = value2 = int(value2/k)
            break

    
    
    max = 10
    for i in range(1, max+1):
        for j in range(1, max+1):
            test1 = i*amount1
            test2 = j*amount2
            for l in range(2, max+1):
                print(f"{test1} % {l} == {test1 % l} and {test2} % {l} == {test2 % l}")
                if(test1 % l == 0) and (test2 % l == 0):
                    if(test1 == l*value1) and (test2 == l*value2):


                        for r in range(2, 10):
                            if(i % r == 0) and (j % r == 0) and (l % r == 0):
                                i  = int(i/r)
                                j = int(j/r)
                                l = int(l/r)
                                break

                        return "Solved", i, j, value1, value2, reactant1, reactant2, amount1, amount2, l
    
    else:
        return "Error", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"



def format(coefficient1, coefficient2, charge1, charge2, reactant1, reactant2, amount1, amount2, product_coefficient):

    if(coefficient1 == 1):
        coefficient1 = ""
    if(coefficient2 == 1):
        coefficient2 = ""
    if(int(amount1) == 1):
        amount1 = ""
    if(int(amount2) == 1):
        amount2 = ""
    if(int(charge1) == 1):
        charge1 = ""
    if(int(charge2) == 1):
        charge2 = ""
    if(product_coefficient == 1):
        product_coefficient = ""
    

    HTML = f"{coefficient1}{reactant1}<sub>{amount1}</sub> + {coefficient2}{reactant2}<sub>{amount2}</sub> -> {product_coefficient}{reactant1}<sub>{charge1}</sub>{reactant2}<sub>{charge2}</sub>"
    return HTML
