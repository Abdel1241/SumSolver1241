

def additionner(nombre1, nombre2):
    return nombre1 + nombre2

nombre1 = float(input("Entrez le premier chiffre : "))
nombre2 = float(input("Entrez le deuxième chiffre : "))

resultat = additionner(nombre1, nombre2)

# Afficher le résultat de l'addition
print("Le résultat de l'addition de", nombre1, "et", nombre2, "est :", resultat)
