import datetime

class Ihminen:
    def __init__(self, etunimi, sukunimi, syntymavuosi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.syntymavuosi = syntymavuosi
        
    def __str__(self):
        return self.etunimi + " " + self.sukunimi + " (" + str(self.syntymavuosi) + ")"
        
    def laske_ika(self):
        tanaan = datetime.date.today()
        nykyinen_vuosi = tanaan.year
        return nykyinen_vuosi - self.syntymavuosi
        
henkilo1 = Ihminen ("Pentti", "Peikkonen", 1999)
henkilo2 = Ihminen ("Raija", "Ratanen", 1995)
        
print(henkilo1)
print(henkilo2)
        
print(henkilo1.sukunimi, henkilo1.etunimi, henkilo1.laske_ika())
print(henkilo2.sukunimi, henkilo2.etunimi, henkilo2. laske_ika())