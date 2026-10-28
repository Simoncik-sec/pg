
def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    if cilova_pozice[0] < 1 or cilova_pozice[0] > 8 or cilova_pozice[1] < 1 or cilova_pozice[1] > 8:
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    rozdil_radku = abs(aktualni_pozice[0] - cilova_pozice[0])
    rozdil_sloupcu = abs(aktualni_pozice[1] - cilova_pozice[1])

    if typ == "král":
        if rozdil_radku <= 1 and rozdil_sloupcu <= 1:
            if rozdil_radku != 0 or rozdil_sloupcu != 0:
                return True

    elif typ == "jezdec":
        if rozdil_radku == 2 and rozdil_sloupcu == 1:
            return True
        elif rozdil_radku == 1 and rozdil_sloupcu == 2:
            return True

    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))

    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice))


