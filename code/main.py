import csv
import copy
from initialization import generatePopulation
from fitnessFunction import fitnessQuantita, fitnessFasceOrarie
from crossover import singlePoint, twoPoint
from selection import rouletteWheelSelection
from mutation import inversion
import time

timeSlot = 20
sizePopulation = 4
numberStudyroom = 3
fileName = 'dataset.csv'
giorni = ['Lunedi','Martedi','Mercoledi','Giovedi','Venerdi']
maxExecutionTime = 5 * 60 #* 48 * 60 

def formattedTime(time, students):
    diff = len(students) - len(time)
    return time + ('-' * diff)

def outputStudyroom(st, pF, students):
    first = []
    second = []
    third = []
    fourth = []
    for i in range(0, pF, 4):
        first.append(formattedTime(st[i], students))
        second.append(formattedTime(st[i+1], students))
        third.append(formattedTime(st[i+2], students))
        fourth.append(formattedTime(st[i+3], students))
    print(*first)
    print(*second)
    print(*third)
    print(*fourth)

def printTableOutput(gene, students):
    gene = gene.split(',')
    pF = int((len(gene)) / numberStudyroom)
    for i in range(numberStudyroom):
        outputStudyroom(gene[i * pF:(i+1) * pF], pF, students)
        print('\n')

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
    start_time = time.time()
    students, quantity, timeSlots = readFileAndFormatInput(fileName)
    population = []
    population = generatePopulation(students, sizePopulation, timeSlot, numberStudyroom)
    printTableOutput(population[0], students)
    print('fasce orarie:', fitnessFasceOrarie(population[0], timeSlots, students, numberStudyroom), 'quantita:', fitnessQuantita(population[0], quantity, students))
    while True:
        resultsFitnessQuantita = []
        resultsFitnessFasceOrarie = []
        for i in range(len(population)):
            resultsFitnessQuantita.append(fitnessQuantita(population[i], quantity, students))
            resultsFitnessFasceOrarie.append(fitnessFasceOrarie(population[i], timeSlots, students, numberStudyroom))
        population = rouletteWheelSelection(resultsFitnessFasceOrarie, resultsFitnessQuantita, population)
        population = singlePoint(population)
        population = inversion(population)
        end_time = time.time()
        if end_time - start_time > maxExecutionTime:
            break
    printTableOutput(population[0], students)
    print('fasce orarie:', fitnessFasceOrarie(population[i], timeSlots, students, numberStudyroom), 'quantita:', fitnessQuantita(population[i], quantity, students))
if __name__ == '__main__':
    main()

    

