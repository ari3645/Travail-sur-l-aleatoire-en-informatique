"""Approximation de Pi par la méthode d'Archimède.

Utilise la méthode géométrique d'Archimède basée sur les polygones réguliers
inscrits (borne inférieure a) et circonscrits (borne supérieure b) à un cercle unités.
"""

from math import radians, sin, tan


def archimede(precision: int) -> tuple[float, float]:
    """Calcule un encadrement de Pi à 10^(-precision) près.

    Args:
        precision (int): Nombre de décimales de précision souhaité (ex: 15).

    Returns:
        tuple[float, float]: (borne_inferieure, borne_superieure) encadrant Pi.
    """
    a, b = 0.0, 1.0  # Valeurs initiales arbitraires pour démarrer la boucle
    n = 123  # Nombre initial de côtés du polygone
    seuil = 10 ** (-precision)

    while (b - a) > seuil:
        angle_deg = 180 / n
        a = n * sin(radians(angle_deg))
        b = n * tan(radians(angle_deg))
        n += 1

    return a, b


if __name__ == "__main__":
    p = 15
    inf, sup = archimede(p)
    print(f"Encadrement de Pi avec une précision 10^-{p} :")
    print(f"  Borne inférieure (inscrit)    : {inf:.15f}")
    print(f"  Borne supérieure (circonscrit): {sup:.15f}")
    print(f"  Amplitude de l'écart          : {sup - inf:.2e}")