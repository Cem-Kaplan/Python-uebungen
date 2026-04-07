import tkinter as tk

"""
MINI TASCHENRECHNER
Cem Kaplan
tkinter und Python
"""

aktuellen_text:int = 0

def ende():
    w.destroy()

def text_aktualisieren(zahl):
    global aktuellen_text
    aktuellen_text += zahl
    zahlen_bereich.config(text=aktuellen_text)

def eins_eingeben():
    print("1")
    text_aktualisieren(1)

def zwei_eingeben():
    print("2")
    text_aktualisieren(2)

def drei_eingeben():
    print("3")
    text_aktualisieren(3)

w = tk.Tk()

zahlen_bereich = tk.Label(w, width=100, height=20, text=aktuellen_text)
zahlen_bereich.pack(padx=10, pady=10)

b = tk.Button(w, text="Beenden", command=ende, width=10)
b.pack(pady=10, padx=10)

#zahlen
b_eins = tk.Button(w, text="1", command=eins_eingeben, width=10)
b_zwei = tk.Button(w, text="2", command=zwei_eingeben, width=10)
b_drei = tk.Button(w, text="3", command=drei_eingeben, width=10)

b_eins.pack(pady=10, padx=10)
b_zwei.pack(pady=10, padx=10)
b_drei.pack(pady=10, padx=10)

w.mainloop()