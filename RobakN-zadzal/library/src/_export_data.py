import json
from ._check_filename import check_filename

def export_data(dataset: dict, destination_filename: str, file_format: str = "json") -> bool:
    if not check_filename(destination_filename, file_format, "w"):
        return False

    if file_format == "json":
        json_object = json.dumps(dataset)
        with open(destination_filename, "w") as out_file:
            out_file.write(json_object)
        return True
    elif file_format == "txt":
        with open(destination_filename, "w") as out_file:
            out_file.write(f"Srednie dla plci:\n")
            for key, value in dataset["srednie_gender"].items():
                out_file.write(f"{key}:\nKobiety: {value['K']}\n")
                out_file.write(f"Mezczyzni: {value['M']}\n")
            out_file.write(f"Srednie dla wieku:\n")
            for key, value in dataset['srednie_wiek'].items():
                out_file.write(f"{key}: {value}\n")
            out_file.write(f"Wspolczynniki korelacji:\n")
            for key, value in dataset['korelacje'].items():
                out_file.write(f"{key}: {value}\n")
    else:
        print("Wybrany format nie jest obsługiwany przez program")
    return False

