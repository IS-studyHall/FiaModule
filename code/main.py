import csv
from initialization import generatePopulation
from fitnessFunction import funzioneQuantita

students = []
quantity = []
timeSlots = []
with open('code\dataset.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    stringa = ""
    for row in spamreader:
        if i > 0:
            students.append(row[0])
            stringa = row[0] + row[1] + row[2] + row[3] + row[4] + row[5]
            quantity.append(row[len(row) - 1])
        i+=1
        timeSlots.append(stringa)
    print(quantity)
    print(students)
    population = generatePopulation(students)
    print(timeSlots)
    print(funzioneQuantita(population[0], quantity[0], students[0]))
    #print(funzioneFasceOraria(population[1], timeSlots, ))

    

