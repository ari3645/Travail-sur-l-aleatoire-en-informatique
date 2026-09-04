"""Simulation de lancers de dés (Problème du Duc de Toscane / Galilée).

Étude empirique de la fréquence des sommes obtenues en lançant trois dés à 6 faces,
notamment pour comparer le nombre d'apparitions de la somme 10 par rapport à la somme 9.
"""

from random import randint


def lance() -> int:
    """Simule le jet de trois dés équilibrés à 6 faces.

    Returns:
        int: La somme des valeurs obtenues (entre 3 et 18).
    """
    return randint(1, 6) + randint(1, 6) + randint(1, 6)


def test(n: int) -> tuple[int, int]:
    """Simule n tirages de 3 dés et compte le nombre de fois où la somme vaut 10 et 9.

    Args:
        n (int): Nombre d'expérimentations (lancers de 3 dés).

    Returns:
        tuple[int, int]:
            - Nombre d'occurrences de la somme égale à 10.
            - Nombre d'occurrences de la somme égale à 9.
    """
    valeur_10 = 0
    valeur_9 = 0
    for _ in range(n):
        res = lance()
        if res == 10:
            valeur_10 += 1
        elif res == 9:
            valeur_9 += 1
    return valeur_10, valeur_9


if __name__ == "__main__":
    n_simulations = 1_000_000
    compte_10, compte_9 = test(n_simulations)
    print(f"Sur {n_simulations:,} lancers de 3 dés :")
    print(f"  - Somme 10 : {compte_10} fois ({compte_10 / n_simulations * 100:.2f}%)")
    print(f"  - Somme  9 : {compte_9} fois ({compte_9 / n_simulations * 100:.2f}%)")