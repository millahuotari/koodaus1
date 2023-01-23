from pprint import pformat, pprint
from time import ctime
import time

aikaleima = time.time()

#aikaleima = time.time()

#print(aikaleima)

#aikateksti = time.ctime(aikaleima)

#print(aikateksti)

#aika1 = time.time()

#time.sleep(3)

#aika2 = time.time()

#print(aika1)
#print(aika2)
#print(aika2 - aika1)

esimerkki_kuvio = {
    "nimi": "Esimerkki",
    "tyyppi": "monikulmio",
    "luotu": ctime(),
    "pisteet": [
        {"x": 10, "y": 20, "z": 30},
        {"x": 20, "y": 5, "z": 10},
        {"x": 30, "y": 15, "z": 20},
    ]
}

pprint(esimerkki_kuvio, sort_dicts=False)

esimerkki_kuvio_muotoiltu_teksti = pformat(esimerkki_kuvio)

# Muutetaan muotoiltu teksti isoiksi kirjaimiksi ja tulostetaan
# Huom: \n = rivinvaihto
print("Muotoiltu teksti:\n", esimerkki_kuvio_muotoiltu_teksti.upper())