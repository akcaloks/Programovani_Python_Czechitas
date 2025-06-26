import requests
import json

# ======= ČÁST 1: Vyhledání subjektu podle IČO =======
ico = input("Zadejte IČO subjektu: ")
url_ico = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico

odpoved_ico = requests.get(url_ico)  # posíláme GET požadavek
data_ico = odpoved_ico.json()        # převod odpovědi na JSON

# Výpis informací o subjektu
print()
print("Název subjektu:")
print(data_ico["obchodniJmeno"])
print("Adresa sídla:")
print(data_ico["sidlo"]["textovaAdresa"])

# ======= ČÁST 2: Vyhledání subjektu podle názvu =======
nazev = input("\nZadejte název subjektu, který chcete vyhledat: ")

url_nazev = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
hlavicky = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
data_nazev = {
    "obchodniJmeno": nazev
}
odpoved_nazev = requests.post(url_nazev, headers=hlavicky, json=data_nazev)
vysledek = odpoved_nazev.json()

print()
print("Nalezeno subjektů:", vysledek["pocetCelkem"])

# ======= BONUS: Získání právních forem =======
url_ciselnik = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat"
data_ciselnik = {
    "kodCiselniku": "PravniForma",
    "zdrojCiselniku": "res"
}
odpoved_ciselnik = requests.post(url_ciselnik, headers=hlavicky, json=data_ciselnik)
ciselnik = odpoved_ciselnik.json()
polozky = ciselnik["ciselniky"][0]["polozkyCiselniku"]

# Pomocná funkce pro hledání názvu právní formy
def najdi_pravni_formu(kod):
    for polozka in polozky:
        if polozka["kod"] == kod:
            return polozka["nazev"]
    return "Neznámá právní forma"

# Výpis subjektů se jménem, IČO a právní formou
for subjekt in vysledek["ekonomickeSubjekty"]:
    jmeno = subjekt["obchodniJmeno"]
    ico = subjekt["ico"]
    kod_pravni_formy = subjekt["pravniForma"]
    nazev_pravni_formy = najdi_pravni_formu(kod_pravni_formy)
    print(f"{jmeno}, {ico}, {nazev_pravni_formy}")