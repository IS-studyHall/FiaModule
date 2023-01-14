import csv
import copy
from initialization import generatePopulation
from fitnessFunction import fitnessQuantita, fitnessFasceOrarie
from crossoverAlgorithm import singlePoint
from selection import rouletteWheelSelection
timeSlot = 20
sizePopulation = 4
numberStudyroom = 3
fileName = 'dataset.csv'
def readFileAndFormatInput(filename):
    students = []
    quantity = []
    timeSlots = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0
        for row in spamreader:
            if i > 0:
                stringa = []
                students.append(row[0])
                for r in range(1, len(row) - 1):
                    for c in row[r]:
                        stringa.append(int(c))
                quantity.append(row[len(row) - 1])
                timeSlots.append(copy.deepcopy(stringa))
            i+=1
    return students, quantity, timeSlots

def main():
    students, quantity, timeSlots = readFileAndFormatInput(fileName)
    population = generatePopulation(students, sizePopulation, timeSlot, numberStudyroom)
    resultsFitnessQuantita = []
    resultsFitnessFasceOrarie = []
    for i in range(len(population)):
        resultsFitnessQuantita.append(fitnessQuantita(population[i], quantity, students))
        resultsFitnessFasceOrarie.append(fitnessFasceOrarie(population[i], timeSlots, students, numberStudyroom))
    newPopulation = rouletteWheelSelection(resultsFitnessFasceOrarie, resultsFitnessQuantita, population)
    print(newPopulation)
if __name__ == '__main__':
    main()

    

