import numpy as np
def rouletteWheelSelection(resultsFitnessFasceOrarie, resultsFitnessQuantita, population):
    newPopulation = []
    totallyFasceOrarieValue = sum(resultsFitnessFasceOrarie)
    #if totallyFasceOrarieValue > 0:
    probabilitiesFasceOrarie = [value/totallyFasceOrarieValue for value in resultsFitnessFasceOrarie]
    for i in range(len(population)):
        newPopulation.append(np.random.choice(population, p=probabilitiesFasceOrarie))
    #else:
    #    totallyQuantitaValue = sum(resultsFitnessQuantita)
    #    probabilitiesQuantita = [value/totallyQuantitaValue for value in resultsFitnessQuantita]
    #    for i in range(len(population)):
    #        newPopulation.append(np.random.choice(population, p=probabilitiesQuantita))
    return newPopulation

