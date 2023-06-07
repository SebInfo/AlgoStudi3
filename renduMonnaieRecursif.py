def rendu_monnaie(s, P):
    if s == 0:
        return []

    meilleur_rendu = None
    meilleur_nombre_pieces = float('inf')

    for p in P:
        if p <= s:
            sous_rendu = rendu_monnaie(s - p, P)
            nombre_pieces = len(sous_rendu) + 1

            if nombre_pieces < meilleur_nombre_pieces:
                meilleur_rendu = [p] + sous_rendu
                meilleur_nombre_pieces = nombre_pieces

    return meilleur_rendu

def rendu_monnaie_nbrPiece(s, P):
    if s == 0:
        return 0
    n = float('inf')
    for p in P:
        if p <= s:
            np = rendu_monnaie_nbrPiece(s - p, P)
            if (np < n):
                n=np
    return 1+n

# Exemple d'utilisation
euros = [1, 2, 5, 10, 20, 50]
nonCanonique = [1,3,4]
somme = 6
resultat = rendu_monnaie(somme, nonCanonique)
print("Rendu optimal pour la somme", somme, "est", resultat , " pièce(s)")
nbrPiece= rendu_monnaie_nbrPiece(somme, nonCanonique)
print("Le nombre de pièce nécessaire est :", nbrPiece)