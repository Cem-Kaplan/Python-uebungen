import sys

datei_name = None
datei = None
typ = None

while True:
    try:
        print("Dateinamen eingeben: ")
        datei_name = str(input())
        print("Dateitypen auswählen: \n 1 - txt\n 2 - odt")
        datei_typ = int(input())
        if (datei_typ == 1):
            typ = ".txt"
        elif (datei_typ == 2):
            typ = ".odt"
        else:
            print("Ungültiger typ")
            sys.exit(1)
        datei = open(datei_name + typ, "w")   
        print("Datei: " + datei_name + " erstellt")
    except Exception as e:
        print(f"Fehler, Datei {datei_name} konnte nicht erstellt werden: " + e)
