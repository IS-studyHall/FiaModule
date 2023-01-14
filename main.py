import csv
from initialization import generatePopulation
from fitnessFunction import funzioneQuantita

studenti = []
quantita = []
with open('dataset.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    for row in spamreader:
        if i > 0:
            studenti.append(row[0])
            quantita.append(row[len(row) - 1])
        i+=1
    print(quantita)
    population = generatePopulation(studenti)
    print(funzioneQuantita(population[0], quantita[0], studenti[0]))

    

