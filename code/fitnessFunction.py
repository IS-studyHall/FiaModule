def funzioneQuantita(gene: str, quantita: str, studente: str):
    i = 0
    for c in gene:
        if c == studente:
            i+=1
    return i-int(quantita) if int(quantita) > i else int(quantita) - i

def funzioneFasceOrarie(gene: str, fasceStudente, studente: str):
    i = 0
    virgole = 0
    corrette = 0
    errate = 0
    for c in gene:
        for i in range(len(fasceStudente)):
            str = fasceStudente[i]
            if c == ",":
                virgole+=1
            if c == studente:
                if str[virgole] == "1":
                    corrette+=1
                else:
                    errate+=1
    
