import csv
from initialization import generatePopulation

studenti = []
with open('dataset.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    i = 0
    for row in spamreader:
        if i > 0:
            print(', '.join(row))
            studenti.append(row[0])
        i+=1
    print(row)
    print(studenti)
    print(generatePopulation(studenti))
    

