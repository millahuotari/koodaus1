# Tähän mennessä käytettyjä funktioita
# print(X) # Tulostetaan X
# X = input() # luetaan merkkijono muuttujaan X
# str(X) # muutetaan X merkkijonoksi


def kysy_nimi():
    nimi = input("Anna nimi: ")
    return nimi


def kysy_nimet(lkm):
    nimet = []
    while len(nimet) < lkm:
        nimi = kysy_nimi()
        nimet.append(nimi)
    return nimet

if __name__ == "__main__":
    print("Testataan kolmella nimellä")
    nimilista = kysy_nimet(3)
    print("Tulos:", nimilista)
    