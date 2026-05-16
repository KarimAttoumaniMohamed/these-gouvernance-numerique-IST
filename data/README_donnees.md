# Sources de données — Thèse I–S–T

> Karim Attoumani Mohamed & Jérôme Velo
> Université de Toamasina, 2025
> Dépôt : https://github.com/karimattoumanimohamed/these-gouvernance-numerique-IST

Ce document décrit l'ensemble des sources de données mobilisées dans la thèse
et utilisées pour produire les figures, les simulations et les estimations
analytiques. Il précise pour chaque source les conditions d'accès, le
traitement appliqué et les figures concernées.

---

## 1. Données IGF (2006–2025)

**Description**
Données longitudinales de participation aux Forums sur la gouvernance de
l'Internet couvrant 19 éditions (Athènes 2006 — Kyoto 2025). Incluent la
distribution géographique des participants, la représentation régionale dans
les sessions, les données de financement des bourses de voyage et la
répartition linguistique des documents préparatoires.

**Source**
Secrétariat de l'IGF, Nations Unies.
https://www.intgovforum.org/

**Référence bibliographique**
IGF Secretariat. (2025). *IGF Secretariat Data (2006–2025)*.
Unpublished dataset.

**Conditions d'accès**
Les données agrégées de participation sont publiquement accessibles sur le
portail officiel de l'IGF. Les données détaillées ont été obtenues dans le
cadre de la recherche académique auprès du Secrétariat de l'IGF. Ces données
ne peuvent pas être redistribuées sans autorisation préalable.

**Traitement appliqué**
- Nettoyage des données manquantes par interpolation linéaire (années 2008
  et 2012 — données partielles)
- Normalisation des catégories régionales selon la classification ONU
- Construction des indicateurs de représentation par calcul des ratios de
  participation relative rapportés à la part de la population mondiale et
  de la base d'utilisateurs Internet de chaque région

**Figures concernées**
3.1, 3.2

---

## 2. Données IETF Datatracker

**Description**
Statistiques de participation et de contribution à l'Internet Engineering
Task Force. Incluent les données d'auteurs de RFC et d'Internet-Drafts par
institution et par pays, la distribution géographique des présidents de
groupes de travail, les statistiques de participation aux réunions IETF et
les métriques de contributions par région.

**Source**
IETF Datatracker — accès public via interface web et API REST.
https://datatracker.ietf.org/

**Référence bibliographique**
Internet Engineering Task Force. (2025). *Datatracker*.
https://datatracker.ietf.org/

Arkko, J. (2024). *Distribution of number of RFCs per continent*.
Internet Research Task Force.
https://irtf.org/rfc-distribution

**Conditions d'accès**
Entièrement public. Aucune restriction d'utilisation pour la recherche
académique. API REST officielle disponible sans authentification.

**Traitement appliqué**
- Extraction des métadonnées d'auteurs pour l'ensemble des RFC publiées
  (RFC 1 à RFC 9700+, période 1969–2025)
- Attribution géographique des institutions par correspondance avec les
  bases de données institutionnelles publiques
- Calcul des coefficients de Gini pour la concentration géographique des
  réunions et des auteurs (Gini = 0,72 pour les lieux de réunion)
- Analyse de variance (ANOVA) pour identifier les facteurs explicatifs de
  la participation régionale (R² = 0,68, p < 0,01)

**Figures concernées**
3.1, 3.2

---

## 3. Données énergétiques et infrastructurelles (Chapitre 4)

**Description**
Données de consommation énergétique des systèmes d'IA et des infrastructures
numériques, benchmarks d'empreinte carbone des grands modèles de langage,
statistiques d'infrastructure numérique africaine.

**Sources multiples**

| Source | Données | URL |
|--------|----------|-----|
| The Shift Project (2019) | Empreinte numérique mondiale | https://theshiftproject.org |
| Patterson et al. (2021) | Émissions carbone entraînement LLM | https://arxiv.org/abs/2104.10350 |
| IEA (2022) | Consommation data centers mondiale | https://www.iea.org |
| IEA (2025) | Énergie et IA | https://www.iea.org/reports/energy-and-ai |
| OpenAI (2024) | Impact environnemental modèles IA | https://openai.com/research |
| Hugging Face (2024) | Benchmarks énergétiques inférence | https://huggingface.co/blog |
| HTTP Archive (2023) | Consommation web standard | https://httparchive.org |
| Reuters/IFC (2025) | Capacité data centers africaine | Public |
| GSMA (2024) | Connectivité mobile africaine | https://www.gsma.com |

**Traitement appliqué**
- Consolidation des données multi-sources par pondération selon la qualité
  méthodologique des études sources
- Application d'un facteur correctif de 30% pour les spécificités des
  infrastructures africaines (pertes réseau, coupures d'électricité,
  surcoût cloud offshore) calibré à partir des données GSMA et IEA
- Modélisation prospective par extrapolation exponentielle :
  E(t) = E₀·e^(αt) avec α ∈ [0,15 — 0,18] selon les scénarios
- Paramètre initial : E₀ = 174 GWh/jour (Afrique, 2024)

**Figures concernées**
4.1, 4.2

---

## 4. Données de simulation UAMINIFU (Chapitre 5)

**Description**
Les données du cadre UAMINIFU sont issues d'une simulation sur scénarios
stylisés et non d'une collecte empirique directe. Les paramètres sont calibrés
sur des hypothèses plausibles fondées sur la littérature existante.

**Paramètres de calibration**

| Paramètre | Valeur | Justification |
|-----------|--------|---------------|
| γ (amplification confiance) | 1,15 | Non-linéarité modérée — littérature sur systèmes sociotechniques |
| δ (amplification risque) | 1,55 | Non-linéarité forte — Helbing (2013), Taleb (2007) |
| κ (vitesse décroissance) | 7,0 | Décroissance rapide post-seuil — GSMA (2023) |
| Rc (seuil critique) | 0,62 | Seuil de basculement — calibration stylisée |

**Scénarios de simulation**
- Scénario A (risque élevé) : ΣSᵢ = 2,2 — ΣRⱼ = 2,7
- Scénario B (mature) : ΣSᵢ = 3,5 — ΣRⱼ = 0,7

**Limite importante**
Ces données sont simulées et non empiriques. Une calibration sur données
réelles (incidents de fraude, temps d'arrêt, indicateurs de conformité des
opérateurs de monnaie mobile africains) constitue une perspective de
recherche future explicitement identifiée dans la thèse (section 6.6.4).

**Références**
- Karim, A. M., & Velo, J. (soumis). UAMINIFU: Modeling Digital Trust.
  CARI 2026.
- GSMA. (2023). State of the Industry Report on Mobile Money.
- Helbing, D. (2013). Globally networked risks. Nature, 497, 51–59.
- Williamson, O. E. (1985). The Economic Institutions of Capitalism.

**Figures concernées**
5.1

---

## 5. Données du cas des Comores (Chapitre 6)

**Description**
Données contextuelles sur le système numérique comorien mobilisées pour
l'étude de cas de la section 6.4. Toutes issues de sources publiques ou de
rapports institutionnels librement accessibles.

**Sources**

| Source | Données mobilisées |
|--------|-------------------|
| ITU (2024) | Taux de pénétration Internet, infrastructure télécoms |
| World Bank (2024) | Indicateurs de développement numérique |
| Smart Africa Alliance (2024) | Stratégies numériques africaines |
| GSMA (2023) | Données monnaie mobile Afrique subsaharienne |
| UNCTAD (2021) | Économie numérique pays en développement |
| FPF (2025) | Flux de données transfrontaliers en Afrique |

**Estimations analytiques utilisées**

| Variable | Valeur estimée | Source principale |
|----------|---------------|-------------------|
| I₀ (inclusion initiale) | 0,33 | ITU (2024) — taux pénétration Internet |
| S₀ (soutenabilité initiale) | 0,40 | IEA + données énergie Comores |
| T₀ (confiance initiale) | 0,45 | GSMA (2023) — adoption monnaie mobile |
| X_t (dépendance externe) | 0,78 | FPF (2025) — 85% données hors continent |

**Limite importante**
Ces valeurs sont des estimations analytiques fondées sur des données
secondaires et non des mesures empiriques directes calibrées sur le terrain.
Elles constituent des approximations à valeur illustrative. Une collecte de
données primaires sur le terrain aux Comores constitue une perspective de
recherche future prioritaire (section 6.6.4 de la thèse).

**Figures concernées**
6.3

---

## 6. Données de simulation du modèle G(t) (Chapitre 6)

**Description**
Les données des Figures 6.1 et 6.2 sont entièrement simulées à partir du
modèle dynamique G(t) formalisé au chapitre 2 de la thèse. Aucune donnée
empirique externe n'est mobilisée pour ces figures.

**Paramètres du modèle G(t)**

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

**Reproductibilité complète**
L'ensemble des figures 6.1, 6.2 et 6.3 peut être reproduit intégralement
en exécutant le code disponible dans ce dépôt :

```bash
python simulation/generate_figures.py
```

**Figures concernées**
6.1, 6.2, 6.3

---

## Principes FAIR

Ce dépôt adhère aux principes FAIR de gestion des données scientifiques
(Wilkinson et al., 2016) :

- **Findability** — dépôt indexé sur GitHub avec DOI Zenodo permanent
- **Accessibility** — code et figures librement accessibles sous licence MIT
- **Interoperability** — formats standards : Python, PNG, Markdown
- **Reusability** — documentation complète, licence explicite, paramètres
  détaillés permettant la reproduction et l'extension du modèle

**Référence**
Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific
data management and stewardship. *Scientific Data, 3*, 160018.
https://doi.org/10.1038/sdata.2016.18

---

*Dernière mise à jour : 2025 — Version 1.0*
