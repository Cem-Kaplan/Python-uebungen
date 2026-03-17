def main(eingabe):
    if eingabe == "":
        print("Ihre eingabe ist nicht vorhanden, bitte nochmal versuchen")
    elif eingabe == "Hallo":
        print("Guten Tag")

print("Hallo, was kann ich für sie tuhen?")

while True:
    try:
        aktuelle_eingabe = str(input())
        main(aktuelle_eingabe)
    except Exception as ausnahme:
        print("Fehler: ", ausnahme)