class Auto:
    def __init__(self, rekisterinumero, merkki, malli):
        self.rekisterinumero = rekisterinumero
        self.merkki = merkki
        self.malli = malli
        self.vuosi = None

    def __str__(self) -> str:
        # Muotoillaan Auto-olio stringiksi
        #
        # Muodostetaan ensin "vuosi"-muuttujaan -95 -tyylinen stringi
        
        # Huom. Terniärioperaattori:
                    # A if EHTO else B
                    # Valitsee arvon A jos EHTO on tosi, muuten arvon B
        # Huom2. % = jakojäännös-operaattori
        #               eli X % Y palauttaa arvon joka jää yli kun X jaetaan Y:llä 
        #               (jos X jaettuna Y:llä menee tasan, niin jakojäännös on 0)           
        
        vuosi = f" -{self.vuosi % 100:02d}" if self.vuosi else ""
        return f" {self.merkki} {self.malli}{vuosi} ({self.rekisterinumero})"
        

volkkari = Auto("ABC-123", "Volkswagen", "Golf")
saab = Auto("XYZ-456", "Saab", "En tiiä")
opel = Auto("XXX-123", "Opel", "Astra")

# Atribuutteja voi asettaa myös luokan ulkopuolelta
volkkari.vuosi = 1986
opel.vuosi = 2005

print(volkkari)
print(saab)
print(opel)

