def singlePoint(population: list):
    part = (len(population[0].split(',')) - 1)/2
    firstCut = int(part)
    newPopulation = []
    for i in range(0, len(population), 2):
        firstGene = population[i].split(',')
        secondGene = population[i + 1].split(',')
        newFirstGene = firstGene[0:firstCut] + firstGene[firstCut:]
        newSecondGene = secondGene[0: firstCut] + secondGene[firstCut:]
        newPopulation.append(','.join(newFirstGene))
        newPopulation.append(','.join(newSecondGene))
    return newPopulation

def twoPoint(population: list):
    part = (len(population[0].split(',')) - 1)/3
    firstCut = int(part)
    secondCut = int(2 * part)
    newPopulation = []
    for i in range(0, len(population), 2):
        firstGene = population[i].split(',')
        secondGene = population[i + 1].split(',')
        newFirstGene = firstGene[0:firstCut] + secondGene[firstCut: secondCut] + firstGene[secondCut:]
        newSecondGene = secondGene[0: firstCut] + firstGene[firstCut: secondCut] + secondGene[secondCut:]
        newPopulation.append(','.join(newFirstGene))
        newPopulation.append(','.join(newSecondGene))
    return newPopulation