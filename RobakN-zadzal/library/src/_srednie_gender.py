def srednie_gender(dataset: dict) -> dict:
    K, M = [], []
    for osoba in dataset.values():
        if osoba["gender"] == "male":
            M.append(osoba)
        else:
            K.append(osoba)
    # Srednia z pierwszego dnia i ostatniego powie nam czy ten wskaznik
    # wzrasta srednio szybciej u kobiet czy u mezczyzn
    srednie_K_M = {"pierwszy_dzien": {"K": 0, "M": 0},
                   "ostatni_dzien": {"K": 0, "M": 0},
                   "pelen_okres": {"K": 0, "M": 0}}

    # Obliczanie srednich
    for kobieta in K:
        #suma dla 1go dnia:
        srednie_K_M["pierwszy_dzien"]["K"] += kobieta["total_UPDRS"][0]
        #suma dla ostatniego dnia:
        srednie_K_M["ostatni_dzien"]["K"] += kobieta["total_UPDRS"][-1]
        #suma dla calego okresu badania - srednie dla kazdej osoby
        srednie_K_M["pelen_okres"]["K"] += sum(kobieta["total_UPDRS"]) / len(kobieta["total_UPDRS"])
    #odpowiednie srednie - ostateczne:
    srednie_K_M["pierwszy_dzien"]["K"] /= len(K)
    srednie_K_M["ostatni_dzien"]["K"] /= len(K)
    srednie_K_M["pelen_okres"]["K"] /= len(K)

    for mezczyzna in M:
        #suma dla 1go dnia
        srednie_K_M["pierwszy_dzien"]["M"] += mezczyzna["total_UPDRS"][0]
        #suma dla ostatniego dnia
        srednie_K_M["ostatni_dzien"]["M"] += mezczyzna["total_UPDRS"][0]
        #suma dla calego okresu badania
        srednie_K_M["pelen_okres"]["M"] += sum(mezczyzna["total_UPDRS"]) / len(mezczyzna["total_UPDRS"])
    #odpowiednie srednie:
    srednie_K_M["pierwszy_dzien"]["M"] /= len(M)
    srednie_K_M["ostatni_dzien"]["M"] /= len(M)
    srednie_K_M["pelen_okres"]["M"] /= len(M)

    #zaokraglanie wartosci
    for klucz, wartosc in srednie_K_M.items():
        srednie_K_M[klucz]["K"] = round(wartosc["K"], 2)
        srednie_K_M[klucz]["M"] = round(wartosc["M"], 2)

    return srednie_K_M
