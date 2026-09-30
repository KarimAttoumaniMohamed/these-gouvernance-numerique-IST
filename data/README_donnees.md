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
listées à la suite (thèse, § 4.3 et Annexe C.3).*

**Traitement appliqué**
- Consolidation des valeurs issues des publications citées par l'article,
  complétées par les simulations des auteurs
- Application d'un facteur correctif forfaitaire de 30 % pour les
  spécificités des infrastructures africaines (pertes réseau, coupures
  d'électricité, surcoût du cloud hébergé à l'étranger) ; ce facteur est une
  hypothèse de l'article et n'a pas fait l'objet d'une calibration documentée
- Modélisation prospective par extrapolation exponentielle :
  E(t) = E₀·e^(αt) avec α ∈ [0,15 — 0,18] selon les scénarios
- Paramètre initial : E₀ = 174 GWh/jour. Cette valeur correspond, dans
  l'article, à la demande de 600 millions d'utilisateurs **à l'horizon 2030**
  (600 M × 100 requêtes/jour × 2,9 Wh), et non à la consommation de 2024.
  La Figure 4.1 la place en 2024 puis lui applique la croissance α : la
  trajectoire du scénario B est donc une borne haute exploratoire (thèse,
  § 4.3)
- Repère de comparaison : production électrique africaine de 965 TWh en
  2024, soit environ 2 640 GWh/jour (Ember, 2026). La demande de 174 à
  300 GWh/jour en représenterait de 7 à 11 %. La version 1.0 du code
  rapportait la demande à un dénominateur non sourcé de 874 GWh/jour,
  vraisemblablement la demande électrique africaine de 2019 (874 TWh/an)
  lue comme des GWh/jour ; ce calcul est retiré en version 2.0

**Figures concernées**
4.1, 4.2

---

## 4. Données de simulation UAMINIFU (Chapitre 5)

**Description**
Les courbes de la Figure 5.1 sont issues d'une simulation sur scénarios
stylisés et non d'une collecte empirique directe. Les paramètres sont calibrés
sur des hypothèses plausibles fondées sur la littérature existante. Le cadre
UAMINIFU est développé au chapitre 5 de la thèse (document de travail, à
soumettre).

**Paramètres de calibration**

| Paramètre | Valeur | Justification |
|-----------|--------|---------------|
| γ (amplification confiance) | 1,15 | Non-linéarité modérée — littérature sur systèmes sociotechniques |
| δ (amplification risque) | 1,55 | Non-linéarité forte — Helbing (2013), Taleb (2007) |
| κ (vitesse décroissance) | 7,0 | Décroissance rapide post-seuil — GSMA (2023) |
| Rc (seuil critique) | 0,62 | Seuil de basculement — calibration stylisée |

**Scénarios de simulation**
- Scénario A (risque élevé) : ΣSᵢ = 2,2 — ΣRⱼ = 2,7 — R̄ = ΣRⱼ/6 = 0,45 — DTI = −2,69
- Scénario B (mature) : ΣSᵢ = 3,5 — ΣRⱼ = 0,7 — R̄ = ΣRⱼ/6 = 0,12 — DTI = 3,60

Dans les deux scénarios, R̄ reste sous Rc = 0,62 : la décroissance n'est pas
activée. Les valeurs de la version initiale du document de travail (−1,06 et
3,59) reposaient sur des puissances erronées et des facteurs de décroissance
non dérivés de l'équation (thèse, § 5.4.2).

**Instanciation sur sources publiques (thèse, § 5.6.4)**
Le DTI est par ailleurs instancié pour l'Union des Comores à partir de sources
exclusivement publiques : GSMA Intelligence, *Digital Africa Index* (données
2024-2025, période 2025 retenue) pour les variables S2 à S5 et R2 à R5 ;
ITU, *Global Cybersecurity Index 2024* pour S1 ; loi du 26 juin 2014 portant
protection des données à caractère personnel pour R1. Un questionnaire
d'élicitation d'experts (n = 8) complète ces sources. Aucune donnée interne
d'opérateur n'est mobilisée. Résultat : ΣSᵢ = 2,336, ΣRⱼ = 5,333,
DTI ≈ −1,73 (zone d'effondrement), résultat robuste à l'analyse de
sensibilité. Cette instanciation n'est pas tracée dans la Figure 5.1.

**Limite importante**
Les courbes de la Figure 5.1 sont simulées et non empiriques. Une calibration
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
l'étude de cas de la section 6.5 de la thèse. Toutes issues de sources
publiques ou de rapports institutionnels librement accessibles. La seule
collecte primaire consiste en questionnaires d'élicitation d'experts
(section 6.5.6 : acteurs comoriens, n = 8 ; section 6.5.7 : praticiens réunis
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
| FPF (2025) | Flux de données transfrontaliers en Afrique |
| GSMA Intelligence (2025) | Digital Africa Index (variables S2–S5, R2–R5 du DTI) |
| ITU (2024) — GCI 2024 | Indice de cybersécurité (variable S1 du DTI) |
| Union des Comores (2014) | Loi sur la protection des données (variable R1 du DTI) |

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
Elles constituent des approximations à valeur illustrative ; les
questionnaires de la section 6.5.6 en proposent une première confrontation.
Une collecte de données primaires plus large aux Comores constitue l'Axe 1
des perspectives de recherche (Conclusion générale, section 3).

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

**Note sur la Figure 6.2**
L'intensité d'usage y est définie par A_t = min(1 ; 0,3·λ/10) : elle sature
dès λ ≈ 34, de sorte que les trajectoires λ = 40 à 100 sont identiques. La
simulation ne permet donc pas d'établir de façon indépendante le seuil
indicatif λ ≈ 40 du chapitre 4 (thèse, § 6.4.2).

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
- **Interoperability** — formats standards : Python, PNG, SVG, Markdown
- **Reusability** — documentation complète, licence explicite, paramètres
  détaillés permettant la reproduction et l'extension du modèle

**Référence**
Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific
data management and stewardship. *Scientific Data, 3*, 160018.
https://doi.org/10.1038/sdata.2016.18

---

*Dernière mise à jour : 2026 — Version 2.0 (alignée sur le manuscrit final de la thèse)*
