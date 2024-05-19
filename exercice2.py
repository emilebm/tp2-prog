import csv

def charger_pokemons_csv(nom_fichier):

    with open(nom_fichier, newline="") as pokemon_csv:
        lecteur_pokemon = csv.reader(pokemon_csv)
        
        
        stats_tous = []
        liste_noms = []
#IMPORTANT : Les listes et les noms seront rentrés dans le même ordre

        for i in lecteur_pokemon:
            stats = [int(s) for s in i[1:]] 
#rentre chaque statistique d'un pokémon dans une liste d'ints
            stats_tous.append(stats)#et les met dans une autre liste
            liste_noms.append(i[0])
        dictionnaire = {nom :[] for nom in liste_noms}
    #crée des dictionnaires vides avec les noms des pokémons comme clés
        
        
        for nom in liste_noms:
            dictionnaire[nom] = stats_tous[liste_noms.index(nom)]
            

    return dictionnaire
        

pkmn = charger_pokemons_csv("pokemon.csv")
for nom,stats in pkmn.items():
    print(f"{nom}: {stats}")
print(isinstance(pkmn,dict))
print(isinstance(pkmn["Pikachu"],list))
print(isinstance(pkmn["Pikachu"][0], int))
