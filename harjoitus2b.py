import harjoitus2 as h2


if __name__ == "__main__":
    print("Kysytään 2 nimeä:")
    joku_juttu = 1
    nimet = h2.kysy_nimet(2)
    joku_juttu = 2
    nimet.append("Ekstra nimi")
    joku_juttu = 3
    print("Nimet ovat", nimet)