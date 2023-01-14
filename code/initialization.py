import random

def generateOutputTime(studenti: list):
    time = ""
    for i in studenti:
        value = random.uniform(0, 1)
        value = i if value > 0.5 else ''
        time += value
    return time

def generateOutputStudyroom(studenti: list, timeSlot):
    output = ""
    for i in range(timeSlot):
        output+=generateOutputTime(studenti)+","
    return output[0:len(output)-1]

def generateGene(studenti: list, numberStudyroom, timeSlot):
    output = ""
    for i in range(numberStudyroom):
        output+=generateOutputStudyroom(studenti, timeSlot)
    return output

def generatePopulation(studenti: list, sizePopulation: int, timeSlot: int, numberStudyroom: int):
    output = []
    for i in range(sizePopulation):
        output.append(generateGene(studenti, numberStudyroom, timeSlot))
    return output