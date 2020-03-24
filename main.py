from GA import GA

def readData(filename):
    with open(filename, 'r') as f:
        n=int(f.readline().rstrip())
        matrice = [[int(num) for num in line.split(',')] for line in f]

    net = {}
    net['noNodes'] = n
    net['mat'] = matrice
    return net

def drumMin(drum, param):
    noNodes = param['noNodes']
    mat = param['mat']
    L=0
    for i in range(0, noNodes-1):
        L+=mat[drum[i]][drum[i+1]]
    L+=mat[drum[noNodes-1]][drum[0]]
    return L

net = readData('hard_01_tsp.txt')
gaParam = {"popSize": 1000, "noGen": 100, "pc": 0.8, "pm": 0.1, "network": net}
problParam = {'function': drumMin, 'noNodes': net['noNodes']}

def afisare(x):
    comunities=[]
    for i in range(0,problParam['noNodes']):
        comunities.append(x[i]+1)
    return comunities

def main():
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    ga.oneGeneration()
    bestChromo=ga.bestChromosome()
    print('Solutia cea mai buna este: ' + str(afisare(bestChromo.repres)) + ' cost = ' + str(bestChromo.fitness))

main()

