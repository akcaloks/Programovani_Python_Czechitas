#Ukol 2 pro Programování v Pythonu - Jana Barotová

import requests 
import json

ico = input("Zadejte IČO subjektu: ")
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico

odpoved_ico = requests.get(url)
data_ico = odpoved_ico.json()         

print("\nObchodní jméno:")
print(data_ico["obchodniJmeno"])
print("Sídlo:")
print(data_ico["sidlo"]["textovaAdresa"])

nazev = input("\nZadejte část názvu firmy: ")

url_vyhledat = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
hlavicky = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
data_vyhledani = {
    "obchodniJmeno": nazev
}

odpoved_nazev = requests.post(url_vyhledat, headers=hlavicky, json=data_vyhledani)
data_nazev = odpoved_nazev.json()

print("\nNalezeno subjektů:", data_nazev["pocetCelkem"])
for subjekt in data_nazev["ekonomickeSubjekty"]:
    print(f'{subjekt["obchodniJmeno"]}, {subjekt["ico"]}')
