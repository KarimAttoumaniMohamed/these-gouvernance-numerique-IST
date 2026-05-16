# Gouvernance systémique du numérique : modélisation I–S–T

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20242475.svg)](https://doi.org/10.5281/zenodo.20242475)

> **Dépôt de code associé à la thèse de doctorat :**
>
> *Vers une gouvernance inclusive, durable et fiable du numérique :
> modélisation systémique de l'inclusion, de la soutenabilité et de la
> confiance à l'ère de l'intelligence artificielle*
>
> **Karim Attoumani Mohamed** & **Jérôme Velo**
> Université de Toamasina — Faculté des Sciences et Technologies
> Doctorat en Mathématiques, Informatique et Applications, 2025

---

## À propos de cette recherche

Cette thèse propose un cadre systémique intégré de gouvernance du numérique
articulant trois variables structurantes interdépendantes :

- **I — Inclusion** : capacité des acteurs à participer effectivement aux
  espaces de gouvernance et aux bénéfices du numérique
- **S — Soutenabilité** : capacité des infrastructures numériques à fonctionner
  durablement sous contraintes énergétiques, computationnelles et environnementales
- **T — Confiance** : condition de légitimité et de stabilité des interactions
  numériques

Ces trois variables sont formalisées dans un modèle dynamique de gouvernance G(t) :

```
G_t = α·I_t^γ + β·S_t^δ + χ·T_t^θ − φ·R_t

R_t = r₁·A_t·I_t·(1−S_t) + r₂·(1−T_t)·X_t + r₃·A_t·X_t
```

où R_t est le risque systémique, A_t l'intensité des usages IA et X_t
la dépendance externe du système.

**Paramètres calibrés :**

| Paramètre | Valeur | Description |
|-----------|--------|-------------|
| α | 0,35 | Poids de l'inclusion I |
| β | 0,35 | Poids de la soutenabilité S |
| χ | 0,30 | Poids de la confiance T |
| γ | 1,15 | Exposant non-linéarité I |
| δ | 1,55 | Exposant non-linéarité S |
| θ | 1,35 | Exposant non-linéarité T |
| φ | 0,50 | Sensibilité au risque systémique |
| Rc | 0,62 | Seuil critique de dégradation de T |
| κ | 7,0 | Vitesse de décroissance exponentielle de T |

---

## Publications associées

Cette thèse est structurée comme une thèse sur articles. Les trois
contributions publiées ou soumises constituent les piliers empiriques
des variables I, S et T.

| Contribution | Statut | Variable | DOI |
|---|---|---|---|
| Karim & Velo (2025a) — *Towards Inclusive Internet Governance: A Multidimensional Analysis of Systemic Barriers and Reform Strategies* | **Publié** — IEEE ICECER 2025 | I | [10.1109/ICECER65523.2025.11401243](https://doi.org/10.1109/ICECER65523.2025.11401243) |
| Karim & Velo (2025b) — *Towards Sustainable Internet Governance: Energy and Bandwidth Challenges in the Era of AI* | **Publié** — IEEE ICECER 2025 | S | [10.1109/ICECER65523.2025.11401095](https://doi.org/10.1109/ICECER65523.2025.11401095) |
| Karim & Velo (soumis) — *UAMINIFU: Modeling Digital Trust as a Systemic and Economic Variable for AI-Driven Digital Sovereignty* | **Soumis** — CARI 2026 | T | — |

---

## Contenu du dépôt

```
these-gouvernance-numerique-IST/
│
├── README.md                        ← Ce fichier
├── LICENSE                          ← MIT License
├── requirements.txt                 ← Dépendances Python
│
├── simulation/
│   └── generate_figures.py          ← Code de génération des 8 figures
│
├── figures/
│   ├── Figure_3_1_DSGM_reseau_participation.png
│   ├── Figure_3_2_participation_scenarios.png
│   ├── Figure_4_1_energie_Afrique_2030.png
│   ├── Figure_4_2_lambda_orchestration.png
│   ├── Figure_5_1_UAMINIFU_trust_degradation.png
│   ├── Figure_6_1_quatre_scenarios.png
│   ├── Figure_6_2_sensibilite_lambda.png
│   └── Figure_6_3_cas_Comores.png
│
└── data/
    └── README_donnees.md            ← Description des sources de données
```

### Organisation du code (`generate_figures.py`)

| Section | Figure | Contenu |
|---------|--------|---------|
| 1 | — | Dépendances et configuration commune |
| 2 | **3.1** | Réseau d'influence pondéré DSGM et participation P_i(t) |
| 3 | **3.2** | Simulation participation sous trois scénarios d'inclusion |
| 4 | **4.1** | Projections énergétiques, bande passante et carbone — Afrique 2024-2030 |
| 5 | **4.2** | Effet du coefficient d'orchestration λ sur Q'(t) |
| 6 | **5.1** | Dégradation non linéaire de la confiance — cadre UAMINIFU |
| 7 | **6.1, 6.2, 6.3** | Modèle G(t) : quatre scénarios, sensibilité λ, cas des Comores |

---

## Installation

### Prérequis

- Python 3.9 ou supérieur
- pip

### Cloner le dépôt

```bash
git clone https://github.com/karimattoumanimohamed/these-gouvernance-numerique-IST
cd these-gouvernance-numerique-IST
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Utilisation

### Générer toutes les figures

```bash
python simulation/generate_figures.py
```

Les huit figures sont sauvegardées en résolution 300 dpi dans le
répertoire courant sous les noms :

```
Figure_3_1_DSGM_reseau_participation.png
Figure_3_2_participation_scenarios.png
Figure_4_1_energie_Afrique_2030.png
Figure_4_2_lambda_orchestration.png
Figure_5_1_UAMINIFU_trust_degradation.png
Figure_6_1_quatre_scenarios.png
Figure_6_2_sensibilite_lambda.png
Figure_6_3_cas_Comores.png
```

### Modifier les paramètres du modèle

Les paramètres du modèle G(t) sont centralisés dans la classe
`ModelParameters` (Section 7 du code). Pour explorer d'autres
configurations :

```python
from simulation.generate_figures import ModelParameters, run_simulation_G

# Modifier les paramètres
params = ModelParameters(
    gamma=1.20,   # Augmenter la non-linéarité de I
    delta=1.60,   # Augmenter la non-linéarité de S
    Rc=0.55       # Abaisser le seuil critique de T
)

# Lancer une simulation personnalisée
# (voir Section 7 pour la définition de ScenarioConfig)
```

### Appliquer le modèle à un nouveau contexte

Pour adapter le modèle à un autre pays ou contexte du Sud global,
modifiez les conditions initiales dans la fonction `generate_figure_6_3()` :

```python
# Exemple : adapter au contexte du Vanuatu
sc_custom = ScenarioConfig(
    name  = "Vanuatu — Statu quo",
    I0    = 0.28,   # Taux de pénétration Internet
    S0    = 0.38,   # Capacité infrastructurelle
    T0    = 0.42,   # Niveau de confiance numérique estimé
    ...
)
```

---

## Figures produites

### Figure 3.1 — Réseau DSGM et participation
![Figure 3.1](figures/Figure_3_1_DSGM_reseau_participation.png)

### Figure 5.1 — Dégradation non linéaire UAMINIFU
![Figure 5.1](figures/Figure_5_1_UAMINIFU_trust_degradation.png)

### Figure 6.1 — Quatre scénarios de gouvernance G(t)
![Figure 6.1](figures/Figure_6_1_quatre_scenarios.png)

### Figure 6.3 — Application au cas des Comores
![Figure 6.3](figures/Figure_6_3_cas_Comores.png)

---

## Résultats clés

### Asymétries de participation (Figure 3.1 — Karim & Velo, 2025a)
- 92% des positions de leadership IETF concentrées dans le Nord global
- 68% de la variance de participation expliquée par la concentration
  géographique (R² = 0,68, p < 0,01)
- Des réformes ciblées pourraient augmenter la participation du Sud global
  de 120 à 150% sur cinq ans (R² = 0,82)

### Contraintes énergétiques africaines (Figure 4.1 — Karim & Velo, 2025b)
- Les interactions IA consomment 145 à 250 fois plus d'énergie que le web
- Sans optimisation, l'IA représenterait 53,6% de la capacité électrique
  africaine installée d'ici 2030
- Le coefficient d'orchestration λ_c ≈ 40 constitue le seuil critique
  pour les contextes africains

### Dégradation de la confiance (Figure 5.1 — UAMINIFU)
- Au-delà du seuil Rc = 0,62, la dégradation de T s'accélère
  exponentiellement selon T' = T·e^(−κ·(R−Rc)₊)
- Le modèle linéaire sous-estime massivement la vitesse de dégradation
- La confiance a des implications économiques directes : Ctx = C₀ + θ/T^η

### Gouvernance équilibrée (Figure 6.1 — Modèle G(t))
- L'amélioration isolée d'une variable ne garantit pas l'amélioration de G
- Le scénario de gouvernance équilibrée est le seul à produire une
  trajectoire ascendante soutenue
- Trois boucles de rétroaction critiques identifiées :
  I→S→T, T→I→S, X_t→R→T

---

## Reproductibilité et principes FAIR

Ce dépôt adhère aux principes FAIR (Wilkinson et al., 2016) :

- **Findability** — dépôt indexé sur GitHub avec DOI Zenodo permanent
- **Accessibility** — code et figures librement accessibles sous licence MIT
- **Interoperability** — formats standards : Python 3.9+, PNG 300 dpi,
  Markdown
- **Reusability** — documentation complète, paramètres détaillés,
  licence explicite, extension facilitée à d'autres contextes

**Référence FAIR :**
Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific
data management and stewardship. *Scientific Data, 3*, 160018.
https://doi.org/10.1038/sdata.2016.18

---

## Citation

Si vous utilisez ce code ou ces résultats dans vos travaux, merci de citer :

```bibtex
@phdthesis{karim2025these,
  author  = {Karim Attoumani Mohamed},
  title   = {Vers une gouvernance inclusive, durable et fiable du
             num{\'e}rique : mod{\'e}lisation syst{\'e}mique de
             l'inclusion, de la soutenabilit{\'e} et de la confiance
             {\`a} l'{\`e}re de l'intelligence artificielle},
  school  = {Universit{\'e} de Toamasina},
  year    = {2025},
  type    = {Th{\`e}se de doctorat en Math{\'e}matiques,
             Informatique et Applications},
  url     = {https://github.com/karimattoumanimohamed/
             these-gouvernance-numerique-IST}
}

@inproceedings{karim2025a,
  author    = {Karim, A. M. and Velo, J.},
  title     = {Towards Inclusive Internet Governance: A Multidimensional
               Analysis of Systemic Barriers and Reform Strategies},
  booktitle = {Proceedings of ICECER 2025},
  year      = {2025},
  doi       = {10.1109/ICECER65523.2025.11401243}
}

@inproceedings{karim2025b,
  author    = {Karim, A. M. and Velo, J.},
  title     = {Towards Sustainable Internet Governance: Energy and
               Bandwidth Challenges in the Era of AI},
  booktitle = {Proceedings of ICECER 2025},
  year      = {2025},
  doi       = {10.1109/ICECER65523.2025.11401095}
}
```

---

## Licence

Ce dépôt est distribué sous licence **MIT**.
Vous êtes libre de l'utiliser, le modifier et le redistribuer sous
condition de mention des auteurs originaux.

Voir le fichier [LICENSE](LICENSE) pour les termes complets.

---

## Contact

**Karim Attoumani Mohamed**
Université de Toamasina — Faculté des Sciences et Technologies
attoukarim@gmail.com

**Jérôme Velo** (directeur de thèse)
Université de Toamasina — Faculté des Sciences et Technologies
zjvelo@gmail.com

---

*Dépôt créé en 2025 — Version 1.0*
