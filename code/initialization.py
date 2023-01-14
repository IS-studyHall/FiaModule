def generateOutputTime(studenti: list):
    return "AB"

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