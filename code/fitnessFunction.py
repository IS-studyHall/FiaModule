def fitnessQuantita(gene: str, quantita: list, studenti: list): #range [0, 1]
    output = 0
    for j in range(len(studenti)):
        i = 0
        for c in gene:
            if c == studenti[i]:
                i+=1
        output += i-int(quantita[j]) if int(quantita[j]) > i else int(quantita[j]) - i
    if output < 0:
        output = 1 / (-1 * output)
    if output == 0:
        output = 1
    return output

def fitnessFasceOrarie(gene: str, fasceStudenti: list, studenti: list, studyroom: int):
    output = 0
    separateGene = gene.split(',')
    studyroomList = []
    n = int(len(separateGene) / studyroom)
    for i in range(studyroom):
        studyroomList.append(separateGene[i*n: (i+1)*n + 1])
    for k in range(len(studenti)):
        for i in range(len(studyroomList[0])):
            count = 0
            for j in range(len(studyroomList)):
                if studenti[k] in studyroomList[j][i]:
                    count += 1
            if count == 1 and fasceStudenti[k][i] == 1:
                output += 1
            elif output - count > 0:
                output -= count
    return output

