print("Suchalgorithmen")

liste = [9,1,3,5,2,1,6,4,3,2,1,5]

def lineare_suche():

    #es soll die 5 gesucht werden
    gesuchter_wert = 5

    #lineare suche:

    for wert in liste:
        if wert == gesuchter_wert:
            print("5 gefunden an position", liste.index(gesuchter_wert) + 1)
            break

def lineare_suche_mit_mehr_loesungen():
    while True:
        try:
            pos = liste.index(5, pos + 1)
            print(pos)
        except:
            print("Keine Zahl gefunden")
            break
    
lineare_suche_mit_mehr_loesungen()