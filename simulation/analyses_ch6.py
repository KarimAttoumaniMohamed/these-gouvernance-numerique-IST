"""Analyses de robustesse du chapitre 6 (thèse, sections 6.1.8, 6.2.1, 6.2.3 et 6.3.2).
À placer dans ist/simulation/ à côté de generate_figures.py ; lancer : python analyses_ch6.py
Tous les tirages utilisent la graine 2026 : les résultats sont reproductibles."""
import itertools, dataclasses
import numpy as np
from generate_figures import ModelParameters, ScenarioConfig, _build_4_scenarios, _risk, _G, _trust_decay

BASE = ModelParameters()
NAMES = [f.name for f in dataclasses.fields(ModelParameters)]
SC4 = _build_4_scenarios(20)

def run(sc, p, T=20, c1=0.0, c2=0.0):
    """Équations (2.3), (2.4), (6.1)-(6.3). c1, c2 : variante couplée (liens I -> S)."""
    I, S, Tt = sc.I0, sc.S0, sc.T0
    G = []
    for t in range(T):
        A = sc.A_profile[min(t, len(sc.A_profile) - 1)]
        X = sc.X_profile[min(t, len(sc.X_profile) - 1)]
        R = _risk(I, S, Tt, A, X, p); G.append(_G(I, S, Tt, R, p))
        dI = p.c_T_to_I * Tt + p.c_S_to_I * max(0.0, p.S_critical - S) + (p.c_pi if sc.pi_active else 0.0)
        Sn = np.clip(S + p.c_A_to_S * A + (p.c_inv_S if sc.inv_S_active else 0.0)
                     - c1 * I * A + (c2 * I if sc.inv_S_active else 0.0), 0, 1)
        Tn = np.clip(_trust_decay(Tt, R, p) + p.c_S_to_T * Sn + (p.c_M_to_T if sc.M_active else 0.0)
                     + p.c_X_to_T * X, 0, 1)
        I, S, Tt = np.clip(I + dI, 0, 1), Sn, Tn
    return np.array(G)

def props(p, c1=0.0, c2=0.0):
    G = [run(sc, p, 20, c1, c2) for sc in SC4]
    p1 = G[0][-1] < G[0][0] and G[1][-1] < G[1][0]
    p2 = G[2][-1] > G[2][0] and G[3][-1] > G[3][0]
    p3 = sorted(range(4), key=lambda i: -G[i][-1])[:2] == [2, 3]
    return p1, p2, p3

def main():
    rng = np.random.default_rng(2026)
    assert all(props(BASE))
    # 1. un paramètre à la fois
    oat = [all(props(dataclasses.replace(BASE, **{n: getattr(BASE, n) * f}))) for n in NAMES for f in (0.5, 1.5)]
    print(f"1. Un à la fois : {sum(oat)}/{len(oat)} simulations conservent les trois propriétés")
    # 2. Monte-Carlo simultané
    N = 2000; rows = []; explained = 0
    for _ in range(N):
        p = dataclasses.replace(BASE, **{n: getattr(BASE, n) * rng.uniform(0.5, 1.5) for n in NAMES})
        r = props(p); rows.append(r)
        if not r[1] and p.c_inv_S < -p.c_A_to_S * 0.5: explained += 1
    r = np.array(rows)
    print(f"2. Monte-Carlo simultané (N={N}) : P1 {r[:,0].mean():.3f} P2 {r[:,1].mean():.3f} "
          f"P3 {r[:,2].mean():.3f} ; les trois : {r.all(1).mean():.3f}")
    print(f"   échecs P1 {(~r[:,0]).sum()}, P2 {(~r[:,1]).sum()} (dont expliqués par la condition (iii) : {explained}), P3 {(~r[:,2]).sum()}")
    # 3. variante couplée
    grid = [all(props(BASE, c1, c2)) for c1 in np.linspace(0, 0.12, 7) for c2 in np.linspace(0, 0.06, 7)]
    print(f"3. Variante couplée, grille : {sum(grid)}/{len(grid)}")
    rc = []
    for _ in range(N):
        p = dataclasses.replace(BASE, **{n: getattr(BASE, n) * rng.uniform(0.5, 1.5) for n in NAMES})
        rc.append(all(props(p, rng.uniform(0, 0.12), rng.uniform(0, 0.06))))
    print(f"   Variante couplée + Monte-Carlo (N={N}) : {np.mean(rc):.3f}")
    # 4. plan factoriel des leviers
    ctxs = {"scénario 4": (0.5, 0.55, 0.55, [0.5] * 20, [max(0.40, 0.70 - 0.015 * t) for t in range(20)]),
            "Comores": (0.33, 0.40, 0.45, [min(0.65, 0.25 + 0.02 * t) for t in range(25)],
                        [max(0.45, 0.80 - 0.015 * t) for t in range(25)])}
    for nom, (I0, S0, T0, A, X) in ctxs.items():
        y = {k: run(ScenarioConfig('f', I0, S0, T0, A, X, *map(bool, k), '', ''), BASE, len(A))[-1]
             for k in itertools.product((0, 1), repeat=3)}
        g0 = y[(0, 0, 0)]
        print(f"4. Leviers ({nom}) : aucun {g0:.3f} ; π seul {y[(1,0,0)]-g0:+.3f} ; ν seul {y[(0,1,0)]-g0:+.3f} ; "
              f"M seul {y[(0,0,1)]-g0:+.3f} ; ν+M {y[(0,1,1)]-g0:+.3f} ; π+ν+M {y[(1,1,1)]-g0:+.3f}")
    # 5. valeurs initiales des Comores
    A = [min(0.65, 0.25 + 0.02 * t) for t in range(25)]
    ok = 0; tot = 0
    for I0, S0, T0, X0 in itertools.product((0.10, 0.20, 0.33), (0.35, 0.40, 0.45), (0.05, 0.25, 0.45), (0.70, 0.80, 0.85)):
        sq = run(ScenarioConfig('sq', I0, S0, T0, A, [X0] * 25, False, False, False, '', ''), BASE, 25)
        eq = run(ScenarioConfig('eq', I0, S0, T0, A, [max(0.45, X0 - 0.015 * t) for t in range(25)], True, True, True, '', ''), BASE, 25)
        tot += 1; ok += sq[-1] < 0 < eq[-1]
    print(f"5. Comores, valeurs initiales : {ok}/{tot} combinaisons avec G final < 0 (statu quo) et > 0 (gouvernance équilibrée)")

if __name__ == "__main__":
    main()
