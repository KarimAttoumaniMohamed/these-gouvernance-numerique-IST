# Gouvernance systémique du numérique : modélisation I–S–T

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20242474.svg)](https://doi.org/10.5281/zenodo.20242474)

> **Dépôt de code associé à la thèse de doctorat :**
>
> *Gouvernance du numérique à l'ère de l'IA : modélisation systémique
> de l'inclusion, de la soutenabilité et de la confiance*
>
> **Karim Attoumani Mohamed** & **Jérôme Velo**
> Université de Toamasina — Faculté des Sciences et Technologies
> Thèse de doctorat en Informatique (Génie informatique)
> ÉAD MIASE — École doctorale SCSD, 2026

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

Cette thèse est structurée comme une thèse sur articles. Deux contributions
publiées et un document de travail intégré à la thèse constituent les
piliers empiriques des variables I, S et T.

| Contribution | Statut | Variable | DOI |
|---|---|---|---|
| Karim & Velo (2025a) — *Towards Inclusive Internet Governance: A Multidimensional Analysis of Systemic Barriers and Reform Strategies* | **Publié** — IEEE ICECER 2025 | I | [10.1109/ICECER65523.2025.11401243](https://doi.org/10.1109/ICECER65523.2025.11401243) |
| Karim & Velo (2025b) — *Towards Sustainable Internet Governance: Energy and Bandwidth Challenges in the Era of AI* | **Publié** — IEEE ICECER 2025 | S | [10.1109/ICECER65523.2025.11401095](https://doi.org/10.1109/ICECER65523.2025.11401095) |
| Karim & Velo (2026) — *UAMINIFU: Modeling Digital Trust as a Systemic and Economic Variable for AI-Driven Digital Sovereignty* | **Document de travail** intégré à la thèse (chapitre 5), à soumettre | T | — |

---

## Contenu du dépôt

```
these-gouvernance-numerique-IST/
│
├── README.md                        ← Ce guide (installation, reproduction, périmètre)
├── LICENSE                          ← Licence MIT (code)
├── requirements.txt                 ← Dépendances Python
│
├── simulation/
│   ├── generate_figures.py          ← Modèle G(t), scénarios, figures 3.1, 3.2, 4.2, 6.2, 6.3
│   ├── energie.py                   ← Tableau 4.I et Figure 4.1 (demande liée à l'IA en 2030)
│   ├── dti.py                       ← DTI révisé, Tableau 5.IV, scénarios A et B, sensibilités
│   ├── figure_5_1_dti.py            ← Figure 5.1
│   ├── figure_6_1_diagramme_causal.py ← Figure 6.1
│   ├── figure_6_4_comores.py        ← Figure 6.4
│   ├── sensibilite_parametres.py    ← 42 simulations « un paramètre à la fois »
│   └── analyses_ch6.py              ← Monte-Carlo, variante couplée, leviers, valeurs initiales
│
├── resultats/                       ← Sorties numériques de référence des scripts
├── figures_these/                   ← Figures du manuscrit (numérotation de la thèse)
├── figures/                         ← Figures de la version 2.0 (historique)
│
└── data/
    └── README_donnees.md            ← Sources de données et hypothèses
```

### Correspondance entre figures du manuscrit et scripts

| Figure du manuscrit | Script | Fichier produit |
|---|---|---|
| 3.1 | `generate_figures.py` → `generate_figure_3_1` | `Figure_3_1_DSGM_reseau_participation` |
| 3.2 | `generate_figures.py` → `generate_figure_3_2` | `Figure_3_2_participation_scenarios` |
| 4.1 | `energie.py` | `Figure_4_1_demande_IA` |
| 4.2 | `generate_figures.py` → `generate_figure_4_2` | `Figure_4_2_lambda_orchestration` |
| 5.1 | `figure_5_1_dti.py` | `Figure_5_1_DTI` |
| 6.1 | `figure_6_1_diagramme_causal.py` | `Figure_6_1_diagramme_causal` |
| 6.2 | `generate_figures.py` → `generate_figure_6_1` (ancienne numérotation) | `Figure_6_1_quatre_scenarios` |
| 6.3 | `generate_figures.py` → `generate_figure_6_2` (ancienne numérotation) | `Figure_6_2_sensibilite_lambda` |
| 6.4 | `figure_6_4_comores.py` | `Figure_6_4_cas_Comores` |

Les fonctions `generate_figure_4_1`, `generate_figure_5_1` et `generate_figure_6_3` de `generate_figures.py` produisent les figures de la version 2.0 ; elles sont conservées pour l'historique et ne correspondent plus au manuscrit. Le dossier `figures_these/` contient les neuf figures sous la numérotation du manuscrit.

### Reproduire les résultats du manuscrit

```bash
pip install -r requirements.txt
cd simulation
python dti.py                       # chapitre 5 ; sortie de référence : resultats/dti.txt
python energie.py                   # chapitre 4 ; resultats/energie.txt
python sensibilite_parametres.py    # resultats/sensibilite_un_a_la_fois.txt
python analyses_ch6.py              # resultats/analyses_ch6.txt (graine 2026)
python figure_5_1_dti.py ; python figure_6_1_diagramme_causal.py ; python figure_6_4_comores.py
```

Paramètres : `ModelParameters` dans `generate_figures.py` (α = 0,35 ; β = 0,35 ; χ = 0,30 ; γ = 1,15 ; δ = 1,55 ; θ = 1,35 ; r₁ = 0,40 ; r₂ = 0,35 ; r₃ = 0,25 ; φ = 0,50 ; Rc = 0,62 ; κ = 7,0 ; coefficients des équations 6.1 à 6.3 : 0,08 ; −0,10 ; 0,05 ; −0,12 ; 0,06 ; 0,09 ; 0,07 ; −0,08 ; Sc = 0,40). Comores : I₀ = 0,33 ; S₀ = 0,40 ; T₀ = 0,45 ; X₀ = 0,80 ; A de 0,25 à 0,65 ; 25 périodes. DTI : facteurs et interactions des tableaux 5.I à 5.III, repris dans `dti.py`. Tirages aléatoires : graine 2026.

### Périmètre de reproductibilité

- **Reproductibles depuis ce dépôt** : toutes les simulations et tous les calculs des chapitres 4, 5 et 6 (Tableaux 4.I, 5.IV, 6.II ; analyses de robustesse ; Figures 4.1 à 6.4). Les sorties de référence figurent dans `resultats/`.
- **Partiellement reproductibles** : le chapitre 3. Les scripts régénèrent les visualisations et simulations du DSGM (Figures 3.1 et 3.2) à partir de poids et de paramètres renseignés dans le code. Ils ne refont ni l'extraction des données historiques IGF/IETF ni les calculs statistiques de l'article (R² = 0,82, intervalle de confiance) : ces valeurs sont reprises de Karim & Velo (2025a) et ne sont pas recalculées. Les jeux de données historiques ne sont pas inclus dans ce dépôt.
- **Non publiés** : les réponses individuelles aux deux questionnaires (n = 8 et n = 9), qui contiennent des données personnelles ; seuls des résultats agrégés figurent dans la thèse.

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
python simulation/generate_figures.py   # figures historiques v2.0 ; voir la correspondance ci-dessus
```

Les huit figures sont sauvegardées dans le répertoire courant, chacune en
PNG (300 dpi) et en SVG (vectoriel), sous les noms suivants (extension
`.png` et `.svg`) :

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

Les neuf figures du manuscrit sont dans `figures_these/`, par exemple :

![Figure 5.1](figures_these/Figure_5_1_DTI.png)

![Figure 6.4](figures_these/Figure_6_4_cas_Comores.png)

---

## Résultats clés

Les résultats ci-dessous sont ceux du manuscrit final de la thèse (2026).
Lorsqu'ils diffèrent de ceux des articles, l'écart est signalé ; voir aussi
la section [Écarts articles → thèse](#écarts-articles--thèse-version-20).

### Asymétries de participation (Figure 3.1 — Karim & Velo, 2025a)
- 92 % des positions de leadership à l'IETF sont détenues par le Nord global
- La proximité géographique des lieux de réunion explique 68 % de la variance
  de la participation (R² = 0,68, p < 0,01)
- Des réformes ciblées pourraient accroître la participation du Sud global
  de 120 à 150 % en cinq ans (modèle DSGM, R² = 0,82)

### Contraintes énergétiques (Figures 4.1 et 4.2 — Karim & Velo, 2025b)
- Une interaction IA consomme 145 à 250 fois plus d'énergie qu'un usage web
  selon les estimations publiées en 2023 et retenues par l'article ; environ
  12 à 15 fois selon les mesures publiées en 2025 (Epoch AI ; Google)
- En 2030, pour 600 millions d'utilisateurs, la demande liée à l'IA représente
  de 6,6 à 11,3 % de la production électrique africaine sous l'hypothèse haute
  (adoption totale, 100 requêtes par jour, 2,9 à 5 Wh par requête), mais moins
  de 1 % sous l'hypothèse basse (0,24 à 0,3 Wh par requête), quel que soit le
  profil d'usage (thèse, Tableau 4.I)
- Le coefficient d'orchestration λ rend visible une charge de calcul
  invisible ; l'article pose un seuil indicatif vers λ ≈ 40, qui n'est pas
  dérivé d'une mesure de capacité

### Dégradation de la confiance (Figure 5.1 — cadre UAMINIFU, chapitre 5)
- DTI révisé : calcul sur les moyennes des facteurs et décroissance vers le
  plancher −1 au-delà de Rc = 0,62 ; le DTI est borné dans [−1 ; 1] et
  décroît avec chaque facteur de risque
- Coût de transaction : Ctx = C₀ + ω/τ^η, avec τ = (1 + DTI)/2
- Comores (sources publiques et élicitation d'experts) : DTI = −0,908, zone
  d'effondrement au sens du modèle UAMINIFU ; −0,94 à −0,87 selon les
  variantes testées (thèse, § 5.6)

### Dynamique de gouvernance (Figures 6.1 à 6.4 — modèle G(t))
- L'amélioration isolée d'une variable ne garantit pas l'amélioration de G
- Les scénarios 1 et 2 se dégradent, les scénarios 3 et 4 progressent et
  restent les mieux classés dans 98 % de 2 000 tirages où les 21 paramètres
  varient simultanément de ±50 % (thèse, § 6.1.8)
- Région de viabilité (thèse, § 6.2.3) : avec investissements, A ≤ 0,5 et
  audit actif, aucun état de K = {I ≥ 0,4 ; S ≥ 0,45 ; T ≥ 0,5} n'en sort
- Cas des Comores (25 périodes) : G = −0,205 en statu quo contre G = 0,654
  sous gouvernance équilibrée ; même conclusion pour les 81 combinaisons de
  valeurs initiales testées

---

## Écarts articles → thèse (versions 2.0 et 3.0)

La version 3.0 (octobre 2026) accompagne la révision du manuscrit : DTI révisé (borné et monotone), projections énergétiques recalculées sans double projection pour l'année 2030, X₀ = 0,80 pour les Comores, analyses de robustesse et figures sous la numérotation de la thèse. Les calculs correspondants sont dans les scripts ajoutés listés plus haut.


La version 1.0 de ce dépôt (2025) reprenait les résultats des articles. La
version 2.0 (2026) aligne le dépôt sur le manuscrit final. **Aucun calcul
n'a été modifié** : les courbes sont identiques ; seuls des libellés,
annotations et commentaires ont changé.

Le tableau suivant décrit les écarts de la version 2.0 ; il emploie la numérotation des figures et des sections de cette version.

| Élément | Version 1.0 | Version 2.0 | Référence thèse |
|---|---|---|---|
| Figure 4.1 — seuil énergétique | Ligne « 15 % de la capacité africaine ≈ 131 GWh/j » et ligne « % capacité africaine » (53,6 %) calculées sur 874 GWh/j | Retirées : le dénominateur 874 n'était pas sourcé ; il correspond vraisemblablement à la demande électrique africaine de 2019 (874 TWh/an) lue comme des GWh/jour | § 4.3 |
| Figure 4.1 — E₀ | E₀ = 174 GWh/j présenté comme la consommation de 2024 | E₀ correspond à la demande de 600 M d'utilisateurs en 2030 ; le scénario B est une borne haute | § 4.3 |
| Figure 4.2 — λ_c | « Seuil critique λ_c = 40 », « capacité africaine systématiquement dépassée » | « Seuil indicatif λ ≈ 40 (hypothèse de l'article) » | § 4.3.4 |
| Figure 5.1 — coût de transaction | Ctx = C₀ + θ/T^η | Ctx = C₀ + ω/T^η (θ est réservé à l'exposant de T dans G(t)) | chap. 5 |
| Figure 5.1 — source | « Manuscrit soumis, CARI 2026 » | Cadre UAMINIFU, chapitre 5 (document de travail) | chap. 5 |
| Figure 5.1 — scénarios A et B | Points DTI = −1,06 et 3,59 placés sur le panneau C, hors de la courbe | Valeurs recalculées avec les exposants exacts et la décroissance sur R̄ = ΣRⱼ/6 (convention du § 5.6.4), soit −2,69 et 3,60, rappelées dans un encadré avec le DTI des Comores (−1,73) : elles ne relèvent pas de la coupe stylisée tracée | § 5.4.2 |
| Figure 6.1 — bande verte | « Zone de gouvernance stable » | « Bande indicative 0,3 < G < 0,7 » | § 6.4.1 |
| Figure 6.2 | Annotation « λ_c ≈ 40 (seuil critique africain) » ; seuil S_c tracé aussi sur le panneau G | Annotation retirée ; saturation A_t = 1 pour λ ≥ 34 indiquée ; S_c tracé sur le seul panneau S | § 6.4.2 |
| Figure 6.3 | Ligne « S₀ initial » tracée à 0,33 (valeur de I₀) | Ligne retirée | § 6.5 |
| Formats | PNG 300 dpi | PNG 300 dpi et SVG vectoriel | Annexe A |

---

## Reproductibilité et principes FAIR

Ce dépôt adhère aux principes FAIR (Wilkinson et al., 2016) :

- **Findability** — dépôt indexé sur GitHub avec DOI Zenodo permanent
- **Accessibility** — code et figures librement accessibles sous licence MIT
- **Interoperability** — formats standards : Python 3.9+, PNG 300 dpi,
  SVG, Markdown
- **Reusability** — documentation complète, paramètres détaillés,
  licence explicite, extension facilitée à d'autres contextes

**Référence FAIR :**
Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific
data management and stewardship. *Scientific Data, 3*, 160018.
https://doi.org/10.1038/sdata.2016.18

---

## Citation

**Archivage Zenodo**

| Version | DOI |
|---|---|
| Toutes versions (DOI de concept, renvoie à la dernière version) | [10.5281/zenodo.20242474](https://doi.org/10.5281/zenodo.20242474) |
| v3.0 — version révisée de la thèse (octobre 2026) | DOI attribué à la publication de la version |
| v2.0 — version de la thèse (2026) | [10.5281/zenodo.23063106](https://doi.org/10.5281/zenodo.23063106) |
| v1.0 — état des articles publiés (2025) | [10.5281/zenodo.20242475](https://doi.org/10.5281/zenodo.20242475) |

Si vous utilisez ce code ou ces résultats dans vos travaux, merci de citer :

```bibtex
@phdthesis{karim2026these,
  author  = {Karim Attoumani Mohamed},
  title   = {Gouvernance du num{\'e}rique {\`a} l'{\`e}re de l'{IA} :
             mod{\'e}lisation syst{\'e}mique de l'inclusion, de la
             soutenabilit{\'e} et de la confiance},
  school  = {Universit{\'e} de Toamasina},
  year    = {2026},
  type    = {Th{\`e}se de doctorat en Informatique
             (G{\'e}nie informatique)},
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

@software{karim2026code,
  author    = {Karim Attoumani Mohamed and Jérôme Velo},
  title     = {these-gouvernance-numerique-IST : code source et figures
               de la th{\`e}se (version 2.0)},
  year      = {2026},
  publisher = {Zenodo},
  version   = {v2.0},
  doi       = {10.5281/zenodo.23063106}
}

@unpublished{karim2026uaminifu,
  author = {Karim, A. M. and Velo, J.},
  title  = {UAMINIFU: Modeling Digital Trust as a Systemic and Economic
            Variable for AI-Driven Digital Sovereignty},
  note   = {Document de travail int{\'e}gr{\'e} {\`a} la th{\`e}se,
            Universit{\'e} de Toamasina},
  year   = {2026}
}
```

---

## Licence

Le code de ce dépôt est distribué sous licence **MIT**.
Vous êtes libre de l'utiliser, le modifier et le redistribuer sous
condition de mention des auteurs originaux. Les textes et figures repris des
articles publiés par l'IEEE (Karim & Velo, 2025a, 2025b) restent soumis aux
conditions de réutilisation de l'IEEE et ne sont pas couverts par cette licence.

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

*Dépôt créé en 2025 — Version 3.0 (octobre 2026), alignée sur le manuscrit révisé de la thèse*
