import csv
import copy
from initialization import generatePopulation
from fitnessFunction import fitnessQuantita, fitnessFasceOrarie
from crossoverAlgorithm import singlePoint

timeSlot = 20
sizePopulation = 4
numberStudyroom = 3

def readFileAndFormatInput():
    students = []
    quantity = []
    timeSlots = []
    with open('dataset.csv', newline='') as csvfile:
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
    students, quantity, timeSlots = readFileAndFormatInput()
    population = generatePopulation(students, sizePopulation, timeSlot, numberStudyroom)
    quantita = fitnessQuantita(population[0], quantity[0], students[0])
    result = fitnessFasceOrarie(population[0], timeSlots[0], students[0], numberStudyroom)

if __name__ == '__main__':
    main()

    

