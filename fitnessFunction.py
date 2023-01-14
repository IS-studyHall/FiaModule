def funzioneQuantita(gene: str, quantita: str, studente: str):
    i = 0
    for c in gene:
        if c == studente:
            i+=1
    return i-int(quantita) if int(quantita) > i else int(quantita) - i
