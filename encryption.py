
alfabeti = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

katrori1 = "EFGHIJKLMNOPQRSTUVWXYABCD"
katrori2 = "MNOPQRSTUVWXYZABCDEFGHIJKL"
katrori3 = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
katrori4 = "STUVWXYZABCDEFGHIJKLMNOPQR"


def enkripto(teksti):
    teksti = teksti.upper().replace("J", "I")
    teksti_enkriptuar = ""
    for shkronja in teksti:
        if shkronja in alfabeti:
            pozicioni = alfabeti.find(shkronja)
            katrori_per_shkronjen = katrori1
            if pozicioni >= 6:
                katrori_per_shkronjen = katrori2
            if pozicioni >= 12:
                katrori_per_shkronjen = katrori3
            if pozicioni >= 18:
                katrori_per_shkronjen = katrori4

            shkronja_e_enkriptuar = katrori_per_shkronjen[pozicioni]
            teksti_enkriptuar += shkronja_e_enkriptuar
        else:
            teksti_enkriptuar += shkronja

    return teksti_enkriptuar


mesazhi = "KY ESHTE NJE TEST"
mesazhi_i_enkriptuar = enkripto(mesazhi)
print("Mesazhi origjinal:", mesazhi)
print("Mesazhi i enkriptuar:", mesazhi_i_enkriptuar)