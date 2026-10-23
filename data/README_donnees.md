# Sources de données — Thèse I–S–T

> Karim Attoumani Mohamed & Jérôme Velo
> Université de Toamasina, 2026
> Dépôt : https://github.com/karimattoumanimohamed/these-gouvernance-numerique-IST

Ce document décrit l'ensemble des sources de données mobilisées dans la thèse
et utilisées pour produire les figures, les simulations et les estimations
analytiques. Il précise pour chaque source les conditions d'accès, le
traitement appliqué et les figures concernées.

---

## 1. Données IGF (2006–2025)

**Description**
Données longitudinales de participation aux Forums sur la gouvernance de
l'Internet couvrant 20 éditions (d'Athènes en 2006 à Lillestrøm en 2025). Incluent la
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
| de Vries (2023) | Empreinte énergétique de l'IA | https://doi.org/10.1016/j.joule.2023.09.004 |
| You (2025) — Epoch AI | Énergie par requête (≈ 0,3 Wh, GPT-4o) | https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use |
| Elsworth et al. (2025) — Google | Énergie, eau et CO₂e par requête (mesures en production) | https://arxiv.org/abs/2508.15734 |
| Ember (2026) | Production électrique africaine (965 TWh en 2024) | https://ember-energy.org/data/yearly-electricity-data/ |

*Les lignes OpenAI (2024), Hugging Face (2024), HTTP Archive (2023) et
Reuters/IFC (2025) sont les sources de l'article (Karim & Velo, 2025b,
références [8] à [10] et [16]) ; elles ne sont pas reprises dans la
bibliographie de la thèse, qui s'appuie sur les mesures plus récentes
listées à la suite (thèse, § 4.2).*

**Traitement appliqué**
- Consolidation des valeurs issues des publications citées par l'article,
  complétées par les simulations des auteurs
- Application d'un facteur correctif forfaitaire de 30 % pour les
  spécificités des infrastructures africaines (pertes réseau, coupures
  d'électricité, surcoût du cloud hébergé à l'étranger) ; ce facteur est une
  hypothèse de l'article et n'a pas fait l'objet d'une calibration documentée
- Projections de la thèse révisée (script `simulation/energie.py`) : demande
  en 2030 = 600 millions d'utilisateurs × taux d'adoption × requêtes par jour ×
  consommation par requête, sous deux hypothèses : haute (2,9 à 5 Wh par
  requête, estimations publiées en 2023 et retenues par l'article) et basse
  (0,24 à 0,3 Wh, mesures publiées en 2025). La version 2.0 appliquait une
  croissance annuelle à une valeur initiale de 174 GWh/jour qui correspondait
  déjà à 2030 (double projection) ; ce calcul n'est plus utilisé
- Repère de comparaison : production électrique africaine de 965 TWh en
  2024, soit environ 2 640 GWh/jour (Ember, 2026)

**Figures concernées**
4.1, 4.2

---

## 4. Données de simulation UAMINIFU (Chapitre 5)

**Description**
Les courbes de la Figure 5.1 sont issues d'une simulation sur scénarios
stylisés et non d'une collecte empirique directe. Les paramètres sont fixés
par hypothèse, à partir de la littérature existante, et non estimés sur données. Le cadre
UAMINIFU est développé au chapitre 5 de la thèse (document de travail, à
soumettre).

**Paramètres retenus**

| Paramètre | Valeur | Justification |
|-----------|--------|---------------|
| γ (amplification confiance) | 1,15 | Non-linéarité modérée — littérature sur systèmes sociotechniques |
| δ (amplification risque) | 1,55 | Non-linéarité forte — Helbing (2013), Taleb (2007) |
| κ (vitesse décroissance) | 7,0 | Décroissance rapide post-seuil — GSMA (2023) |
| Rc (seuil critique) | 0,62 | Seuil de basculement — valeur stylisée |

**Formulation révisée (thèse, § 5.2 et 5.3)**
Le DTI est calculé sur les moyennes des facteurs (S̄ = ΣSᵢ/n, R̄ = ΣRⱼ/m), le terme
de risque est (R̄^δ + Σλⱼₖ·Rⱼ·Rₖ)/(1 + Σλⱼₖ), et la décroissance tire le score vers le
plancher −1 : DTI = −1 + (1 + T)·e^(−κ(R̄ − Rc)⁺). Le DTI est ainsi borné dans [−1 ; 1]
et décroissant en chaque facteur de risque (script `simulation/dti.py`).

**Scénarios de simulation**
- Scénario A (risque élevé) : Sᵢ = 0,50 ; 0,75 ; 0,25 ; 0,50 ; 0,25 (S̄ = 0,45) — Rⱼ = 0,75 ; 0,75 ; 0,50 ; 0,75 ; 0,50 ; 1,00 (R̄ = 0,708) — DTI = −0,536
- Scénario B (mature) : Sᵢ = 0,75 ; 0,75 ; 0,50 ; 0,75 ; 0,75 (S̄ = 0,70) — Rⱼ = 0,25 ; 0 ; 0,25 ; 0 ; 0,25 ; 0 (R̄ = 0,125) — DTI = 0,630
- Interactions : mêmes paires et coefficients que pour les Comores (tableau 5.III, Σλ = 0,75)

**Instanciation sur sources publiques (thèse, § 5.6)**
Le DTI est par ailleurs instancié pour l'Union des Comores à partir de sources
exclusivement publiques : GSMA Intelligence, *Digital Africa Index* (données
2024-2025, période 2025 retenue) pour les variables S2 à S5 et R2 à R5 ;
ITU, *Global Cybersecurity Index 2024* pour S1 ; loi du 26 juin 2014 portant
protection des données à caractère personnel pour R1. Un questionnaire
d'élicitation d'experts (n = 8) complète ces sources. Aucune donnée interne
d'opérateur n'est mobilisée. Résultat : S̄ = 0,467, R̄ = 0,889,
DTI = −0,908 (zone d'effondrement), résultat robuste à l'analyse de
sensibilité (−0,94 à −0,87). Ce point figure dans le panneau (a) de la Figure 5.1.

**Limite importante**
Les courbes de la Figure 5.1 sont calculées et non empiriques. Une calibration
sur séries temporelles réelles (incidents de fraude, temps d'arrêt,
indicateurs de conformité publiés) constitue une perspective de recherche
identifiée dans la thèse (Conclusion générale, perspectives de recherche).

**Références**
- Karim, A. M., & Velo, J. (2026). UAMINIFU: Modeling digital trust as a
  systemic and economic variable for AI-driven digital sovereignty. Document
  de travail intégré à la thèse, Université de Toamasina. À soumettre.
- GSMA Intelligence. (2025). Digital Africa Index : données 2024-2025.
- International Telecommunication Union. (2024). Global Cybersecurity Index 2024.
- GSMA. (2023). State of the Industry Report on Mobile Money.
- Helbing, D. (2013). Globally networked risks. Nature, 497, 51–59.
- Williamson, O. E. (1985). The Economic Institutions of Capitalism.

**Figures concernées**
5.1

---

## 5. Données du cas des Comores (Chapitre 6)

**Description**
Données contextuelles sur le système numérique comorien mobilisées pour
l'étude de cas de la section 6.3 de la thèse. Toutes issues de sources
publiques ou de rapports institutionnels librement accessibles. La seule
collecte primaire consiste en questionnaires d'élicitation d'experts
(section 6.3.6 : acteurs comoriens, n = 8, et praticiens réunis
à l'ICANN86, n = 9) ; les réponses individuelles ne sont pas publiées dans ce
dépôt.

**Sources**

| Source | Données mobilisées |
|--------|-------------------|
| ITU (2024) | Taux de pénétration Internet, infrastructure télécoms |
| World Bank (2024) | Indicateurs de développement numérique |
| Smart Africa Alliance (2024) | Stratégies numériques africaines |
| GSMA (2023) | Données monnaie mobile Afrique subsaharienne |
| UNCTAD (2021) | Économie numérique pays en développement |
| IFC et GSMA (TechAfrica News, 2026) | Part des données africaines hébergées hors du continent (X₀) |
| GSMA Intelligence (2025) | Digital Africa Index (variables S2–S5, R2–R5 du DTI) |
| ITU (2024) — GCI 2024 | Indice de cybersécurité (variable S1 du DTI) |
| Union des Comores (2014) | Loi sur la protection des données (variable R1 du DTI) |

**Estimations analytiques utilisées**

| Variable | Valeur estimée | Source principale |
|----------|---------------|-------------------|
| I₀ (inclusion initiale) | 0,33 | UIT/Banque mondiale (2024) — 32,5 % de la population utilise Internet (arrondi) |
| S₀ (soutenabilité initiale) | 0,40 | IEA + données énergie Comores |
| T₀ (confiance initiale) | 0,45 | GSMA (2023) — adoption monnaie mobile |
| X₀ (dépendance externe) | 0,80 | Borne basse des estimations de la part des données africaines hébergées hors du continent (plus de 80 % selon IFC et GSMA ; 85 % selon Karim & Velo, 2025b) |

**Limite importante**
Ces valeurs sont des estimations analytiques fondées sur des données
secondaires et non des mesures empiriques directes calibrées sur le terrain.
Elles constituent des approximations à valeur illustrative ; les
questionnaires de la section 6.3.6 en proposent une première confrontation.
Une collecte de données primaires plus large aux Comores constitue l'Axe 1
des perspectives de recherche (Conclusion générale, section 3).

**Figures concernées**
6.4

---

## 6. Données de simulation du modèle G(t) (Chapitre 6)

**Description**
Les données des Figures 6.2 et 6.3 sont entièrement simulées à partir du
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

**Note sur la Figure 6.3**
L'intensité d'usage y est définie par A_t = min(1 ; 0,3·λ/10) : elle sature
dès λ ≈ 34, de sorte que les trajectoires λ = 40 à 100 sont identiques. La
simulation ne permet donc pas d'établir de façon indépendante le seuil
indicatif λ ≈ 40 du chapitre 4 (thèse, § 6.2.2).

**Reproductibilité complète**
L'ensemble des figures 6.1 à 6.4 peut être reproduit avec les scripts
du dossier `simulation/` (correspondance dans le README principal) :

```bash
cd simulation
python figure_6_1_diagramme_causal.py ; python figure_6_2_6_3.py ; python figure_6_4_comores.py
```

**Figures concernées**
6.1, 6.2, 6.3, 6.4

---

## 7. Sessions de l'ICANN86 Policy Forum (Chapitre 6, Annexe C)

**Description**
Comptages I, S et T des 25 sessions enregistrées de l'ICANN86 Policy Forum
(Séville, 8-11 juin 2026) : 5 sessions de la ccNSO, 8 d'At-Large et 12 du GAC.
Fichier : `data/icann86_sessions.csv` (une ligne par session : identifiant de
l'enregistrement Zoom, communauté, date et heure de début en UTC, intitulé,
comptages selon les deux règles).

**Source**
Transcriptions automatiques (VTT) des enregistrements Zoom publiés par l'ICANN
pour chaque session : https://icann86.sched.com/list/simple

**Conditions d'accès**
Les enregistrements et transcriptions sont publics sur le site de l'ICANN. Ils
ne sont pas redistribués dans ce dépôt ; les fils de discussion (chat), qui
contiennent des échanges entre participants nommés, ne sont pas utilisés.

**Traitement appliqué** (script `simulation/icann86_codage.py`)
- Un segment (ligne de sous-titre, sans le nom de l'orateur) est compté une
  fois pour une variable s'il contient au moins un mot-clé de cette variable
  (dictionnaire de l'Annexe C)
- Règle « sous-chaine » (comptages de la thèse) : recherche de la chaîne,
  insensible à la casse ; elle retient aussi des mots qui contiennent un
  mot-clé (« observer » pour « server »)
- Règle « mot » (variante de contrôle) : mots entiers, pluriel accepté ; elle
  réduit S de 356 à 309 segments sans changer la variable dominante d'aucune
  communauté
- Les intitulés sont reconstitués à partir de l'annonce d'ouverture de chaque
  transcription (corrigée des erreurs de reconnaissance vocale)

**Figures et tableaux concernés**
Section 6.3.7 ; tableau de synthèse de l'Annexe C (sortie de référence :
`resultats/icann86_synthese.txt`)

---

## Principes FAIR

Ce dépôt adhère aux principes FAIR de gestion des données scientifiques
(Wilkinson et al., 2016) :

- **Findability** — dépôt indexé sur GitHub avec DOI Zenodo permanent
- **Accessibility** — code et figures librement accessibles sous licence MIT
- **Interoperability** — formats standards : Python, PNG, SVG, Markdown
- **Reusability** — documentation complète, licence explicite, paramètres
  détaillés permettant la reproduction et l'extension du modèle

**Référence**
Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific
data management and stewardship. *Scientific Data, 3*, 160018.
https://doi.org/10.1038/sdata.2016.18

---

*Dernière mise à jour : octobre 2026 — Version 3.1.0 (alignée sur le manuscrit révisé de la thèse). Version anglaise : [README_data_EN.md](README_data_EN.md)*
