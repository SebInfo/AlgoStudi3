valeurs = [1,2,5,10,20,50,100,200,500]

def renduMonnaie(sommeARendre):
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

print(renduMonnaie(7))