valeurs = [1,2,5,10,20,50,100,200,500]

#Entrées : Ensemble P d’entiers (valeurs), entier s (sommeAREndre)
#Sortie  : Liste de pièces de P, minimale, dont la somme vaut s
def renduMonnaie(valeurs, sommeARendre):
    liste = []
    indice = len(valeurs) - 1

    while sommeARendre > 0:
        piece = valeurs[indice] #glouton
        if piece > sommeARendre:
            indice -= 1
        else:
            liste.append(piece)
            sommeARendre -= piece
    
    return liste

euro = [1,2,5,10,20,50,100,200,500]
print(renduMonnaie(euro,7))