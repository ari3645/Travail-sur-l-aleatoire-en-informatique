"""Module d'expérimentation pour la génération de nombres aléatoires.

Compte la fréquence d'apparition d'entiers générés aléatoirement entre 1 et 100.
"""

from random import randint


def generation(t: int) -> tuple[dict[int, int], int]:
    """Génère t entiers aléatoires entre 1 et 100 et compte leurs occurrences.

    Args:
        t (int): Nombre de tirages à effectuer.

    Returns:
        tuple[dict[int, int], int]:
            - Dictionnaire associant chaque valeur à son nombre d'occurrences.
            - Nombre de valeurs distinctes obtenues.
    """
    dico: dict[int, int] = {}
    for _ in range(t):
        a = randint(1, 100)
        dico[a] = dico.get(a, 0) + 1

    return dico, len(dico)


if __name__ == "__main__":
    resultats, nombre_valeurs = generation(1_000_000)
    print(f"Nombre de valeurs uniques obtenues: {nombre_valeurs}")
    print(f"Exemple de répartition (10 premiers): {dict(list(resultats.items())[:10])}")
