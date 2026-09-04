"""Générateur Congruentiel Linéaire (LCG) et tests statistiques.

Ce module implémente l'algorithme du Générateur Congruentiel Linéaire (LCG)
ainsi que les fonctions d'analyse statistique de la qualité de répartition.
"""

from generateur_aleatoire import (
    compteur_verif_5,
    compteur_verif_5c,
    compteur_verif_10,
    compteur_verif_25,
    compteur_verif_25c,
    compteur_verif_50,
    compteur_verif_102,
    gen_cong_lin,
    gen_test,
    gen_test2,
    gen_test3,
    gen_test_horl,
    gen_test_liste,
    gen_test_valeur,
    moyenne,
    moyenne_compteur,
    verif_cong_lin,
)

__all__ = [
    "gen_cong_lin",
    "verif_cong_lin",
    "moyenne",
    "gen_test",
    "gen_test2",
    "gen_test3",
    "gen_test_horl",
    "gen_test_liste",
    "gen_test_valeur",
    "moyenne_compteur",
    "compteur_verif_50",
    "compteur_verif_25",
    "compteur_verif_10",
    "compteur_verif_5",
    "compteur_verif_25c",
    "compteur_verif_5c",
    "compteur_verif_102",
]

if __name__ == "__main__":
    print("=== Démonstration du Générateur Congruentiel Linéaire (LCG) ===")
    a, c, m, seed = 1664525, 1013904223, 32, 42
    seq = gen_cong_lin(a, m, c, seed)
    print(f"Paramètres LCG: a={a}, c={c}, m=2^{m}, x0={seed}")
    print(f"Longueur de la séquence: {len(seq):,}")
    print(f"Premières valeurs: {seq[:5]}")
    print(f"Moyenne de la séquence: {moyenne(seq):.2f}")

    print("\n=== Analyse des quartiles (compteur_verif_25c) ===")
    quartiles = compteur_verif_25c(seq)
    print(f"Répartition par quartiles (Q1, Q2, Q3, Q4): {quartiles}")