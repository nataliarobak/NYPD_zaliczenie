import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import pearsonr

def korelacje(dataset: dict, plot: bool = False) -> dict:
    data = {"NHR": [],
            "HNR": [],
            "motor_UPDRS": [],
            "total_UPDRS": []}

    for osoba in dataset.values():
        for wspolczynnik in data.keys():
            data[wspolczynnik].append(osoba[wspolczynnik])

    means = {}
    for wspolczynnik in data.keys():
        data[wspolczynnik] = pd.DataFrame(data[wspolczynnik])
        means[wspolczynnik] = data[wspolczynnik].mean()

    nhr_f = pd.DataFrame({"wartosc_NHR": means["NHR"], "czas_pomiaru": range(1, 169)})
    hnr_f = pd.DataFrame({"wartosc_HNR": means["HNR"], "czas_pomiaru": range(1, 169)})
    m_updrs_f = pd.DataFrame({"wartosc_MotorUPDRS": means["motor_UPDRS"], "nhr": means["NHR"], "hnr": means["HNR"]})
    t_updrs_f = pd.DataFrame({"wartosc_TotalUPDRS": means["total_UPDRS"], "nhr": means["NHR"], "hnr": means["HNR"]})

    #wartosci wspolczynnika korelacji oraz istotnosci statystycznej (zmienne *_p służą sprawdzeniu, czy korelacje są istotne)
    nhr_korelacja = nhr_f["wartosc_NHR"].corr(nhr_f["czas_pomiaru"])
    nhr_p = pearsonr(nhr_f["wartosc_NHR"], nhr_f["czas_pomiaru"])
    hnr_korelacja = hnr_f["wartosc_HNR"].corr(hnr_f["czas_pomiaru"])
    hnr_p = pearsonr(hnr_f["wartosc_HNR"], nhr_f["czas_pomiaru"])

    mupdrs_nhr_kor = m_updrs_f["wartosc_MotorUPDRS"].corr(nhr_f["wartosc_NHR"])
    mupdrs_nhr_p = pearsonr(m_updrs_f["wartosc_MotorUPDRS"], nhr_f["wartosc_NHR"])
    mupdrs_hnr_kor = m_updrs_f["wartosc_MotorUPDRS"].corr(hnr_f["wartosc_HNR"])
    mupdrs_hnr_p = pearsonr(m_updrs_f["wartosc_MotorUPDRS"], hnr_f["wartosc_HNR"])
    tupdrs_nhr_kor = t_updrs_f["wartosc_TotalUPDRS"].corr(nhr_f["wartosc_NHR"])
    tupdrs_nhr_p = pearsonr(t_updrs_f["wartosc_TotalUPDRS"], nhr_f["wartosc_NHR"])
    tupdrs_hnr_kor = t_updrs_f["wartosc_TotalUPDRS"].corr(hnr_f["wartosc_HNR"])
    tupdrs_hnr_p = pearsonr(t_updrs_f["wartosc_TotalUPDRS"], hnr_f["wartosc_HNR"])

    if plot:
        opcja = input("Chcesz zapisac pliki z wykresami? [y/n]: ")
        while opcja.lower() not in ['y', 'yes', 'n', 'no', '']:
            opcja = input("Chcesz zapisac pliki z wykresami? [y/n]: ")
        if opcja.lower() in ['y', 'yes', '']:
            filename = input("Wprowadz nazwe lub sciezke do pliku: ")
            while filename == '':
                filename = input("Wprowadz nazwe lub sciezke do pliku (nie moze byc pusta): ")
            nhr_f.plot(x="czas_pomiaru", y="wartosc_NHR", kind="scatter",
                       title="Zaleznosc miedzy czasem pomiaru a wartoscia NHR")
            plt.savefig(f"{filename}_nhr.png")
            hnr_f.plot(x="czas_pomiaru", y="wartosc_HNR", kind="scatter",
                       title="Zaleznosc miedzy czasem pomiaru a wartoscia HNR")
            plt.savefig(f"{filename}_hnr.png")
            m_updrs_f.plot(x="nhr", y="wartosc_MotorUPDRS", kind="scatter", title="Zaleznosc miedzy wartoscia NHR a wartoscia motor UPDRS")
            plt.savefig(f"{filename}_mupdrs_nhr.png")
            m_updrs_f.plot(x="hnr", y="wartosc_MotorUPDRS", kind="scatter", title="Zaleznosc miedzy wartoscia HNR a wartoscia motor UPDRS")
            plt.savefig(f"{filename}_mupdrs_hnr.png")
            t_updrs_f.plot(x="nhr", y="wartosc_TotalUPDRS", kind="scatter", title="Zaleznosc miedzy wartoscia NHR a wartoscia total UPDRS")
            plt.savefig(f"{filename}_tupdrs_nhr.png")
            t_updrs_f.plot(x="hnr", y="wartosc_TotalUPDRS", kind="scatter", title="Zaleznosc miedzy wartoscia HNR a wartoscia total UPDRS")
            plt.savefig(f"{filename}_tupdrs_hnr.png")

            plt.show()

    return {"NHR_czas": nhr_korelacja,
            "HNR_czas": hnr_korelacja,
            "Motor_UPDRS_NHR": mupdrs_nhr_kor,
            "Motor_UPDRS_HNR": mupdrs_hnr_kor,
            "Total_UPDRS_NHR": tupdrs_nhr_kor,
            "Total_UPDRS_HNR": tupdrs_hnr_kor}
