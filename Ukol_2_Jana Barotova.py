#Ukol 2 pro Programování v Pythonu - Jana Barotová

import requests 

def get_info_by_ico(ico: int):
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"{response.json()["popis"].split("|")[1]}")
        return None
    return response.json()

def get_info_by_name(name: str):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
    data = {"obchodniJmeno": name}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        return None

    response_data = response.json()

    return {"subjekty": response_data["ekonomickeSubjekty"],
            "pocet_subjektu": response_data["pocetCelkem"]}


def print_single_data(subject_data):
    print("\nObchodní jméno:")
    print(subject_data["obchodniJmeno"])
    print("Sídlo:")
    print(subject_data["sidlo"]["textovaAdresa"])

def print_subjects_data(subjects_data):
    print(f"Celkový počet: {subjects_data.get('pocet_subjektu')}")
    for subject in subjects_data.get('subjekty'):
        print(f'{subject["obchodniJmeno"]}, {subject["ico"]}')

def search_by_ico():
    try:
        ico = int(input("Zadejte IČO subjektu: "))
    except ValueError:
        print("Nezadali jste číslo, ukončuji aplikaci")
        exit()

    subject_data = get_info_by_ico(ico)

    if subject_data is None:
        print(f"Subjekt nebyl nalezen nebo server neodpověděl správně, ukončuji aplikaci")
        exit()

    print_single_data(subject_data)

def search_by_name():
    subject_name = input("\nZadejte část názvu firmy: ")
    subjects_data = get_info_by_name(subject_name)

    if subjects_data is None:
        print(f"Server neodpověděl správně, ukončuji aplikaci")
        exit()

    print_subjects_data(subjects_data)

def main():
    search_by_ico()
    search_by_name()

main()




