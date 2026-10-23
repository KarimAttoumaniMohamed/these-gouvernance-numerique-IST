# Data sources — I–S–T thesis

> Karim Attoumani Mohamed & Jérôme Velo
> University of Toamasina, 2026
> Repository: https://github.com/karimattoumanimohamed/these-gouvernance-numerique-IST

This document describes all the data sources used in the thesis to produce
the figures, simulations and analytical estimates. For each source, it states
the conditions of access, the processing applied and the figures concerned.
French version: [README_donnees.md](README_donnees.md).

---

## 1. IGF data (2006–2025)

**Description**
Longitudinal data on participation in the Internet Governance Forum covering
20 editions (from Athens in 2006 to Lillestrøm in 2025). They include the
geographical distribution of participants, regional representation in the
sessions, travel fellowship funding data and the linguistic distribution of
preparatory documents.

**Source**
IGF Secretariat, United Nations.
https://www.intgovforum.org/

**Bibliographic reference**
IGF Secretariat. (2025). *IGF Secretariat Data (2006–2025)*.
Unpublished dataset.

**Conditions of access**
Aggregated participation data are publicly available on the official IGF
portal. Detailed data were obtained from the IGF Secretariat for academic
research. These data may not be redistributed without prior authorisation.

**Processing applied**
- Missing data handled by linear interpolation (2008 and 2012 — partial data)
- Regional categories normalised according to the UN classification
- Representation indicators built as ratios of relative participation to each
  region's share of the world population and of the Internet user base

**Figures concerned**
3.1, 3.2

---

## 2. IETF Datatracker data

**Description**
Statistics on participation in and contributions to the Internet Engineering
Task Force. They include author data for RFCs and Internet-Drafts by
institution and country, the geographical distribution of working group
chairs, IETF meeting attendance statistics and contribution metrics by region.

**Source**
IETF Datatracker — public access via the web interface and REST API.
https://datatracker.ietf.org/

**Bibliographic references**
Internet Engineering Task Force. (2025). *Datatracker*.
https://datatracker.ietf.org/

Arkko, J. (2024). *Distribution of number of RFCs per continent*.
Internet Research Task Force.
https://irtf.org/rfc-distribution

**Conditions of access**
Fully public. No restriction on use for academic research. Official REST API
available without authentication.

**Processing applied**
- Extraction of author metadata for all published RFCs (RFC 1 to RFC 9700+,
  1969–2025)
- Geographical attribution of institutions by matching against public
  institutional databases
- Gini coefficients for the geographical concentration of meetings and authors
  (Gini = 0.72 for meeting venues)
- Analysis of variance (ANOVA) to identify the factors explaining regional
  participation (R² = 0.68, p < 0.01)

**Figures concerned**
3.1, 3.2

---

## 3. Energy and infrastructure data (Chapter 4)

**Description**
Data on the energy consumption of AI systems and digital infrastructures,
carbon footprint benchmarks for large language models, and statistics on
African digital infrastructure.

**Multiple sources**

| Source | Data | URL |
|--------|------|-----|
| The Shift Project (2019) | Global digital footprint | https://theshiftproject.org |
| Patterson et al. (2021) | Carbon emissions of LLM training | https://arxiv.org/abs/2104.10350 |
| IEA (2022) | Global data centre consumption | https://www.iea.org |
| IEA (2025) | Energy and AI | https://www.iea.org/reports/energy-and-ai |
| OpenAI (2024) | Environmental impact of AI models | https://openai.com/research |
| Hugging Face (2024) | Inference energy benchmarks | https://huggingface.co/blog |
| HTTP Archive (2023) | Standard web consumption | https://httparchive.org |
| Reuters/IFC (2025) | African data centre capacity | Public |
| GSMA (2024) | African mobile connectivity | https://www.gsma.com |
| de Vries (2023) | Energy footprint of AI | https://doi.org/10.1016/j.joule.2023.09.004 |
| You (2025) — Epoch AI | Energy per request (≈ 0.3 Wh, GPT-4o) | https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use |
| Elsworth et al. (2025) — Google | Energy, water and CO₂e per request (production measurements) | https://arxiv.org/abs/2508.15734 |
| Ember (2026) | African electricity generation (965 TWh in 2024) | https://ember-energy.org/data/yearly-electricity-data/ |

*The rows OpenAI (2024), Hugging Face (2024), HTTP Archive (2023) and
Reuters/IFC (2025) are the sources of the article (Karim & Velo, 2025b,
references [8] to [10] and [16]); they are not included in the bibliography of
the thesis, which relies on the more recent measurements listed after them
(thesis, § 4.2).*

**Processing applied**
- Consolidation of the values from the publications cited by the article,
  supplemented by the authors' simulations
- A flat 30% correction factor for the specificities of African infrastructure
  (network losses, power cuts, extra cost of cloud hosted abroad); this factor
  is an assumption of the article and has not been documented by a
  calibration
- Projections of the revised thesis (script `simulation/energie.py`): demand
  in 2030 = 600 million users × adoption rate × requests per day ×
  consumption per request, under two assumptions: high (2.9 to 5 Wh per
  request, estimates published in 2023 and used by the article) and low (0.24
  to 0.3 Wh, measurements published in 2025). Version 2.0 applied an annual
  growth rate to an initial value of 174 GWh/day that already corresponded to
  2030 (double projection); this calculation is no longer used
- Benchmark: African electricity generation of 965 TWh in 2024, i.e. about
  2,640 GWh/day (Ember, 2026)

**Figures concerned**
4.1, 4.2

---

## 4. UAMINIFU simulation data (Chapter 5)

**Description**
The curves of Figure 5.1 come from a simulation on stylised scenarios, not
from direct empirical data collection. The parameters are set by assumption,
on the basis of the existing literature, and are not estimated from data. The
UAMINIFU framework is developed in Chapter 5 of the thesis (working paper, to
be submitted).

**Parameter values**

| Parameter | Value | Justification |
|-----------|-------|---------------|
| γ (trust amplification) | 1.15 | Moderate non-linearity — literature on socio-technical systems |
| δ (risk amplification) | 1.55 | Strong non-linearity — Helbing (2013), Taleb (2007) |
| κ (decay rate) | 7.0 | Rapid post-threshold decay — GSMA (2023) |
| Rc (critical threshold) | 0.62 | Tipping threshold — stylised value |

**Revised formulation (thesis, §§ 5.2 and 5.3)**
The DTI is computed on the means of the factors (S̄ = ΣSᵢ/n, R̄ = ΣRⱼ/m), the
risk term is (R̄^δ + Σλⱼₖ·Rⱼ·Rₖ)/(1 + Σλⱼₖ), and the decay pulls the score
towards the floor −1: DTI = −1 + (1 + T)·e^(−κ(R̄ − Rc)⁺). The DTI is thus
bounded in [−1, 1] and decreasing in each risk factor (script
`simulation/dti.py`).

**Simulation scenarios**
- Scenario A (high risk): Sᵢ = 0.50, 0.75, 0.25, 0.50, 0.25 (S̄ = 0.45) — Rⱼ = 0.75, 0.75, 0.50, 0.75, 0.50, 1.00 (R̄ = 0.708) — DTI = −0.536
- Scenario B (mature): Sᵢ = 0.75, 0.75, 0.50, 0.75, 0.75 (S̄ = 0.70) — Rⱼ = 0.25, 0, 0.25, 0, 0.25, 0 (R̄ = 0.125) — DTI = 0.630
- Interactions: same pairs and coefficients as for the Comoros (Table 5.III, Σλ = 0.75)

**Instantiation from public sources (thesis, § 5.6)**
The DTI is also instantiated for the Union of the Comoros from public sources
only: GSMA Intelligence, *Digital Africa Index* (2024-2025 data, 2025 period
used) for variables S2 to S5 and R2 to R5; ITU, *Global Cybersecurity Index
2024* for S1; the law of 26 June 2014 on the protection of personal data for
R1. An expert elicitation questionnaire (n = 8) complements these sources. No
internal operator data are used. Result: S̄ = 0.467, R̄ = 0.889,
DTI = −0.908 (collapse zone), robust to the sensitivity analysis (−0.94 to
−0.87). This point appears in panel (a) of Figure 5.1.

**Important limitation**
The curves of Figure 5.1 are computed, not empirical. Calibration on real time
series (fraud incidents, downtime, published compliance indicators) is a
research perspective identified in the thesis (General conclusion, research
perspectives).

**References**
- Karim, A. M., & Velo, J. (2026). UAMINIFU: Modeling digital trust as a
  systemic and economic variable for AI-driven digital sovereignty. Working
  paper integrated into the thesis, University of Toamasina. To be submitted.
- GSMA Intelligence. (2025). Digital Africa Index: 2024-2025 data.
- International Telecommunication Union. (2024). Global Cybersecurity Index 2024.
- GSMA. (2023). State of the Industry Report on Mobile Money.
- Helbing, D. (2013). Globally networked risks. Nature, 497, 51–59.
- Williamson, O. E. (1985). The Economic Institutions of Capitalism.

**Figures concerned**
5.1

---

## 5. Data for the case of the Comoros (Chapter 6)

**Description**
Contextual data on the Comorian digital system used for the case study of
Section 6.3 of the thesis. All come from public sources or freely available
institutional reports. The only primary data collection consists of expert
elicitation questionnaires (Section 6.3.6: Comorian actors, n = 8, and
practitioners gathered at ICANN86, n = 9); the individual answers are not
published in this repository.

**Sources**

| Source | Data used |
|--------|-----------|
| ITU (2024) | Internet penetration rate, telecom infrastructure |
| World Bank (2024) | Digital development indicators |
| Smart Africa Alliance (2024) | African digital strategies |
| GSMA (2023) | Mobile money data, Sub-Saharan Africa |
| UNCTAD (2021) | Digital economy of developing countries |
| IFC and GSMA (TechAfrica News, 2026) | Share of African data hosted outside the continent (X₀) |
| GSMA Intelligence (2025) | Digital Africa Index (DTI variables S2–S5, R2–R5) |
| ITU (2024) — GCI 2024 | Cybersecurity index (DTI variable S1) |
| Union of the Comoros (2014) | Data protection law (DTI variable R1) |

**Analytical estimates used**

| Variable | Estimated value | Main source |
|----------|-----------------|-------------|
| I₀ (initial inclusion) | 0.33 | ITU/World Bank (2024) — 32.5% of the population uses the Internet (rounded) |
| S₀ (initial sustainability) | 0.40 | IEA + energy data for the Comoros |
| T₀ (initial trust) | 0.45 | GSMA (2023) — mobile money adoption |
| X₀ (external dependence) | 0.80 | Lower bound of the estimates of the share of African data hosted outside the continent (more than 80% according to IFC and GSMA; 85% according to Karim & Velo, 2025b) |

**Important limitation**
These values are analytical estimates based on secondary data, not direct
empirical measurements calibrated in the field. They are approximations of
illustrative value; the questionnaires of Section 6.3.6 provide a first
comparison with practitioners' views. Wider primary data collection in the
Comoros is Axis 1 of the research perspectives (General conclusion,
Section 3).

**Figures concerned**
6.4

---

## 6. Simulation data of the model G(t) (Chapter 6)

**Description**
The data of Figures 6.2 and 6.3 are entirely simulated from the dynamic model
G(t) formalised in Chapter 2 of the thesis. No external empirical data are
used for these figures.

**Parameters of the model G(t)**

| Parameter | Value | Description |
|-----------|-------|-------------|
| α | 0.35 | Weight of inclusion I |
| β | 0.35 | Weight of sustainability S |
| χ | 0.30 | Weight of trust T |
| γ | 1.15 | Non-linearity exponent of I |
| δ | 1.55 | Non-linearity exponent of S |
| θ | 1.35 | Non-linearity exponent of T |
| φ | 0.50 | Sensitivity to systemic risk |
| Rc | 0.62 | Critical threshold for the degradation of T |
| κ | 7.0 | Rate of exponential decay of T |

**Note on Figure 6.3**
The intensity of use is defined as A_t = min(1, 0.3·λ/10): it saturates from
λ ≈ 34, so the trajectories for λ = 40 to 100 are identical. The simulation
therefore cannot independently establish the indicative threshold λ ≈ 40 of
Chapter 4 (thesis, § 6.2.2).

**Full reproducibility**
Figures 6.1 to 6.4 can be reproduced with the scripts of the `simulation/`
folder (correspondence in the main README), and their English versions with
those of `simulation/en/`:

```bash
cd simulation
python figure_6_1_diagramme_causal.py ; python figure_6_2_6_3.py ; python figure_6_4_comores.py
```

**Figures concerned**
6.1, 6.2, 6.3, 6.4

---

## 7. ICANN86 Policy Forum sessions (Chapter 6, Appendix C)

**Description**
I, S and T counts of the 25 recorded sessions of the ICANN86 Policy Forum
(Seville, 8-11 June 2026): 5 ccNSO, 8 At-Large and 12 GAC sessions. File:
`data/icann86_sessions.csv` (one row per session: Zoom recording identifier,
community, date and start time in UTC, title, counts under both rules).

**Source**
Automatic transcripts (VTT) of the Zoom recordings published by ICANN for each
session: https://icann86.sched.com/list/simple

**Conditions of access**
The recordings and transcripts are public on the ICANN website. They are not
redistributed in this repository; the session chats, which contain exchanges
between named participants, are not used.

**Processing applied** (script `simulation/icann86_codage.py`)
- A segment (subtitle line, without the speaker's name) is counted once for a
  variable if it contains at least one keyword of that variable (dictionary of
  Appendix C)
- "sous-chaine" rule (counts of the thesis): case-insensitive string search;
  it also retains words that contain a keyword ("observer" for "server")
- "mot" rule (control variant): whole words, plurals accepted; it reduces S
  from 356 to 309 segments without changing the dominant variable of any
  community
- Titles are reconstructed from the opening announcement of each transcript
  (corrected for speech-recognition errors)

**Figures and tables concerned**
Section 6.3.7; summary table of Appendix C (reference output:
`resultats/icann86_synthese.txt`)

---

## FAIR principles

This repository follows the FAIR principles for scientific data management
(Wilkinson et al., 2016):

- **Findability** — repository indexed on GitHub with a permanent Zenodo DOI
- **Accessibility** — code and figures freely available under the MIT licence
- **Interoperability** — standard formats: Python, PNG, SVG, Markdown
- **Reusability** — complete documentation, explicit licence, detailed
  parameters allowing the model to be reproduced and extended

**Reference**
Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific
data management and stewardship. *Scientific Data, 3*, 160018.
https://doi.org/10.1038/sdata.2016.18

---

*Last updated: October 2026 — Version 3.1.0 (aligned with the revised manuscript of the thesis)*
