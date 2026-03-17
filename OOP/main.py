class Auto:
    def __init__(self, name, baujahr, geschwindigkeit):
        self.name = name
        self.baujahr = baujahr
        self.geschwindigkeit = geschwindigkeit

    def __str__(self):
        return self.name+ " " + str( self.baujahr )
    
    def __delete__(self):
        print(self)

    def beschleunigen(self):
        self.geschwindigkeit += 1
        return "geschw. von " + self.name + " ist jetzt " + self.geschwindigkeit

audi = Auto("Audi A1", 2020, 0)
print(audi)
del audi