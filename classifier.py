#!/usr/bin/env python3

CLÉS = (
    "Numéro Atomique",
    "Nom",
    "Symbole",
    "Masse Atomique",
    "Nombre de neutrons",
    "Nombre de neutrons",
    "Nombre d'électrons",
    "Période",
    "Groupe",
    "Phase",
)


class Élément:
    """Un élément de la classification périodique"""

    def __init__(self, liste: list) -> None:
        self.num = int(liste[0])
        self.nom = liste[1]
        self.symbole = liste[2]
        self.mass = float(liste[3])
        self.neutrons = int(liste[4])
        self.protons = int(liste[5])
        self.électrons = int(liste[6])
        self.période = int(liste[7])
        self.groupe = int(liste[8])
        self.phase = liste[9]

    def __repr__(self) -> str:
        return self.nom


def lire_fichier(nom_fichier: str = "liste/elements.csv", clés: tuple = CLÉS) -> list:
    éléments = []
    with open(nom_fichier, "r", encoding="utf-8") as f:
        première_ligne = True
        for ligne in f:
            if première_ligne:
                première_ligne = False
                continue
            données = ligne.split(",")
            éléments.append(Élément(données))
    return éléments


if __name__ == "__main__":
    éléments = lire_fichier()
    for e in éléments:
        print(e)
