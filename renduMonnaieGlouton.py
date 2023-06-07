valeurs = [1,2,5,10,20,50,100,200,500]

#Entrées : Ensemble P d’entiers croissants (valeurs), entier s (sommeAREndre)
#Sortie  : Liste de pièces de P, minimale, dont la somme vaut s
def renduMonnaie(valeurs, sommeARendre):
    liste = []
    indice = len(valeurs) - 1

    while sommeARendre > 0:
        piece = valeurs[indice] #glouton on commence par la plus grande pièce ou billet
        if piece > sommeARendre:
            indice -= 1
        else:
            liste.append(piece)
            sommeARendre -= piece
    
    return liste
nonCanonique = [1,3,4]
euro = [1,2,5,10,20,50,100,200,500]
print(renduMonnaie(nonCanonique,6))