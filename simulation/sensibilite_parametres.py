"""
Analyse de sensibilité « un paramètre à la fois » du modèle I-S-T (chapitre 6, § 6.1.8).

Chacun des 21 paramètres de ModelParameters est multiplié par 0,5 puis par 1,5
(42 simulations des quatre scénarios). Le script vérifie trois propriétés :
  1. G finit sous sa valeur initiale dans les scénarios 1 et 2 ;
  2. G finit au-dessus de sa valeur initiale dans les scénarios 3 et 4 ;
  3. les scénarios 3 et 4 sont les deux mieux classés en fin de simulation.

À placer dans ist/simulation/, à côté de generate_figures.py, puis lancer :
    python sensibilite_parametres.py
"""
import dataclasses
from generate_figures import ModelParameters, run_simulation_G, _build_4_scenarios

PARAMS = [f.name for f in dataclasses.fields(ModelParameters)]
SCENARIOS = _build_4_scenarios(20)


def proprietes(p):
    G = [run_simulation_G(sc, p, 20)['G'] for sc in SCENARIOS]
    baisse_1_2 = G[0][-1] < G[0][0] and G[1][-1] < G[1][0]
    hausse_3_4 = G[2][-1] > G[2][0] and G[3][-1] > G[3][0]
    tete_3_4 = sorted(range(4), key=lambda i: -G[i][-1])[:2] == [2, 3]
    return baisse_1_2, hausse_3_4, tete_3_4, [round(g[-1], 3) for g in G]


def main():
    print("Référence :", proprietes(ModelParameters()))
    echecs = 0
    for nom in PARAMS:
        for f in (0.5, 1.5):
            p = ModelParameters()
            setattr(p, nom, getattr(p, nom) * f)
            b12, h34, t34, Gfin = proprietes(p)
            ok = b12 and h34 and t34
            echecs += not ok
            print(f"{nom:12s} x{f:<4}  {'OK ' if ok else 'ÉCHEC'}  G final = {Gfin}")
    print(f"\n{2 * len(PARAMS)} simulations, {echecs} échec(s).")


if __name__ == "__main__":
    main()
