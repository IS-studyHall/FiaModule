from random import randint

def inversion(population: list):
    newPopulation = []
    for i in range(len(population)):
        newGene = population[i].split(',')
        while True:
            firstValue = randint(0, len(newGene))
            secondValue = randint(0, len(newGene))
            if firstValue < secondValue:
                break
        part = newGene[firstValue: secondValue]
        part.reverse()
        newPopulation.append(','.join(newGene[0:firstValue] + part + newGene[secondValue:]))
    return newPopulation