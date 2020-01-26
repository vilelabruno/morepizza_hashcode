from random import seed
from random import randint

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
    solutions = genRandomSol(slycesArr, slMax, 30)
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

def geneticAlgorithm(slycesArr, solArr, generations):
    points = getPoints(slycesArr, solArr)
    print (points)
    print (slycesArr)
    points_ = points.copy()
    points.sort()
    for _ in range(0, generations):
        print("oi")
    return solArr[points_.index(max(points_))], max(points_) 

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
    print(geneticAlgorithm(slycesArr, initSolutions, 2))
    

if __name__ == "__main__":
    main()