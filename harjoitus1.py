# Parit pikanäppäimet:
# VSCoden komentopaletti Ctrl+Shift+P
# Rivien kommentointi Ctrl + ' (Windows)
# Ohjelman pysäyttäminen Ctrl + C

nimet = []

# Vaihtoehto 1

nimi = input("Anna nimi: ")
nimet.append(nimi)
nimi = input("Anna nimi: ")
nimet.append(nimi)
nimi = input("Anna nimi: ")
nimet.append(nimi)
nimi = input("Anna nimi: ")
nimet.append(nimi)
nimi = input("Anna nimi: ")
nimet.append(nimi)

# Vaihtoehto 2
for i in (1, 6):
    nimi = input("Anna nimi: " + str(i) + ": ")
    nimet.append(nimi)

# while True:
#    nimi = input("Anna nimi: ")
#    nimet.append(nimi)
#    if len(nimet) >= 5:
#        break
 
while len(nimet) < 5:
     nimi = input("Anna nimi: ")
     nimet.append(nimi)
     
print("Nimet:", nimet)