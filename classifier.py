#!/usr/bin/env python3

from io import TextIOBase
import colorama
import sys

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

    def __init__(self, liste: list = []) -> None:
        if liste == []:
            self.num = 0
            self.nom = "__aucun__"
        else:
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

    def estVide(self) -> bool:
        return self.num == 0

    def versSymboleCar(self):
        if self.estVide():
            return "  "
        else:
            return f"{self.symbole:2}"

    def __repr__(self) -> str:
        if self.estVide():
            return "Aucun élément"
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


def créer_tableau(éléments: list) -> list:
    tableau = []
    for e in éléments:
        while e.période > len(tableau):
            tableau.append(list(Élément() for _ in range(18)))
        tableau[e.période - 1][e.groupe - 1] = e
    return tableau


def afficher_tableau(tableau: list, couleur=None) -> None:
    if couleur:
        print(end=couleur)
    print("┌─" + 17 * "─┬─" + "─┐")
    for i in range(len(tableau)):
        print(end="│")
        for élément in tableau[i]:
            print(élément.versSymboleCar(), end="│")
        print()
        if i < len(tableau) - 1:
            print("├─" + 17 * "─┼─" + "─┤")
        else:
            print("└─" + 17 * "─┴─" + "─┘")
    if couleur:
        print(end=colorama.Style.RESET_ALL)


def créer_tableau_markdown(tableau: list, nom_fichier: str = "tableau.md") -> None:
    with open(nom_fichier, "w", encoding="utf-8") as f:
        texte = "|" + "|".join("<!-- -->" for _ in tableau[0]) + "|\n"
        texte += "|" + "|".join(":------:" for _ in tableau[0]) + "|\n"
        for i in range(len(tableau)):
            for élément in tableau[i]:
                texte += "|" + f"{élément.versSymboleCar():^8}"
            texte += "|\n"
        f.write(texte)


if __name__ == "__main__":
    éléments = lire_fichier()
    tableau = créer_tableau(éléments)
    afficher_tableau(tableau, couleur=colorama.Fore.RED)
    créer_tableau_markdown(tableau, sys.argv[1] if len(sys.argv) else "tableau.md")

