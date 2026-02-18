import pandas as pd

d = {
    "Spieler1":100,
    "Spieler3":99
}

#Serie erstellen
s = pd.Series(d)

#DataFrame erstellen
df = pd.DataFrame(d, index=["1."])

#csv einlesen
datei = pd.read_csv('datei.csv')

#json einlesen
#json_datei = pd.read_json()