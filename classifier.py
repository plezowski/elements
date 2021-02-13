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


def lire_fichier(nom_fichier: str = "liste/elements.csv", clés: tuple = CLÉS) -> list:
    éléments = []
    with open(nom_fichier, "r", encoding="utf-8") as f:
        première_ligne = True
        for ligne in f:
            if première_ligne:
                première_ligne = False
                continue
            données = ligne.split(",")
            élément = {clés[i]: données[i].strip() for i in range(len(clés))}
            éléments.append(élément)
    return éléments


if __name__ == "__main__":
    éléments = lire_fichier()
    for e in éléments:
        print(e.get("Nom", "inconnu"))
