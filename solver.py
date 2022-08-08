from math import fabs, prod


def solve(reactant1, w, reactant2, r, t, y):
    charge1 = fabs(int(w))
    charge2 = fabs(int(r))

    amount1 = int(t)
    amount2 = int(y)

    value1 = charge2
    value2 = charge1


    # reduces the amounts to the least common factors helps simplify later
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

def check_1(num):
    if(num == 1):
        return ""
    else:
        return num

def format(coefficient1, coefficient2, charge1, charge2, reactant1, reactant2, amount1, amount2, product_coefficient):

    coefficient1 = check_1(coefficient1)
    coefficient2 = check_1(coefficient2)
    amount1 = check_1(amount1)
    amount2 = check_1(amount2)
    charge1 = check_1(charge1)
    charge2 = check_1(charge2)
    product_coefficient = check_1(product_coefficient)
    

    HTML = f"{coefficient1}{reactant1}<sub>{amount1}</sub> + {coefficient2}{reactant2}<sub>{amount2}</sub> -> {product_coefficient}{reactant1}<sub>{charge1}</sub>{reactant2}<sub>{charge2}</sub>"
    return HTML
