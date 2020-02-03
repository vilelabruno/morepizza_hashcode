#!/usr/bin/env python3
from pulp import *

fa = "../input/a_example.in"
fb = "../input/b_small.in"
fc = "../input/c_medium.in"
fd = "../input/d_quite_big.in"
fe = "../input/e_also_big.in"

files_arr = [fa, fb, fc, fd, fe]

def loadFile(inpFilePath):
    f = open(inpFilePath).readlines()
    params = f[0].split(" ")
    arr = [int(x) for x in f[1].split(" ")]
    return int(params[0]), arr

def main(filePath):
    sl_max, slices_arr = loadFile(filePath)
    sl_arr_len = len(slices_arr)    
    problem = LpProblem("more_pizza", LpMaximize)

    # if x is Binary
    x_vars  = {(i):
    LpVariable(cat=LpBinary, name="x_{0}".format(i)) 
    for i in range(sl_arr_len)}

    # Less than equal constraints
    c1 = sum([x_vars[i] * slices_arr[i] for i in range(sl_arr_len)]) <= sl_max
    problem += c1

    # objective function
    objective = lpSum(x_vars[i] * slices_arr[i] for i in range(sl_arr_len))

    # for maximization
    problem.sense = LpMaximize
    problem.setObjective(objective)

    problem.solve()

    result = []
    for v in problem.variables():
      if str(v).startswith("x_") and v.varValue:
        result.append(int(str(v).replace("x_", "")))

    print("Solution for " + filePath)
    print(value(problem.objective))

    resultF = open(filePath + ".result", "w+")
    resultF.write(str(len(result)) + "\n")
    for r in result:
        resultF.write(str(r) + " ")

if __name__ == '__main__':
    for f in files_arr:
        main(f)