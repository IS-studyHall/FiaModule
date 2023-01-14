def fitnessQuantita(gene: str, quantita: str, studente: str):
    i = 0
    for c in gene:
        if c == studente:
            i+=1
    return i-int(quantita) if int(quantita) > i else int(quantita) - i

def fitnessFasceOrarie(gene: str, fasceStudente, studente: str, studyroom: int):
    output = 0
    separateGene = gene.split(',')
    studyroomList = []
    n = int(len(separateGene) / studyroom)
    for i in range(studyroom):
        studyroomList.append(separateGene[i*n: (i+1)*n + 1])
    for i in range(len(studyroomList[0])):
        count = 0
        for j in range(len(studyroomList)):
            if studente in studyroomList[j][i]:
                count += 1
        if count == 1:
            output += 1
        else:
            output -= count
    return output

