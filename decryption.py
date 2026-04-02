alfabeti = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

katrori1 = "EFGHIJKLMNOPQRSTUVWXYABCD"
katrori2 = "MNOPQRSTUVWXYZABCDEFGHIJKL"
katrori3 = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
katrori4 = "STUVWXYZABCDEFGHIJKLMNOPQR"

# Simple encryption
def enkripto(teksti):
    teksti = teksti.upper().replace("J", "I")
    rezultati = ""
    katrorët = [katrori1, katrori2, katrori3, katrori4]

    for i, shkronja in enumerate(teksti):
        if shkronja in alfabeti:
            katrori = katrorët[i % 4]  # cikël 1-4
            rezultati += katrori[alfabeti.index(shkronja)]
        else:
            rezultati += shkronja
    return rezultati

# Simple decryption
def dekripto(teksti):
    teksti = teksti.upper().replace("J", "I")
    rezultati = ""
    katrorët = [katrori1, katrori2, katrori3, katrori4]

    for i, shkronja in enumerate(teksti):
        if shkronja in alfabeti:
            katrori = katrorët[i % 4]
            rezultati += alfabeti[katrori.index(shkronja)]
        else:
            rezultati += shkronja
    return rezultati

# Shembull
mesazhi = "KY ESHTE NJE TEST"
mesazhi_i_enkriptuar = enkripto(mesazhi)

print("Enkriptuar:", mesazhi_i_enkriptuar)
print("Dekriptuar:", dekripto(mesazhi_i_enkriptuar))