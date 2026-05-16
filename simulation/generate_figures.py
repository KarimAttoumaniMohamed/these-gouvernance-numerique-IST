# -*- coding: utf-8 -*-
"""
=============================================================================
ANNEXE E — CODES PYTHON DE GÉNÉRATION DES FIGURES DE LA THÈSE

Thèse : Vers une gouvernance inclusive, durable et fiable du numérique :
modélisation systémique de l'inclusion, de la soutenabilité et de la
confiance à l'ère de l'intelligence artificielle

Auteurs : Karim Attoumani Mohamed & Jérôme Velo
Université de Toamasina — Faculté des Sciences et Technologies
Doctorat en Mathématiques, Informatique et Applications, 2025

Organisation :
  E.1  Dépendances et configuration commune
  E.2  Figure 3.1 — Réseau DSGM et niveaux de participation
  E.3  Figure 3.2 — Simulation participation sous trois scénarios
  E.4  Figure 4.1 — Projections énergétiques Afrique 2024-2030
  E.5  Figure 4.2 — Effet du coefficient d'orchestration λ
  E.6  Figure 5.1 — Dégradation non linéaire UAMINIFU
  E.7  Figures 6.1, 6.2, 6.3 — Modèle G(t) : scénarios, sensibilité λ, Comores

Point d'entrée : exécuter main() pour générer toutes les figures.
Les fichiers PNG sont sauvegardés dans le répertoire courant.
=============================================================================
"""

# =============================================================================
# E.1 — DÉPENDANCES ET CONFIGURATION COMMUNE
# =============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import networkx as nx
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, List

# Configuration graphique commune à toutes les figures
plt.rcParams.update({
    'font.family':    'DejaVu Sans',
    'font.size':      10,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi':     300,
})

# Palette commune
PALETTE = {
    'bleu':   '#1f77b4',
    'orange': '#ff7f0e',
    'vert':   '#2ca02c',
    'rouge':  '#d62728',
    'violet': '#9467bd',
    'marron': '#8c564b',
    'bleu_f': '#2166ac',
}

OUTPUT_DIR = "./"   # Modifier pour changer le répertoire de sortie


# =============================================================================
# E.2 — FIGURE 3.1 : RÉSEAU D'INFLUENCE PONDÉRÉ (DSGM)
#        ET ÉVOLUTION TEMPORELLE DE LA PARTICIPATION P_i(t)
#
# Source : Karim & Velo (2025a), IEEE ICECER
# DOI : 10.1109/ICECER65523.2025.11401243
# =============================================================================

def generate_figure_3_1(save=True):
    """
    Génère la Figure 3.1 :
    - Panneau gauche  : réseau dirigé pondéré G=(V,E,W,D) — modèle DSGM
    - Panneau droit   : trajectoires P_i(t) par catégorie de parties prenantes
    """

    # --- Graphe dirigé pondéré G=(V,E,W,D) ---
    COLORS_NODES = {
        'States':               '#2166ac',
        'Private Sector':       '#d62728',
        'Civil Society':        '#2ca02c',
        'Technical Community':  '#ff7f0e',
        'End Users':            '#9467bd',
        'International Orgs':   '#8c564b',
    }
    LABELS_FR = {
        'States':               'États',
        'Private Sector':       'Secteur privé',
        'Civil Society':        'Société civile',
        'Technical Community':  'Communauté\ntechnique',
        'End Users':            'Utilisateurs\nfinaux',
        'International Orgs':   'Organisations\ninternationales',
    }

    G = nx.DiGraph()
    nodes = list(COLORS_NODES.keys())
    G.add_nodes_from(nodes)

    # Poids W(u,v) calibrés sur données IGF/IETF (Karim & Velo, 2025a)
    edges = [
        ('States',              'Private Sector',      0.8),
        ('States',              'Civil Society',        0.6),
        ('States',              'Technical Community',  0.5),
        ('Technical Community', 'End Users',            0.9),
        ('Technical Community', 'States',               0.4),
        ('Private Sector',      'End Users',            0.7),
        ('Private Sector',      'States',               0.6),
        ('International Orgs',  'States',               0.5),
        ('International Orgs',  'Civil Society',        0.4),
        ('Civil Society',       'Technical Community',  0.4),
        ('Civil Society',       'States',               0.3),
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = {
        'States':               np.array([0.0,  0.6]),
        'Private Sector':       np.array([0.7,  0.8]),
        'Civil Society':        np.array([-0.7, 0.3]),
        'Technical Community':  np.array([0.6, -0.3]),
        'End Users':            np.array([0.0, -0.8]),
        'International Orgs':   np.array([-0.6, 0.9]),
    }

    centrality   = nx.degree_centrality(G)
    node_sizes   = [3500 + centrality[n] * 8000 for n in nodes]
    node_colors  = [COLORS_NODES[n] for n in nodes]
    weights      = [G[u][v]['weight'] for u, v in G.edges()]

    fig = plt.figure(figsize=(16, 7))
    fig.suptitle(
        "Figure 3.1 — Réseau d'influence pondéré des parties prenantes de la gouvernance de l'Internet\n"
        "et évolution temporelle des niveaux de participation P_i(t) — Modèle DSGM",
        fontsize=11, fontweight='bold', y=1.01
    )

    ax1 = fig.add_subplot(1, 2, 1)

    nx.draw_networkx_edges(G, pos, ax=ax1,
        width=[w * 3.5 for w in weights], edge_color='#555555',
        alpha=0.65, arrows=True, arrowsize=18, arrowstyle='-|>',
        connectionstyle='arc3,rad=0.08',
        min_source_margin=25, min_target_margin=25)

    edge_labels = {(u, v): f"{G[u][v]['weight']:.1f}" for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
        font_size=7.5, font_color='#333333',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', alpha=0.7), ax=ax1)

    nx.draw_networkx_nodes(G, pos, ax=ax1,
        node_color=node_colors, node_size=node_sizes, alpha=0.92)
    nx.draw_networkx_labels(G, pos, labels={n: LABELS_FR[n] for n in nodes},
        font_size=8.5, font_weight='bold', font_color='white', ax=ax1)

    ax1.set_title(
        "Réseau d'influence pondéré G = (V, E, W, D)\n"
        "Taille des nœuds ∝ centralité de degré",
        fontsize=9.5, fontweight='bold', pad=10)
    ax1.axis('off')

    legend_elements = [mpatches.Patch(color=COLORS_NODES[n],
                       label=LABELS_FR[n].replace('\n', ' ')) for n in nodes]
    ax1.legend(handles=legend_elements, loc='lower left', fontsize=7.5,
               framealpha=0.85, title='Catégories de parties prenantes',
               title_fontsize=8)
    ax1.annotate('72 % des positions\ncentrales : Nord global',
                 xy=(0.02, 0.95), xycoords='axes fraction',
                 fontsize=7.5, color='#8B0000',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff0f0', alpha=0.85))

    # --- Panneau droit : trajectoires P_i(t) ---
    ax2 = fig.add_subplot(1, 2, 2)
    t = np.arange(0, 20, 1)
    participation = {
        'States':               0.40 + 0.018 * t,
        'Private Sector':       0.35 + 0.014 * t,
        'Civil Society':        0.20 + 0.025 * np.sin(t / 4) + 0.008 * t,
        'Technical Community':  0.28 + 0.010 * t,
        'End Users':            0.10 + 0.015 * np.cos(t / 3) + 0.005 * t,
        'International Orgs':   0.30 + 0.012 * t,
    }
    for node, values in participation.items():
        ax2.plot(t, values, color=COLORS_NODES[node], linewidth=2.0,
                 label=LABELS_FR[node].replace('\n', ' '),
                 marker='o' if node in ['End Users', 'Civil Society'] else None,
                 markersize=3.5, markevery=4)

    ax2.axvline(x=5, color='black', linestyle='--', linewidth=1.3, alpha=0.7)
    ax2.annotate("Activation des\npolitiques d'inclusion\n(t = 5)",
                 xy=(5, 0.72), xytext=(7.5, 0.70), fontsize=7.5, color='black',
                 arrowprops=dict(arrowstyle='->', color='black', lw=0.9),
                 bbox=dict(boxstyle='round,pad=0.25', facecolor='lightyellow', alpha=0.85))
    ax2.axhspan(0.10, 0.22, alpha=0.08, color='red')

    ax2.set_xlabel("Période (t)", fontsize=9)
    ax2.set_ylabel("Niveau de participation P_i(t)", fontsize=9)
    ax2.set_title("Évolution temporelle des niveaux de participation P_i(t)\n"
                  "par catégorie de parties prenantes",
                  fontsize=9.5, fontweight='bold', pad=10)
    ax2.legend(loc='upper left', fontsize=7.5, framealpha=0.85)
    ax2.grid(True, alpha=0.3, linewidth=0.5)
    ax2.set_xlim(0, 19)
    ax2.set_ylim(0.0, 0.85)
    ax2.tick_params(labelsize=8)

    fig.text(0.5, -0.03,
        "© 2025 IEEE. Reproduit avec permission de : Karim, A. M., & Velo, J. (2025a). "
        "Towards Inclusive Internet Governance. ICECER 2025. DOI : 10.1109/ICECER65523.2025.11401243.",
        ha='center', fontsize=7, color='#555555', style='italic')

    plt.tight_layout()
    path = OUTPUT_DIR + "Figure_3_1_DSGM_reseau_participation.png"
    if save:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"  Figure 3.1 sauvegardée : {path}")
    plt.close()


# =============================================================================
# E.3 — FIGURE 3.2 : SIMULATION TEMPORELLE DE LA PARTICIPATION
#        SOUS TROIS SCÉNARIOS DE POLITIQUE D'INCLUSION
#
# Équation DSGM (Karim & Velo, 2025a, Éq. 3) :
#   P_i(t+1) = α·P_i(t) + β·S_i(t) − γ·[O_i(t) + μ·I(t)] + δ·π_i(t)
# =============================================================================

class GovernanceInclusionModel:
    """
    Modèle DSGM — dynamique de participation des parties prenantes.
    Implémente les équations (3) à (6) de Karim & Velo (2025a).
    """
    ACTORS = ['États', 'Secteur privé', 'Société civile',
              'Communauté technique', 'Utilisateurs finaux', 'Organisations intl.']
    COLORS = ['#2166ac', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b']

    def simulate(self, T=20, policy_mode='none'):
        """
        policy_mode : 'none' | 'moderate' | 'aggressive'
        """
        p = {'α': 0.90, 'β': 0.15, 'γ': 0.30, 'δ': 0.40, 'μ': 0.10}
        P = np.array([0.40, 0.35, 0.20, 0.28, 0.10, 0.35])
        w = np.array([1.0, 1.0, 1.2, 1.1, 1.3, 1.0])
        O = np.array([0.10, 0.10, 0.42, 0.32, 0.52, 0.20])
        S = np.array([0.80, 0.70, 0.30, 0.52, 0.20, 0.60])

        results = []
        for t in range(T):
            π = np.zeros(6)
            if policy_mode == 'moderate' and t >= T // 3:
                π = np.array([0.00, 0.00, 0.30, 0.20, 0.40, 0.10])
            elif policy_mode == 'aggressive' and t >= T // 4:
                π = np.array([0.00, 0.00, 0.55, 0.40, 0.75, 0.20])

            I_t = np.mean((P / np.max(P)) * w)                    # Éq. (4)
            P_norm = P / np.sum(P)
            H_t = -np.sum(P_norm * np.log(P_norm + 1e-10))        # Éq. (5)

            results.append({'Période': t,
                            **dict(zip(self.ACTORS, P.copy())),
                            'Inclusivité I(t)': I_t,
                            'Entropie H(t)': H_t})

            P = (p['α']*P + p['β']*S - p['γ']*(O + p['μ']*I_t) + p['δ']*π)  # Éq. (3)
            P = np.clip(P, 0.05, 0.95)

        return pd.DataFrame(results)


def generate_figure_3_2(save=True):
    """Génère la Figure 3.2 : simulation participation — trois scénarios."""
    model = GovernanceInclusionModel()
    T = 20
    df_none  = model.simulate(T=T, policy_mode='none')
    df_mod   = model.simulate(T=T, policy_mode='moderate')
    df_agg   = model.simulate(T=T, policy_mode='aggressive')

    scenarios = {
        'Référence (sans intervention)': (df_none,  '--', '#555555'),
        'Intervention modérée':          (df_mod,   '-',  '#1f77b4'),
        'Intervention agressive':        (df_agg,   '-.', '#d62728'),
    }

    fig = plt.figure(figsize=(16, 11))
    fig.suptitle(
        "Figure 3.2 — Simulation temporelle des niveaux de participation P_i(t)\n"
        "sous trois scénarios de politique d'inclusion — Modèle DSGM",
        fontsize=12, fontweight='bold', y=1.01)

    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.50, wspace=0.35)

    for col, (sc_name, (df_sc, ls, _)) in enumerate(scenarios.items()):
        ax = fig.add_subplot(gs[0, col])
        label = {0: "(A)", 1: "(B)", 2: "(C)"}[col]
        t_act = {1: T//3, 2: T//4}.get(col)
        for i, actor in enumerate(model.ACTORS):
            ax.plot(df_sc['Période'], df_sc[actor],
                    color=model.COLORS[i], linewidth=1.8,
                    linestyle=ls, label=actor,
                    marker=['o', 's', '^'][col], markersize=3, markevery=4)
        if t_act:
            ax.axvline(x=t_act, color='black', linestyle=':', linewidth=1.3, alpha=0.8)
            ax.annotate(f'Activation\n(t = {t_act})',
                        xy=(t_act, 0.82), xytext=(t_act+2, 0.88),
                        fontsize=7.5, arrowprops=dict(arrowstyle='->', lw=0.8))
        ax.axhspan(0.05, 0.18, alpha=0.10, color='red')
        ax.set_title(f"{label} {sc_name}", fontweight='bold', fontsize=9)
        ax.set_xlabel("Période (t)"); ax.set_ylabel("P_i(t)")
        ax.set_ylim(0.0, 1.0); ax.grid(True, alpha=0.3)
        ax.legend(fontsize=7, loc='upper left')
        ax.tick_params(labelsize=8)

    ax_d = fig.add_subplot(gs[1, :])
    for sc_name, (df_sc, ls, color) in scenarios.items():
        ax_d.plot(df_sc['Période'], df_sc['Inclusivité I(t)'],
                  color=color, linestyle=ls, linewidth=2.2, label=f'I(t) — {sc_name}')
        h_norm = df_sc['Entropie H(t)'] / df_sc['Entropie H(t)'].max()
        ax_d.plot(df_sc['Période'], h_norm, color=color, linestyle=ls,
                  linewidth=1.4, alpha=0.6, marker='D', markersize=3, markevery=3,
                  label=f'H(t) norm. — {sc_name}')

    ax_d.axvline(x=T//3, color='#1f77b4', linestyle=':', linewidth=1.2, alpha=0.7)
    ax_d.axvline(x=T//4, color='#d62728', linestyle=':', linewidth=1.2, alpha=0.7)
    ax_d.axhline(y=0.75, color='green', linestyle='--', linewidth=1.2,
                 alpha=0.6, label='Seuil équitable')
    ax_d.annotate('R² = 0,82 (p < 0,01)\nIC 95% : [118%, 153%]',
                  xy=(18, 0.90), xytext=(13, 0.96), fontsize=8, color='#1a5276',
                  bbox=dict(boxstyle='round,pad=0.35', facecolor='#eaf4fb', alpha=0.90),
                  ha='center')
    ax_d.set_title("(D) Indice d'inclusivité I(t) et entropie H(t) normalisée",
                   fontweight='bold')
    ax_d.set_xlabel("Période (t)"); ax_d.set_ylabel("Indice normalisé")
    ax_d.set_ylim(0.0, 1.05); ax_d.grid(True, alpha=0.3)
    ax_d.legend(loc='upper left', fontsize=7.5, ncol=2, framealpha=0.85)
    ax_d.tick_params(labelsize=8)

    fig.text(0.5, -0.025,
        "© 2025 IEEE. Reproduit avec permission de : Karim, A. M., & Velo, J. (2025a). "
        "Towards Inclusive Internet Governance. ICECER 2025. DOI : 10.1109/ICECER65523.2025.11401243.",
        ha='center', fontsize=7, color='#555555', style='italic')

    plt.tight_layout()
    path = OUTPUT_DIR + "Figure_3_2_participation_scenarios.png"
    if save:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"  Figure 3.2 sauvegardée : {path}")
    plt.close()


# =============================================================================
# E.4 — FIGURE 4.1 : PROJECTIONS ÉNERGÉTIQUES AFRIQUE 2024-2030
#
# Équations (Karim & Velo, 2025b) :
#   E(t) = E₀ · e^(αt)          [Éq. 1 — énergie]
#   B(t) = β₀ + β₁·Q(t)         [Éq. 2 — bande passante]
#   C_total = C_train + n·C_inf  [Éq. 4 — carbone]
# =============================================================================

def generate_figure_4_1(save=True):
    """Génère la Figure 4.1 : projections énergétiques Afrique 2024-2030."""
    annees = np.arange(2024, 2031)
    t = np.arange(0, 7)
    population_2030 = 600e6
    population = population_2030 * (1 - 0.33 * (1 - t / 6))

    # Modèle énergétique E(t) = E₀·e^(αt)
    E0, alpha = 174, 0.165
    energie_A = 1.2 * np.ones_like(t)
    energie_B = E0 * np.exp(alpha * t)
    energie_C = 0.60 * energie_B

    # Modèle bande passante
    requetes = 100 * (1 + 0.10)**t
    bp_A = 30 * (population / population_2030)
    bp_B = population * requetes * 3.5e-9
    bp_C = 0.50 * bp_B

    # Modèle carbone
    C_inf_B = 2.28e-6
    emissions_B = (10000 + population * requetes * 365 * C_inf_B) / 1e6
    emissions_C = (10000 + population * requetes * 365 * 0.40 * C_inf_B) / 1e6

    seuil = 0.15 * 874  # 15% capacité africaine ≈ 131 GWh/j
    CA, CB, CC = '#2ca02c', '#d62728', '#1f77b4'

    fig = plt.figure(figsize=(16, 11))
    fig.suptitle(
        "Figure 4.1 — Projections énergétiques, de bande passante et d'émissions carbone\n"
        "des interactions IA en Afrique (2024–2030) selon trois scénarios de déploiement",
        fontsize=12, fontweight='bold', y=1.01)

    gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.48, wspace=0.32)

    # Panneau A — Énergie
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.fill_between(annees, energie_A, energie_B, alpha=0.08, color=CB)
    ax1.fill_between(annees, energie_C, energie_B, alpha=0.06, color=CC)
    for val, col, ls, ms, lab in [
        (energie_A, CA, '-',  'o', 'Scénario A — Web classique'),
        (energie_B, CB, '-',  's', 'Scénario B — IA non optimisée'),
        (energie_C, CC, '--', '^', 'Scénario C — IA optimisée (−40%)'),
    ]:
        ax1.plot(annees, val, color=col, linewidth=2.2, linestyle=ls,
                 marker=ms, markersize=5, label=lab)
    ax1.axhline(y=seuil, color='#8B0000', linestyle=':', linewidth=1.5, alpha=0.85,
                label=f'Seuil critique (15% capacité africaine ≈ {seuil:.0f} GWh/j)')
    ax1.set_title("(A) Consommation énergétique quotidienne\nE(t) = E₀·e^(αt),  α = 16,5%",
                  fontweight='bold')
    ax1.set_ylabel("Énergie (GWh/jour)"); ax1.set_xlabel("Année")
    ax1.set_ylim(0, 520); ax1.set_xlim(2024, 2030)
    ax1.grid(True, alpha=0.3); ax1.legend(fontsize=7.5, loc='upper left')
    ax1.tick_params(labelsize=8)

    # Panneau B — Bande passante
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.fill_between(annees, bp_A, bp_B, alpha=0.07, color=CB)
    for val, col, ls, ms, lab in [
        (bp_A, CA, '-',  'o', 'Scénario A'),
        (bp_B, CB, '-',  's', 'Scénario B'),
        (bp_C, CC, '--', '^', 'Scénario C (−50%)'),
    ]:
        ax2.plot(annees, val, color=col, linewidth=2.2, linestyle=ls,
                 marker=ms, markersize=5, label=lab)
    ax2.set_title("(B) Bande passante quotidienne\nB(t) = β₀ + β₁·Q(t)",
                  fontweight='bold')
    ax2.set_ylabel("Bande passante (PB/jour)"); ax2.set_xlabel("Année")
    ax2.set_xlim(2024, 2030)
    ax2.grid(True, alpha=0.3); ax2.legend(fontsize=7.5, loc='upper left')
    ax2.tick_params(labelsize=8)

    # Panneau C — Émissions carbone
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.fill_between(annees, emissions_C, emissions_B, alpha=0.10, color=CB)
    ax3.plot(annees, emissions_B, color=CB, linewidth=2.2, linestyle='-',
             marker='s', markersize=5, label='Scénario B')
    ax3.plot(annees, emissions_C, color=CC, linewidth=2.2, linestyle='--',
             marker='^', markersize=5, label='Scénario C (−60%)')
    ax3.axhline(y=50, color='#8B4513', linestyle=':', linewidth=1.4, alpha=0.80,
                label='Référence : pays de taille moyenne (~50 Mt CO₂e/an)')
    ax3.set_title("(C) Émissions carbone annuelles\nC_total = C_train + n·C_inf",
                  fontweight='bold')
    ax3.set_ylabel("Mt CO₂e/an"); ax3.set_xlabel("Année")
    ax3.set_xlim(2024, 2030)
    ax3.grid(True, alpha=0.3); ax3.legend(fontsize=7.5, loc='upper left')
    ax3.tick_params(labelsize=8)

    # Panneau D — Tableau comparatif 2030
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.axis('off')
    data_table = [
        ['Indicateur', 'Scén. A\n(Web)', 'Scén. B\n(IA std.)', 'Scén. C\n(IA opt.)'],
        ['Énergie/jour (GWh)', f'{energie_A[-1]:.1f}', f'{energie_B[-1]:.0f}', f'{energie_C[-1]:.0f}'],
        ['% capacité africaine', f'{100*energie_A[-1]/874:.1f}%', f'{100*energie_B[-1]/874:.1f}%', f'{100*energie_C[-1]/874:.1f}%'],
        ['Bande passante/jour (PB)', f'{bp_A[-1]:.0f}', f'{bp_B[-1]:.0f}', f'{bp_C[-1]:.0f}'],
        ['Émissions CO₂e (Mt/an)', '—', f'{emissions_B[-1]:.1f}', f'{emissions_C[-1]:.1f}'],
        ['Ratio énergie vs Web', '×1', f'×{energie_B[-1]/energie_A[-1]:.0f}', f'×{energie_C[-1]/energie_A[-1]:.0f}'],
    ]
    table = ax4.table(cellText=data_table[1:], colLabels=data_table[0],
                      cellLoc='center', loc='center', bbox=[0.0, 0.05, 1.0, 0.90])
    table.auto_set_font_size(False); table.set_fontsize(8.5)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#2c3e50'); cell.set_text_props(color='white', fontweight='bold')
        elif col == 2: cell.set_facecolor('#fde8e8')
        elif col == 3: cell.set_facecolor('#e8f4fd')
        else: cell.set_facecolor('#f8f9fa')
        cell.set_edgecolor('#bdc3c7')
    ax4.set_title("(D) Valeurs clés comparatives — Afrique 2030",
                  fontweight='bold', fontsize=9, pad=10)

    fig.text(0.5, -0.01,
        "© 2025 IEEE. Reproduit avec permission de : Karim, A. M., & Velo, J. (2025b). "
        "Towards Sustainable Internet Governance. ICECER 2025. DOI : 10.1109/ICECER65523.2025.11401095.",
        ha='center', fontsize=7, color='#555555', style='italic')

    plt.tight_layout()
    path = OUTPUT_DIR + "Figure_4_1_energie_Afrique_2030.png"
    if save:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"  Figure 4.1 sauvegardée : {path}")
    plt.close()


# =============================================================================
# E.5 — FIGURE 4.2 : EFFET DU COEFFICIENT D'ORCHESTRATION λ
#
# Équation (Karim & Velo, 2025b, Éq. 3) :
#   Q'(t) = Q(t) · λ,  λ ∈ [5, 100]
# =============================================================================

def generate_figure_4_2(save=True):
    """Génère la Figure 4.2 : effet de λ sur Q'(t), énergie, bande passante."""
    lambda_values = np.linspace(5, 100, 500)
    lambda_disc   = np.array([5, 10, 20, 40, 60, 80, 100])
    Q_base, E_r, D_r = 100, 5e-3, 3.5e-3
    lambda_c = 40

    Q_prime   = Q_base * lambda_values
    energy_pu = E_r * Q_prime
    bw_pu     = D_r * Q_prime

    C_main, C_danger = '#1a6fdf', '#d62728'
    C_energy, C_bw   = '#9467bd', '#8c564b'

    fig = plt.figure(figsize=(16, 7))
    fig.suptitle(
        "Figure 4.2 — Effet du coefficient d'orchestration λ sur le volume effectif de requêtes\n"
        "Q'(t) = Q(t) · λ,  Q(t) = 100 req./utilisateur/jour,  λ ∈ [5, 100]",
        fontsize=12, fontweight='bold', y=1.02)

    gs = gridspec.GridSpec(1, 3, figure=fig, hspace=0.30, wspace=0.38)

    # Panneau A
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.axvspan(0, lambda_c, alpha=0.07, color='#2ca02c',
                label='Zone capacité africaine soutenable (λ < λ_c)')
    ax1.axvspan(lambda_c, 100, alpha=0.07, color=C_danger,
                label='Zone de dépassement capacitaire (λ > λ_c)')
    ax1.plot(lambda_values, Q_prime, color=C_main, linewidth=2.8,
             label="Q'(t) = Q(t) · λ")
    ax1.scatter(lambda_disc, Q_base * lambda_disc, color=C_main, s=55, zorder=5)
    ax1.axvline(x=lambda_c, color=C_danger, linestyle='--', linewidth=2.0,
                label=f'Seuil critique λ_c = {lambda_c}')
    ax1.axhline(y=Q_base * lambda_c, color=C_danger, linestyle=':', linewidth=1.3, alpha=0.7)
    ax1.annotate(f'λ_c = {lambda_c}\nCapacité africaine\nsystématiquement\ndépassée',
                 xy=(lambda_c, Q_base * lambda_c), xytext=(52, 2800),
                 fontsize=7.5, color='#8B0000',
                 arrowprops=dict(arrowstyle='->', color='#8B0000', lw=1.0),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff0f0', alpha=0.90))
    ax1.set_title("(A) Volume effectif de requêtes Q'(t)\npar utilisateur et par jour",
                  fontweight='bold')
    ax1.set_xlabel("Coefficient d'orchestration λ")
    ax1.set_ylabel("Requêtes effectives / utilisateur / jour")
    ax1.set_xlim(5, 100); ax1.set_ylim(0, 10500)
    ax1.grid(True, alpha=0.3); ax1.legend(fontsize=7.5, loc='upper left')
    ax1.tick_params(labelsize=8)

    # Panneau B
    ax2 = fig.add_subplot(gs[0, 1])
    ax2_twin = ax2.twinx()
    ax2.plot(lambda_values, energy_pu, color=C_energy, linewidth=2.5,
             label='Énergie (kWh/util./jour)')
    ax2.axvline(x=lambda_c, color=C_danger, linestyle='--', linewidth=1.8)
    ax2.fill_between(lambda_values, energy_pu,
                     where=(lambda_values >= lambda_c), alpha=0.12, color=C_danger)
    ax2_twin.plot(lambda_values, bw_pu, color=C_bw, linewidth=2.5, linestyle='-.',
                  label='Bande passante (GB/util./jour)')
    ax2_twin.set_ylabel("Bande passante (GB/util./jour)", color=C_bw, fontsize=8)
    ax2_twin.tick_params(axis='y', labelcolor=C_bw, labelsize=8)
    ax2.set_title("(B) Impact par utilisateur selon λ\nÉnergie (kWh) et bande passante (GB)/jour",
                  fontweight='bold')
    ax2.set_xlabel("Coefficient d'orchestration λ")
    ax2.set_ylabel("Énergie (kWh/util./jour)", color=C_energy, fontsize=8)
    ax2.tick_params(axis='y', labelcolor=C_energy, labelsize=8)
    ax2.set_xlim(5, 100); ax2.grid(True, alpha=0.3)
    lines1, lbl1 = ax2.get_legend_handles_labels()
    lines2, lbl2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1+lines2, lbl1+lbl2, fontsize=7.5, loc='upper left')

    # Panneau C — tableau
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.axis('off')
    rows = []
    for lam in [5, 10, 20, 40, 60, 80, 100]:
        qp = Q_base * lam
        rows.append([f'λ = {lam}', f'{qp:,}', f'{E_r*qp:.2f}',
                     f'{D_r*qp:.1f}',
                     '⚠ CRITIQUE' if lam >= lambda_c else '✓ Soutenable'])
    table = ax3.table(
        cellText=rows,
        colLabels=["λ", "Q' (req./j)", "Énergie\n(kWh)", "Bande p.\n(GB)", "Statut"],
        cellLoc='center', loc='center', bbox=[0.0, 0.05, 1.0, 0.90])
    table.auto_set_font_size(False); table.set_fontsize(8.0)
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_facecolor('#2c3e50'); cell.set_text_props(color='white', fontweight='bold')
        elif row > 0 and [5,10,20,40,60,80,100][row-1] >= lambda_c:
            cell.set_facecolor('#fff0f0' if col != 4 else '#fde8e8')
            if col in [0, 4]: cell.set_text_props(color='#8B0000', fontweight='bold')
        else:
            cell.set_facecolor('#f0fff0' if col != 4 else '#e8f8e8')
            if col in [0, 4]: cell.set_text_props(color='#1a5e20', fontweight='bold')
        cell.set_edgecolor('#bdc3c7')
    ax3.set_title("(C) Tableau comparatif par valeur de λ\n"
                  "Q(t)=100 req./j  |  E_r=5 Wh/req.  |  D_r=3,5 MB/req.",
                  fontweight='bold', fontsize=9, pad=10)

    fig.text(0.5, -0.04,
        "© 2025 IEEE. Reproduit avec permission de : Karim, A. M., & Velo, J. (2025b). "
        "Towards Sustainable Internet Governance. ICECER 2025. DOI : 10.1109/ICECER65523.2025.11401095.",
        ha='center', fontsize=7, color='#555555', style='italic')

    plt.tight_layout()
    path = OUTPUT_DIR + "Figure_4_2_lambda_orchestration.png"
    if save:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"  Figure 4.2 sauvegardée : {path}")
    plt.close()


# =============================================================================
# E.6 — FIGURE 5.1 : DÉGRADATION NON LINÉAIRE DE LA CONFIANCE — UAMINIFU
#
# Équations (Karim & Velo, soumis CARI 2026) :
#   T  = α·(ΣSᵢ)^γ − β·(ΣRⱼ)^δ − Σλⱼₖ(Rⱼ·Rₖ)   [DTI]
#   T' = T · e^(−κ · max(0, R − Rc))               [décroissance]
#   Ctx = C₀ + θ/T^η                                [coût transaction]
# Paramètres calibrés : γ=1.15, δ=1.55, κ=7.0, Rc=0.62
# =============================================================================

def generate_figure_5_1(save=True):
    """Génère la Figure 5.1 : dégradation non linéaire UAMINIFU."""
    # Paramètres UAMINIFU
    gamma, delta, kappa, Rc = 1.15, 1.55, 7.0, 0.62
    alpha_u, beta_u = 0.55, 0.45
    Sum_Si = 2.8
    lambda_total = 0.31   # Σλⱼₖ = 0.12 + 0.09 + 0.10

    R_values = np.linspace(0.0, 3.0, 1000)

    # Modèle linéaire
    T_linear = np.clip(1.0 - 0.35 * R_values, -2.5, 1.0)

    # Modèle non linéaire sans interaction
    T_nl_raw  = alpha_u * (Sum_Si**gamma) - beta_u * (R_values**delta)
    decay_nl  = np.exp(-kappa * np.maximum(0.0, R_values - Rc))
    T_nonlinear = T_nl_raw * decay_nl

    # UAMINIFU complet (+ terme interaction)
    interaction = lambda_total * (R_values**2) / 4.0
    T_uam_raw   = alpha_u*(Sum_Si**gamma) - beta_u*(R_values**delta) - interaction
    T_uaminifu  = T_uam_raw * np.exp(-kappa * np.maximum(0.0, R_values - Rc))

    # Coûts de transaction
    C0, theta_eco, eta_eco = 0.5, 0.8, 1.4
    T_pos = np.where(T_uaminifu > 0.05, T_uaminifu, np.nan)
    Ctx   = C0 + theta_eco / (T_pos**eta_eco)

    CL, CN, CU = '#1f77b4', '#ff7f0e', '#2ca02c'

    fig = plt.figure(figsize=(16, 8))
    fig.suptitle(
        "Figure 5.1 — Dégradation non linéaire de la confiance numérique sous risque croissant\n"
        "Comparaison : modèle linéaire, non linéaire sans interaction, cadre UAMINIFU complet",
        fontsize=12, fontweight='bold', y=1.02)

    gs = gridspec.GridSpec(1, 3, figure=fig, hspace=0.30, wspace=0.40)

    # Panneau A
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.axhspan(-2.5, 0, alpha=0.06, color='#d62728')
    ax1.axvspan(0, Rc, alpha=0.05, color=CL)
    ax1.text(Rc/2, 3.6, 'Zone\nstable', fontsize=7.5, color='#1a5276', ha='center',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='#eaf4fb', alpha=0.80))
    ax1.plot(R_values, T_linear,  color=CL, linewidth=2.2, linestyle='--',
             label='Modèle linéaire (référence)')
    ax1.plot(R_values, T_nonlinear, color=CN, linewidth=2.2, linestyle='-.',
             label='Non linéaire (sans interaction)')
    ax1.plot(R_values, T_uaminifu,  color=CU, linewidth=2.8, linestyle='-',
             label='UAMINIFU complet\n(non lin. + interaction + décroissance)')
    ax1.axhline(y=0, color='black', linewidth=0.8, alpha=0.5, linestyle=':')
    ax1.axvline(x=Rc, color='#d62728', linewidth=2.0, linestyle='--',
                label=f'Seuil critique Rc = {Rc}')
    idx_c = np.where(T_uaminifu < 0)[0]
    if len(idx_c) > 0:
        R_c = R_values[idx_c[0]]
        ax1.annotate(f'Point de basculement\nUAMINIFU\n(R ≈ {R_c:.2f})',
                     xy=(R_c, 0), xytext=(R_c-0.8, 1.8), fontsize=7.5, color='#1a5e20',
                     arrowprops=dict(arrowstyle='->', color='#1a5e20', lw=1.0),
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f8e8', alpha=0.90))
    ax1.set_title("(A) DTI en fonction du risque agrégé R", fontweight='bold')
    ax1.set_xlabel("Risque agrégé R"); ax1.set_ylabel("Digital Trust Index — DTI")
    ax1.set_xlim(0, 3.0); ax1.set_ylim(-2.5, 4.2)
    ax1.grid(True, alpha=0.3); ax1.legend(fontsize=7.5, loc='upper right')
    ax1.tick_params(labelsize=8)

    # Panneau B — Zoom sur zone de basculement
    ax2 = fig.add_subplot(gs[0, 1])
    mask = (R_values >= 0.3) & (R_values <= 1.5)
    R_z, TL_z, TN_z, TU_z = R_values[mask], T_linear[mask], T_nonlinear[mask], T_uaminifu[mask]
    ax2.fill_between(R_z, TU_z, TN_z, where=(TU_z < TN_z),
                     alpha=0.15, color=CU)
    ax2.fill_between(R_z, TN_z, TL_z, where=(TN_z < TL_z),
                     alpha=0.10, color=CN)
    ax2.plot(R_z, TL_z, color=CL, linewidth=2.2, linestyle='--', label='Linéaire')
    ax2.plot(R_z, TN_z, color=CN, linewidth=2.2, linestyle='-.', label='Non linéaire')
    ax2.plot(R_z, TU_z, color=CU, linewidth=2.8, linestyle='-', label='UAMINIFU complet')
    ax2.axhline(y=0, color='black', linewidth=0.8, alpha=0.5, linestyle=':')
    ax2.axvline(x=Rc, color='#d62728', linewidth=2.0, linestyle='--', label=f'Rc = {Rc}')
    ax2.annotate(f'T\' = T·e^(−κ·(R−Rc)₊)\nκ = {kappa}, Rc = {Rc}',
                 xy=(Rc+0.05, TU_z[R_z >= Rc][2]), xytext=(0.85, 2.5),
                 fontsize=7.5, color='#1a5e20',
                 arrowprops=dict(arrowstyle='->', color='#1a5e20', lw=0.9),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#e8f8e8', alpha=0.90))
    ax2.set_title(f"(B) Zoom — Zone de basculement\nR ∈ [0,3 – 1,5], autour de Rc = {Rc}",
                  fontweight='bold')
    ax2.set_xlabel("Risque agrégé R"); ax2.set_ylabel("DTI")
    ax2.set_xlim(0.3, 1.5); ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=7.5, loc='upper right'); ax2.tick_params(labelsize=8)

    # Panneau C — DTI et coûts de transaction
    ax3 = fig.add_subplot(gs[0, 2])
    ax3_twin = ax3.twinx()
    ax3.plot(R_values, T_uaminifu, color=CU, linewidth=2.5,
             label='DTI — UAMINIFU (axe gauche)')
    ax3.axhline(y=0, color='black', linewidth=0.8, alpha=0.5, linestyle=':')
    ax3.axvline(x=Rc, color='#d62728', linewidth=1.8, linestyle='--', alpha=0.8,
                label=f'Rc = {Rc}')
    ax3_twin.plot(R_values[~np.isnan(Ctx)], Ctx[~np.isnan(Ctx)],
                  color='#9467bd', linewidth=2.5, linestyle='--',
                  label='Ctx = C₀ + θ/T^η (axe droit)')
    ax3_twin.set_ylabel("Coût de transaction Ctx", color='#9467bd', fontsize=8)
    ax3_twin.tick_params(axis='y', labelcolor='#9467bd', labelsize=8)
    ax3_twin.set_ylim(0, 15)
    ax3.annotate('Quand DTI ↓\nCtx ↑ non linéairement\n(η = 1,4 > 1)',
                 xy=(0.55, 0.5), xytext=(1.2, 2.8), fontsize=7.5, color='#4a235a',
                 arrowprops=dict(arrowstyle='->', color='#4a235a', lw=0.9),
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='#f5eef8', alpha=0.90))
    for label, (R_pt, T_pt, color) in {
        'Scén. A\n(DTI = −1,06)': (2.7, -1.06, '#d62728'),
        'Scén. B\n(DTI = 3,59)':  (0.70, 3.59, '#2ca02c'),
    }.items():
        ax3.scatter([R_pt], [T_pt], color=color, s=80, zorder=6)
        ax3.annotate(label, xy=(R_pt, T_pt), xytext=(R_pt-0.6, T_pt-0.6),
                     fontsize=7, color=color,
                     arrowprops=dict(arrowstyle='->', color=color, lw=0.8),
                     bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.85))
    ax3.set_title(f"(C) DTI et coûts de transaction Ctx\nCtx = C₀ + θ/T^η  (C₀={C0}, θ={theta_eco}, η={eta_eco})",
                  fontweight='bold')
    ax3.set_xlabel("Risque agrégé R")
    ax3.set_ylabel("DTI", color=CU, fontsize=8)
    ax3.tick_params(axis='y', labelcolor=CU, labelsize=8)
    ax3.set_xlim(0, 3.0); ax3.set_ylim(-2.5, 4.2)
    ax3.grid(True, alpha=0.3)
    lines1, lbl1 = ax3.get_legend_handles_labels()
    lines2, lbl2 = ax3_twin.get_legend_handles_labels()
    ax3.legend(lines1+lines2, lbl1+lbl2, fontsize=7.5, loc='upper right')
    ax3.tick_params(labelsize=8)

    fig.text(0.5, -0.04,
        "Source : Karim, A. M., & Velo, J. (soumis). UAMINIFU: Modeling Digital Trust. "
        "CARI 2026. Reproduit du manuscrit soumis avec l'accord des auteurs.",
        ha='center', fontsize=7, color='#555555', style='italic')

    plt.tight_layout()
    path = OUTPUT_DIR + "Figure_5_1_UAMINIFU_trust_degradation.png"
    if save:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"  Figure 5.1 sauvegardée : {path}")
    plt.close()


# =============================================================================
# E.7 — FIGURES 6.1, 6.2, 6.3 : MODÈLE DYNAMIQUE G(t)
#
# Équation de gouvernance (Chapitre 2) :
#   G_t = α·I_t^γ + β·S_t^δ + χ·T_t^θ − φ·R_t
#   R_t = r₁·A_t·I_t·(1−S_t) + r₂·(1−T_t)·X_t + r₃·A_t·X_t
# =============================================================================

@dataclass
class ModelParameters:
    alpha: float = 0.35;  beta: float = 0.35;   chi: float = 0.30
    gamma: float = 1.15;  delta: float = 1.55;  theta: float = 1.35
    r1: float = 0.40;     r2: float = 0.35;     r3: float = 0.25
    phi: float = 0.50;    Rc: float = 0.62;     kappa: float = 7.0
    c_T_to_I: float = 0.08;  c_S_to_I: float = -0.10; c_pi: float = 0.05
    c_A_to_S: float = -0.12; c_inv_S: float = 0.06
    c_S_to_T: float = 0.09;  c_M_to_T: float = 0.07;  c_X_to_T: float = -0.08
    S_critical: float = 0.40

@dataclass
class ScenarioConfig:
    name: str; I0: float; S0: float; T0: float
    A_profile: List[float]; X_profile: List[float]
    pi_active: bool; inv_S_active: bool; M_active: bool
    color: str; linestyle: str

def _risk(I,S,T,A,X,p):
    return p.r1*A*I*(1-S) + p.r2*(1-T)*X + p.r3*A*X

def _G(I,S,T,R,p):
    return p.alpha*(I**p.gamma)+p.beta*(S**p.delta)+p.chi*(T**p.theta)-p.phi*R

def _trust_decay(T,R,p):
    return T*np.exp(-p.kappa*max(0.0, R-p.Rc))

def _evol_I(I,S,T,pi,p):
    d = p.c_T_to_I*T + p.c_S_to_I*max(0.0,p.S_critical-S) + (p.c_pi if pi else 0.0)
    return np.clip(I+d,0.0,1.0)

def _evol_S(S,A,inv,p):
    return np.clip(S + p.c_A_to_S*A + (p.c_inv_S if inv else 0.0), 0.0, 1.0)

def _evol_T(T,S,X,R,M,p):
    Td = _trust_decay(T,R,p)
    return np.clip(Td + p.c_S_to_T*S + (p.c_M_to_T if M else 0.0) + p.c_X_to_T*X, 0.0, 1.0)

def run_simulation_G(sc, p, T_periods=20):
    I,S,T = sc.I0, sc.S0, sc.T0
    h = {'I':[I],'S':[S],'T':[T],'R':[],'G':[]}
    for t in range(T_periods):
        A_t = sc.A_profile[t] if t < len(sc.A_profile) else sc.A_profile[-1]
        X_t = sc.X_profile[t] if t < len(sc.X_profile) else sc.X_profile[-1]
        R_t = _risk(I,S,T,A_t,X_t,p)
        h['R'].append(R_t); h['G'].append(_G(I,S,T,R_t,p))
        I = _evol_I(I,S,T,sc.pi_active,p)
        S = _evol_S(S,A_t,sc.inv_S_active,p)
        T = _evol_T(T,S,X_t,R_t,sc.M_active,p)
        h['I'].append(I); h['S'].append(S); h['T'].append(T)
    h['I']=h['I'][:-1]; h['S']=h['S'][:-1]; h['T']=h['T'][:-1]
    return h

def _build_4_scenarios(T=20):
    A_high   = [min(1.0, 0.7+0.01*t) for t in range(T)]
    A_low    = [0.3]*T; A_med = [0.5]*T
    X_high   = [0.85]*T; X_med = [0.65]*T
    X_low    = [max(0.40, 0.70-0.015*t) for t in range(T)]
    return [
        ScenarioConfig("Scénario 1 : Expansion non maîtrisée",
                       0.60,0.40,0.55,A_high,X_high,True,False,False,'#d62728','-'),
        ScenarioConfig("Scénario 2 : Dépendance technologique",
                       0.50,0.55,0.60,A_med,X_high,False,False,False,'#ff7f0e','--'),
        ScenarioConfig("Scénario 3 : Stabilisation par contrainte",
                       0.35,0.65,0.65,A_low,X_med,False,True,True,'#2ca02c','-.'),
        ScenarioConfig("Scénario 4 : Gouvernance équilibrée",
                       0.50,0.55,0.55,A_med,X_low,True,True,True,'#1f77b4','-'),
    ]

def generate_figure_6_1(save=True):
    """Génère la Figure 6.1 : quatre scénarios G(t)."""
    params = ModelParameters(); T = 20
    scenarios = _build_4_scenarios(T)
    histories = [run_simulation_G(sc, params, T) for sc in scenarios]
    periods   = list(range(T))
    labels    = {'I':'Inclusion I(t)','S':'Soutenabilité S(t)','T':'Confiance T(t)',
                 'R':'Risque systémique R(t)','G':'Gouvernance G(t)'}

    fig = plt.figure(figsize=(16, 12))
    fig.suptitle(
        "Figure 6.1 — Simulation du modèle dynamique de gouvernance G(t)\n"
        "Trajectoires comparées de I, S, T, R et G sous les quatre scénarios",
        fontsize=12, fontweight='bold', y=0.99)

    gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.50, wspace=0.35)
    axes = {'I':fig.add_subplot(gs[0,0]),'S':fig.add_subplot(gs[0,1]),
            'T':fig.add_subplot(gs[0,2]),'R':fig.add_subplot(gs[1,0]),
            'G':fig.add_subplot(gs[1,1]),'G_compare':fig.add_subplot(gs[2,:])}

    for sc, hist in zip(scenarios, histories):
        for var in ['I','S','T','R','G']:
            axes[var].plot(periods, hist[var], color=sc.color,
                           linestyle=sc.linestyle, linewidth=1.8, label=sc.name)
        axes['G_compare'].plot(periods, hist['G'], color=sc.color,
                               linestyle=sc.linestyle, linewidth=2.2, label=sc.name)

    axes['R'].axhline(y=0.62, color='black', linestyle=':', linewidth=1.3,
                      label='Seuil critique Rc = 0,62')
    axes['S'].axhline(y=0.40, color='orange', linestyle=':', linewidth=1.3,
                      label='Seuil critique S_c = 0,40')
    axes['G_compare'].axhspan(0.3, 0.7, alpha=0.08, color='green',
                               label='Zone de gouvernance stable')

    for var, ax in axes.items():
        if var == 'G_compare':
            ax.set_title("Vue comparative — Trajectoires de G(t) selon les quatre scénarios",
                         fontsize=10, fontweight='bold')
            ax.set_xlabel("Période (t)", fontsize=9); ax.set_ylabel("G(t)", fontsize=9)
            ax.legend(loc='lower right', fontsize=8, ncol=2)
        else:
            ax.set_title(labels.get(var,var), fontsize=9, fontweight='bold')
            ax.set_xlabel("Période (t)", fontsize=8)
            ax.set_ylabel(labels.get(var,var), fontsize=8)
            if var in ['R','S']: ax.legend(loc='best', fontsize=7)
        ax.set_xlim(0, T-1); ax.grid(True, alpha=0.3); ax.tick_params(labelsize=8)

    handles, lbls = axes['I'].get_legend_handles_labels()
    fig.legend(handles, lbls, loc='upper center', bbox_to_anchor=(0.5, 0.69),
               ncol=2, fontsize=8, framealpha=0.9)

    fig.text(0.5, -0.01,
        "Source : simulation du modèle dynamique G(t), code Python Annexe A & Annexe E. "
        "Paramètres : α=0,35, β=0,35, χ=0,30, γ=1,15, δ=1,55, θ=1,35, φ=0,50, Rc=0,62, κ=7,0.",
        ha='center', fontsize=7.5, color='#555555', style='italic')

    plt.tight_layout(rect=[0,0,1,0.97])
    path = OUTPUT_DIR + "Figure_6_1_quatre_scenarios.png"
    if save:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"  Figure 6.1 sauvegardée : {path}")
    plt.close()


def generate_figure_6_2(save=True):
    """Génère la Figure 6.2 : sensibilité au coefficient λ."""
    params = ModelParameters(); T = 20
    lambda_values = [10, 25, 40, 60, 80, 100]
    base_A = 0.3
    colors = plt.cm.RdYlGn_r(np.linspace(0.1, 0.9, len(lambda_values)))

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle(
        "Figure 6.2 — Analyse de sensibilité au coefficient d'orchestration λ\n"
        "Trajectoires de S(t) et G(t) sous six valeurs de λ ∈ [10, 100] — Contexte africain (S₀ = 0,42)",
        fontsize=10, fontweight='bold')

    for i, lam in enumerate(lambda_values):
        A_eff = min(1.0, base_A * (lam/10))
        sc = ScenarioConfig(f"λ = {lam}", 0.35, 0.42, 0.45,
                            [A_eff]*T, [0.75]*T,
                            False, False, False, colors[i], '-')
        hist = run_simulation_G(sc, params, T)
        periods = list(range(T))
        axes[0].plot(periods, hist['S'], color=colors[i], linewidth=1.8, label=f"λ = {lam}")
        axes[1].plot(periods, hist['G'], color=colors[i], linewidth=1.8, label=f"λ = {lam}")

    for ax, title, ylabel in zip(axes,
        ["Trajectoire de S(t) selon λ", "Trajectoire de G(t) selon λ"],
        ["Soutenabilité S(t)", "Gouvernance G(t)"]):
        ax.axhline(y=0.40, color='red', linestyle='--', linewidth=1.3,
                   alpha=0.8, label='Seuil critique S_c = 0,40')
        ax.set_title(title, fontsize=10, fontweight='bold')
        ax.set_xlabel("Période (t)", fontsize=9); ax.set_ylabel(ylabel, fontsize=9)
        ax.legend(fontsize=7.5, loc='lower left')
        ax.grid(True, alpha=0.3); ax.tick_params(labelsize=8); ax.set_xlim(0, T-1)

    axes[0].axvline(x=5, color='darkred', linestyle=':', linewidth=1.0, alpha=0.5)
    axes[0].annotate('λ_c ≈ 40\n(seuil critique\nafricain)',
                     xy=(5, 0.40), xytext=(8, 0.55), fontsize=7, color='darkred',
                     arrowprops=dict(arrowstyle='->', color='darkred', lw=0.8))

    fig.text(0.5, -0.04,
        "Source : simulation du modèle dynamique G(t), code Python Annexe A & Annexe E. "
        "Paramètres : S₀=0,42, I₀=0,35, T₀=0,45, X_t=0,75.",
        ha='center', fontsize=7.5, color='#555555', style='italic')

    plt.tight_layout()
    path = OUTPUT_DIR + "Figure_6_2_sensibilite_lambda.png"
    if save:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"  Figure 6.2 sauvegardée : {path}")
    plt.close()


def generate_figure_6_3(save=True):
    """Génère la Figure 6.3 : application au cas des Comores."""
    params = ModelParameters(); T = 25
    A_com = [min(0.65, 0.25+0.02*t) for t in range(T)]
    X_base = [0.78]*T
    X_S4   = [max(0.45, 0.78-0.015*t) for t in range(T)]

    scenarios = [
        ScenarioConfig("Comores — Statu quo", 0.33,0.40,0.45,
                       A_com, X_base, False,False,False,'#d62728','--'),
        ScenarioConfig("Comores — Gouvernance équilibrée (S4)", 0.33,0.40,0.45,
                       A_com, X_S4, True,True,True,'#1f77b4','-'),
    ]
    histories = [run_simulation_G(sc, params, T) for sc in scenarios]
    periods   = list(range(T))

    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    fig.suptitle(
        "Figure 6.3 — Application au cas des Comores\n"
        "Comparaison Statu quo vs Gouvernance équilibrée — Trajectoires I, S, T, R, G",
        fontsize=11, fontweight='bold')

    var_labels = {'I':'Inclusion I(t)','S':'Soutenabilité S(t)','T':'Confiance T(t)',
                  'R':'Risque systémique R(t)','G':'Gouvernance G(t)'}

    for idx, (var, ax) in enumerate(zip(['I','S','T','R','G'], axes.flatten()[:5])):
        for sc, hist in zip(scenarios, histories):
            ax.plot(periods, hist[var], color=sc.color, linestyle=sc.linestyle,
                    linewidth=2.0, label=sc.name)
        if var == 'R':
            ax.axhline(y=params.Rc, color='black', linestyle=':', linewidth=1.2,
                       label=f'Seuil Rc = {params.Rc}')
        if var == 'S':
            ax.axhline(y=params.S_critical, color='orange', linestyle=':',
                       linewidth=1.2, label=f'Seuil S_c = {params.S_critical}')
            ax.axhline(y=0.33, color='gray', linestyle=':', alpha=0.5,
                       linewidth=1.0, label='S₀ initial')
        ax.set_title(var_labels[var], fontsize=9, fontweight='bold')
        ax.set_xlabel("Période (t)", fontsize=8); ax.set_ylabel(var, fontsize=8)
        ax.legend(fontsize=7, loc='best'); ax.grid(True, alpha=0.3)
        ax.tick_params(labelsize=8); ax.set_xlim(0, T-1)

    ax_s = axes.flatten()[5]; ax_s.axis('off')
    lines = [
        "RÉSULTATS FINAUX (t = 25)", "",
        f"{'Variable':<18} {'Statu quo':>12} {'Sc. équil.':>12}", "-"*44,
        f"{'Inclusion I':<18} {histories[0]['I'][-1]:>12.3f} {histories[1]['I'][-1]:>12.3f}",
        f"{'Soutenabilité S':<18} {histories[0]['S'][-1]:>12.3f} {histories[1]['S'][-1]:>12.3f}",
        f"{'Confiance T':<18} {histories[0]['T'][-1]:>12.3f} {histories[1]['T'][-1]:>12.3f}",
        f"{'Risque R':<18} {histories[0]['R'][-1]:>12.3f} {histories[1]['R'][-1]:>12.3f}",
        f"{'Gouvernance G':<18} {histories[0]['G'][-1]:>12.3f} {histories[1]['G'][-1]:>12.3f}",
        "", "Paramètres initiaux :",
        "  I₀=0,33 | S₀=0,40 | T₀=0,45",
        "  X_t=0,78 (statu quo)",
        "  X_t : 0,78→0,45 (sc. équilibré)",
    ]
    ax_s.text(0.05, 0.95, "\n".join(lines), transform=ax_s.transAxes,
              fontsize=8, verticalalignment='top', fontfamily='monospace',
              bbox=dict(boxstyle='round', facecolor='#f0f4f8', alpha=0.8))

    fig.text(0.5, -0.02,
        "Source : simulation du modèle dynamique G(t), code Python Annexe A & Annexe E. "
        "Conditions initiales estimées — ITU, World Bank, GSMA (2023-2024).",
        ha='center', fontsize=7.5, color='#555555', style='italic')

    plt.tight_layout()
    path = OUTPUT_DIR + "Figure_6_3_cas_Comores.png"
    if save:
        plt.savefig(path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"  Figure 6.3 sauvegardée : {path}")
    plt.close()


# =============================================================================
# POINT D'ENTRÉE PRINCIPAL
# =============================================================================

def main():
    print("=" * 65)
    print("ANNEXE E — Génération de toutes les figures de la thèse")
    print("Karim Attoumani Mohamed & Jérôme Velo")
    print("Université de Toamasina, 2025")
    print("=" * 65)

    print("\n── Chapitre 3 ──────────────────────────────────────────────")
    generate_figure_3_1()
    generate_figure_3_2()

    print("\n── Chapitre 4 ──────────────────────────────────────────────")
    generate_figure_4_1()
    generate_figure_4_2()

    print("\n── Chapitre 5 ──────────────────────────────────────────────")
    generate_figure_5_1()

    print("\n── Chapitre 6 ──────────────────────────────────────────────")
    generate_figure_6_1()
    generate_figure_6_2()
    generate_figure_6_3()

    print("\n" + "=" * 65)
    print("8 figures générées avec succès.")
    print("Fichiers PNG (300 dpi) disponibles dans :", OUTPUT_DIR)
    print("=" * 65)


if __name__ == "__main__":
    main()
