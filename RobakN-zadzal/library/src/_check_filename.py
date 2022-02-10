def check_filename(filename: str, file_format: str = "data", mode: str = "r") -> bool:
    if len(filename) < 6:
        print("Nazwa pliku nie moze posiadac mniej niz 6 znakow.\nSprawdz czy podales rozszerzenie.")
        return False
    elif filename[-(len(file_format)+1):] != f".{file_format}":
        print(f"Plik powinien miec rozszerzenie '.{file_format}'.")
        return False
    try:
        with open(filename, mode):
            pass
        return True
    except FileNotFoundError:
        print("Nie znaleziono tego pliku.")
    except PermissionError:
        print("Nie posiadasz wystarczajaco wysokie uprawnienia aby otworzyc ten plik")
    except OSError:
        print("Wystapil blad przy otwieraniu pliku")
    except Exception:
        print("Wystapil nieznany blad")
    return False
