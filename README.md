# 🎲 Génération de Nombres Aléatoires & Approximations Mathématiques

Projet réalisé dans le cadre du **Grand Oral** (Spécialités Mathématiques / NSI). Ce dépôt regroupe plusieurs expérimentations informatiques et simulations numériques portant sur les générateurs de nombres pseudo-aléatoires, les tests de distribution statistique et des approximations de constantes mathématiques.

---

## 📌 Sommaire

- [Aperçu du Projet](#-aperçu-du-projet)
- [Structure du Dépôt](#-structure-du-dépôt)
- [Description des Modules](#-description-des-modules)
  - [1. Générateurs Pseudo-Aléatoires & Tests](#1-générateurs-pseudo-aléatoires--tests-generateur_aleatoirepy)
  - [2. Générateur Congruentiel Linéaire (LCG)](#2-générateur-congruentiel-linéaire-lcg-generateur_congruentiel_lineairepy)
  - [3. Problème du Duc de Toscane (Dés)](#3-problème-du-duc-de-toscane-hasard_depy)
  - [4. Fréquences de Tirages Aléatoires](#4-fréquences-de-tirages-aléatoires-essai_aleatoirepy)
  - [5. Approximation de Pi par Archimède](#5-approximation-de-pi-par-archimède-mathspy)
- [Installation et Utilisation](#-installation-et-utilisation)
- [Notions Mathématiques et Algorithmiques](#-notions-mathématiques-et-algorithmiques)

---

## 💡 Aperçu du Projet

L'aléatoire en informatique est au cœur de nombreux domaines (cryptographie, simulation Monte-Carlo, jeux vidéo, modélisation physique). Comme un ordinateur est par nature déterministe, on utilise des **générateurs de nombres pseudo-aléatoires (PRNG)**.

Ce projet explore :
1. **Comment fabriquer et tester la qualité d'un générateur pseudo-aléatoire** (répartition uniforme, écarts max/min sur des quantiles).
2. **Le Générateur Congruentiel Linéaire (LCG)**, une méthode classique basée sur l'arithmétique modulaire.
3. **Des simulations empiriques** (probabilités aux dés et problème historique du Duc de Toscane).
4. **L'approximation numérique** (calcul des décimales de $\pi$ selon l'algorithme des polygones d'Archimède).

---

## 📁 Structure du Dépôt

```text
.
├── .gitignore                          # Fichiers à ignorer par Git
├── README.md                           # Documentation du projet
├── generateur_aleatoire.py             # Algorithmes PRNG & batterie de tests statistiques
├── generateur_congruentiel_lineaire.py # Module dédié au Générateur Congruentiel Linéaire (LCG)
├── hasard_de.py                        # Simulation du problème du Duc de Toscane (3 dés)
├── essai_aleatoire.py                  # Expérimentation sur la fréquence de tirage [1, 100]
└── maths.py                            # Approximation de Pi par la méthode d'Archimède
```

---

## ⚙️ Description des Modules

### 1. Générateurs Pseudo-Aléatoires & Tests (`generateur_aleatoire.py`)
Contient plusieurs propositions d'algorithmes de génération et des fonctions d'évaluation statistique :
- **`gen_test_horl(x)`** : Exploite l'entropie de l'horloge système (microsecondes de `datetime.now()`).
- **`gen_cong_lin(mult, exp, incr, xn)`** : Implémente la suite congruentielle $x_{n+1} = (a \cdot x_n + c) \pmod{2^m}$.
- **Tests de répartition** : `compteur_verif_50`, `compteur_verif_25`, `compteur_verif_10`, `compteur_verif_5` mesurent l'écart relatif entre la tranche la plus représentée et la moins représentée (pour évaluer l'uniformité).

### 2. Générateur Congruentiel Linéaire (LCG) (`generateur_congruentiel_lineaire.py`)
Focalisé sur la méthode LCG :
$$x_{n+1} = (a \cdot x_n + c) \pmod m$$
Permet de générer de grandes séquences de nombres (ex: 100 000 termes) et de vérifier leur moyenne théorique ainsi que leur répartition par quartiles.

### 3. Problème du Duc de Toscane (`hasard_de.py`)
Simule le jet de 3 dés équilibrés à 6 faces. Il permet de vérifier empiriquement l'énigme posée à Galilée : *Pourquoi obtient-on plus souvent la somme 10 que la somme 9 en lançant trois dés, alors que les deux sommes possèdent le même nombre de décompositions en 3 entiers ?*
- **Résultat théorique** : $P(S=10) = \frac{27}{216} \approx 12.5\%$ contre $P(S=9) = \frac{25}{216} \approx 11.57\%$.

### 4. Fréquences de Tirages Aléatoires (`essai_aleatoire.py`)
Effectue 1 000 000 de tirages aléatoires d'entiers entre 1 et 100 et vérifie l'équiprobabilité de tirage pour chaque valeur.

### 5. Approximation de Pi par Archimède (`maths.py`)
Implémente la méthode géométrique d'Archimède basées sur les polygones réguliers à $n$ côtés inscrits ($a_n$) et circonscrits ($b_n$) au cercle unité :
$$n \sin\left(\frac{180^\circ}{n}\right) < \pi < n \tan\left(\frac{180^\circ}{n}\right)$$

---

## 🚀 Installation et Utilisation

### Prérequis
- **Python 3.10+** (aucune bibliothèque externe n'est requise, uniquement la bibliothèque standard Python : `random`, `math`, `datetime`).

### Lancer les scripts

Vous pouvez exécuter chaque script indépendamment depuis votre terminal :

```bash
# Tester le générateur aléatoire et les métriques statistiques
python generateur_aleatoire.py

# Tester la démonstration du générateur LCG
python generateur_congruentiel_lineaire.py

# Lancer la simulation des 3 dés (Duc de Toscane)
python hasard_de.py

# Lancer le calcul d'approximation de Pi
python maths.py

# Lancer le test d'équiprobabilité
python essai_aleatoire.py
```

---

## 📐 Notions Mathématiques et Algorithmiques

- **Arithmétique Modulaire** : Réductions modulo $2^m$ utilisées dans les LCG.
- **Loi des Grands Nombres** : Convergence des fréquences observées vers la probabilité théorique au fur et à mesure que le nombre de tirages $n$ augmente.
- **Analyse d'Équirépartition** : Découpage de l'intervalle de valeurs en quantiles pour évaluer la qualité d'un générateur pseudo-aléatoire.
- **Suite de Polygones & Limite** : Encadrement d'une constante géométrique ($\pi$) par encadrement de sommes trigonométriques.
