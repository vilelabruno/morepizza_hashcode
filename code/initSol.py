from random import seed
from random import randint
from random import choice

populacao = 30

def loadFile(inpFilePath):
    with open(inpFilePath) as inpFile:
        inpFile = inpFile.readlines()
        return int(inpFile[0].split(" ")[0].strip()), int(inpFile[0].split(" ")[1].strip()), inpFile[1].split(" ")
            #print(line) 

def orderedSol(slycesArr, slycesArr_, slMax):
    summ = 0
    solution = []
    for pizza in slycesArr:
        summ += pizza
        if summ > slMax:
            break
        solution.append(slycesArr_.index(pizza))
    return solution

def randomSol(slycesArr, slMax):
    summ = 0
    sol = []
    while True:
        pizza = randint(0, len(slycesArr)-1)
        while pizza in sol:
            pizza = randint(0, len(slycesArr)-1)
        summ += slycesArr[pizza]
        if summ > slMax:
            break
        sol.append(pizza)
    return sol

def genRandomSol(slycesArr, slMax, qtd):
    solArr = []
    for _ in range(0, qtd):
        solArr.append(randomSol(slycesArr, slMax))
    return solArr

def initSol(slMax, typesPizza, slycesArr):
    solutions = genRandomSol(slycesArr, slMax, populacao)
    slycesArr_ = slycesArr.copy()
    slycesArr_.sort()
    solutions.append(orderedSol(slycesArr_, slycesArr, slMax))
    slycesArr_.sort(reverse=True)
    solutions.append(orderedSol(slycesArr_, slycesArr, slMax))
    return solutions

def getPoints(slycesArr, solArr):
    points = []
    for sol in solArr:
        summ = 0
        for pt in sol:
            summ += slycesArr[pt]
        points.append(summ)
    return points

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

def join(solA, solB):
    return unique(solA+solB)

def isSolValid(sol, slycesArr, slMax):
    if len(sol) == 0:
        return False
    summ = 0
    for pizza in sol:
        summ += slycesArr[pizza]
        if summ > slMax:
            #print(summ)
            #print(sol)
            return False
    return True

def randomWeighted():
    lst = (list(range(0,int(populacao/3))) * 60) +(list(range(int(populacao/3),int((populacao/3))*2)) * 30) +(list(range((int(populacao/3))*2,int(populacao))) * 10)
    return choice(lst)

def transformToValid(sol, slycesArr, slMax):
    #summ = 0
    while not(isSolValid(sol, slycesArr, slMax)):
        sol_ = sol.copy()
        sol_.sort()
        #print(sol.index(sol_[0]))
        #print(sol)
        del sol[sol.index(sol_[0])]
    return sol

def geneticAlgorithm(slycesArr, solArr, generations, slMax):
    allGen = []
    solNewGen = solArr
    for _ in range(0, generations):
        solArr = solNewGen
        allGen.append(solNewGen)
        solNewGen = []
        points = getPoints(slycesArr, solArr)
        #print (points)
        #print (slycesArr)
        points_ = points.copy()
        points.sort(reverse=True)
        #print(points)
        for piNumber in range(0, populacao):
            sol = []
            print(str(piNumber)+" generating...")
            while not(isSolValid(sol, slycesArr, slMax)):
                sol = join(solArr[points_.index(points[randomWeighted()])], solArr[points_.index(points[randomWeighted()])])
            #sol = transformToValid(sol, slycesArr, slMax)
            #print(sol)
            solNewGen.append(sol)
        #print("oi")
    output = []
    for sArr in allGen:
        pointsFinal = getPoints(slycesArr, sArr)
        output.append((sArr[pointsFinal.index(max(pointsFinal))], max(pointsFinal) ))
    return output

def getBest(slycesArr, solArr, generations, slMax):
    points = getPoints(slycesArr, solArr)
    #print (points)
    #print (slycesArr)
    return solArr[points.index(max(points))], max(points)

fExample = "../input/a_example.in"
fSmall = "../input/b_small.in"
fMedium = "../input/c_medium.in"
fQuiteBig = "../input/d_quite_big.in"
fAlsoBig = "../input/e_also_big.in"

def main():
    slMax, typesPizza, slycesArr = loadFile(fAlsoBig)
    slycesArr[len(slycesArr)-1] = slycesArr[len(slycesArr)-1].strip()
    slycesArr = list(map(int, slycesArr))
    initSolutions = initSol(slMax, typesPizza, slycesArr)
    print(initSolutions)
    print(geneticAlgorithm(slycesArr, initSolutions, 2, slMax)[1])
    

if __name__ == "__main__":
    main()