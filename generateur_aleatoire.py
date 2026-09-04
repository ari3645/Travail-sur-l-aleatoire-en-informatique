"""Générateurs de nombres pseudo-aléatoires et tests de distribution.

Ce module rassemble diverses fonctions d'expérimentation pour la génération
de nombres aléatoires (générateur congruentiel linéaire - LCG, horloge système,
permutations arithmétiques) ainsi que des outils de vérification statistique
(répartition par quantiles / histogrammes).
"""

from datetime import datetime
from random import choice, randint


def gen_test3(x: int, y: int) -> list[int]:
    """Génère une suite arithmétique u_(n+1) = u_n + y de 101 termes."""
    l = [x]
    for _ in range(100):
        x += y
        l.append(x)
    return l


def moyenne(l: list[float]) -> float:
    """Calcule la moyenne arithmétique d'une liste de nombres."""
    if not l:
        return 0.0
    return sum(l) / len(l)


def compteur_verif_102(l: list[float]) -> list[int]:
    """Compte la répartition des éléments d'une liste l en 10 tranches relatives
    par rapport au dernier élément x = l[-1].
    """
    x = l[-1]
    counts = [0] * 10
    step = x / 10.0

    for item in l:
        if item < step:
            counts[0] += 1
        elif item < step * 2:
            counts[1] += 1
        elif item < step * 3:
            counts[2] += 1
        elif item < step * 4:
            counts[3] += 1
        elif item < step * 5:
            counts[4] += 1
        elif item < step * 6:
            counts[5] += 1
        elif item < step * 7:
            counts[6] += 1
        elif item < step * 8:
            counts[7] += 1
        elif item < step * 9:
            counts[8] += 1
        else:
            counts[9] += 1

    return counts


def gen_test(x: int, y: int, z: int) -> int:
    """Générateur d'essai #1 : choisit aléatoirement une combinaison produit/quotient."""
    r = randint(0, 2)
    if r == 0:
        return int(x * z / y)
    if r == 1:
        return int(x * y / z)
    return int(y * z / x)


def gen_test_valeur(x: int, y: int, z: int) -> list[int]:
    """Donne les trois valeurs possibles pouvant être générées par gen_test."""
    return [int(x * z / y), int(x * y / z), int(y * z / x)]


def gen_test2(x: int, y: int, z: int) -> int:
    """Générateur d'essai #2 : multiplie une combinaison par un grand entier aléatoire 64-bit."""
    r = randint(0, 2**64)
    return (x + y - z) * r


def gen_test_liste(x: int, y: int, z: int) -> int:
    """Générateur d'essai #3 : multiplie une combinaison par un élément choisi dans [0, 99]."""
    l = list(range(100))
    return (x + y - z) * choice(l)


def gen_test_horl(x: int) -> float:
    """Générateur pseudo-aléatoire basé sur les composantes de l'horloge système (datetime.now)."""
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    sec = now.second
    mili = now.microsecond

    # Évite la division par zéro si heure == 0
    h_denom = hour if hour != 0 else 24
    return (((x + year - day + month) * minute * sec) / h_denom) * mili


def compteur_verif_test(x: int, y: int, z: int, l: list[int]) -> list[int]:
    """Compte la fréquence de chaque valeur de l dans 100 tirages de gen_test."""
    li = [gen_test(x, y, z) for _ in range(100)]
    r_1, r_2, r_3 = 0, 0, 0

    for val in li:
        if val == l[0]:
            r_1 += 1
        elif val == l[1]:
            r_2 += 1
        else:
            r_3 += 1

    return [r_1, r_2, r_3]


def moyenne_compteur(x: int) -> list[float]:
    """Calcule la moyenne des fréquences obtenues par compteur_verif_test sur x répétitions."""
    valeurs_cible = gen_test_valeur(25, 46, 23)
    s = compteur_verif_test(25, 46, 23, valeurs_cible)

    for _ in range(x):
        res = compteur_verif_test(25, 46, 23, valeurs_cible)
        s[0] += res[0]
        s[1] += res[1]
        s[2] += res[2]

    return [s[0] / x, s[1] / x, s[2] / x]


def gen_cong_lin(mult: int, exp: int, incr: int, xn: int) -> list[int]:
    """Générateur Congruentiel Linéaire (LCG).

    Calcule la suite : x_(n+1) = (mult * x_n + incr) mod (2^exp)
    Génère une suite de 100 000 valeurs.
    """
    assert xn > 0, "xn doit être supérieur à 0"
    assert mult > 1, "mult doit être plus grand que 1"
    assert exp > 0, "exp doit être plus grand que 0"

    l = [xn]
    modulus = 2**exp
    for _ in range(100_000):
        xn = ((mult * xn) + incr) % modulus
        l.append(xn)

    return l


def verif_cong_lin(l: list[int]) -> float:
    """Teste et calcule une moyenne statistique sur des sous-échantillons d'une liste."""
    r = randint(0, 1)
    l_copy = l.copy()

    if r == 0:
        return sum(l_copy) / len(l_copy)
    else:
        z = (len(l_copy) - 1) // 2 if len(l_copy) % 2 == 1 else len(l_copy) // 2
        l1 = [l_copy.pop() for _ in range(z)]
        l2 = [l_copy.pop() for _ in range(len(l_copy))]

        moy_l1 = sum(l1) / len(l1) if l1 else 0
        moy_l2 = sum(l2) / len(l2) if l2 else 0

        u = randint(0, 1)
        return moy_l2 if u == 0 else moy_l1


def compteur_verif_50(x: int, y: int) -> list[int]:
    """Compte la répartition en 2 demi-groupes (<= x/2 et > x/2) sur y tirages de [1, x]."""
    l = [randint(1, x) for _ in range(y)]
    compt_m_50 = sum(1 for i in l if i <= x / 2)
    compt_p_50 = y - compt_m_50
    return [compt_m_50, compt_p_50]


def compteur_verif_25(x: int, y: int) -> tuple[list[int], float]:
    """Compte la répartition en 4 quartiles sur y tirages de [1, x]
    et renvoie la répartition ainsi que le pourcentage d'écart (max - min).
    """
    l = [randint(1, x) for _ in range(y)]
    c1, c2, c3, c4 = 0, 0, 0, 0

    for i in l:
        if i < x / 4:
            c1 += 1
        elif i < x / 2:
            c2 += 1
        elif i < (x / 4) * 3:
            c3 += 1
        else:
            c4 += 1

    counts = [c1, c2, c3, c4]
    ecart_pct = (max(counts) - min(counts)) * 100 / y
    return counts, ecart_pct


def compteur_verif_10(x: int, y: int) -> tuple[list[int], float]:
    """Compte la répartition en 10 déciles sur y tirages de [1, x]
    et renvoie la répartition ainsi que le pourcentage d'écart (max - min).
    """
    l = [randint(1, x) for _ in range(y)]
    counts = [0] * 10
    step = x / 10.0

    for i in l:
        idx = min(int(i / step), 9)
        counts[idx] += 1

    ecart_pct = (max(counts) - min(counts)) * 100 / y
    return counts, ecart_pct


def compteur_verif_5(x: int, y: int) -> float:
    """Compte la répartition en 20 tranches (5% chacune) sur y tirages de [1, x]
    et renvoie le pourcentage d'écart (max - min).
    """
    l = [randint(1, x) for _ in range(y)]
    counts = [0] * 20
    step = x / 20.0

    for i in l:
        idx = min(int(i / step), 19)
        counts[idx] += 1

    return (max(counts) - min(counts)) * 100 / y


def compteur_verif_25c(l: list[int]) -> list[int]:
    """Analyse la répartition en 4 quartiles d'une liste l de valeurs (plage max 2^64)."""
    x = 2**64
    c1, c2, c3, c4 = 0, 0, 0, 0

    for i in l:
        if i < x / 4:
            c1 += 1
        elif i < x / 2:
            c2 += 1
        elif i < (x / 4) * 3:
            c3 += 1
        else:
            c4 += 1

    return [c1, c2, c3, c4]


def compteur_verif_5c(l: list[int]) -> list[int]:
    """Analyse la répartition en 20 tranches (5% chacune) d'une liste l de valeurs (plage max 2^64)."""
    x = 2**64
    counts = [0] * 20
    step = x / 20.0

    for i in l:
        idx = min(int(i / step), 19)
        counts[idx] += 1

    return counts


if __name__ == "__main__":
    print("=== Test du Générateur Congruentiel Linéaire (LCG) ===")
    lcg_data = gen_cong_lin(mult=1664525, exp=32, incr=1013904223, xn=42)
    print(f"Nombre d'éléments générés: {len(lcg_data):,}")
    print(f"Moyenne de la séquence: {moyenne(lcg_data):.2f}")

    print("\n=== Test de Répartition par Tranches de 5% ===")
    for p in range(6):
        n = 10**p
        ecart = compteur_verif_5(500, n)
        print(f"  Tirages = {n:7d} | Écart max-min: {ecart:.2f}%")