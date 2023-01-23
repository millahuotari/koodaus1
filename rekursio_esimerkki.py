def kysy_nimet_rekursiolla(jäljellä, nimet=None):
    if jäljellä == 0:
        return nimet
    if nimet is None:
        nimet = []
    nimi = input("Anna nimi: ")
    return kysy_nimet_rekursiolla(jäljellä - 1, nimet + [nimi])

    
    nimet = kysy_nimet_rekursiolla(4)
    print(nimet)