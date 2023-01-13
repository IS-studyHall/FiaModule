timeSlot = 20
sizePopulation = 4
numberStudyroom = 3

def generateOutputTime(studenti: list):
    return "AB"

def generateOutputStudyroom(studenti: list):
    output = ""
    for i in range(timeSlot):
        output+=generateOutputTime(studenti)+","
    print(len(output))
    
    return output[0:len(output)-1]

def generateGene(studenti: list):
    output = ""
    for i in range(numberStudyroom):
        output+=generateOutputStudyroom(studenti)
    return output

def generatePopulation(studenti: list):
    output = []
    for i in range(sizePopulation):
        output.append(generateGene(studenti))
    return output