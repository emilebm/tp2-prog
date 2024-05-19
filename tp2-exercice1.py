import json

with open("data.json", "r", encoding="utf8") as f:
    donnees = json.load(f)
    donnees = donnees["chiffres"]
    
    
with open("complexes.csv", "w", newline="", encoding="utf8") as fichier_csv:
    fichier_csv.write("reel,imaginaire\n")
    for ligne in donnees:
            ligne = [str(el) for el in ligne]
            fichier_csv.write(','.join(ligne) + '\n')