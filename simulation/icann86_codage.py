"""Codage I-S-T des 25 sessions de l'ICANN86 Policy Forum (thèse, section 6.3.7 et Annexe C).

Unité de comptage : un segment de transcription (ligne de texte d'un sous-titre VTT, sans le nom de
l'orateur) est compté une fois pour une variable s'il contient au moins un mot-clé de cette variable.
Deux règles d'appariement sont disponibles :
  - « sous-chaine » : recherche de la chaîne, insensible à la casse (règle des comptages de la thèse) ;
  - « mot » : mot entier, pluriel accepté (évite par exemple « server » dans « observer »).

Usage :
  python icann86_codage.py                      # synthèse par communauté depuis data/icann86_sessions.csv
  python icann86_codage.py --transcripts DOSSIER  # recalcule les comptages depuis les fichiers .vtt
                                                  # (les fichiers en double sont ignorés) et réécrit le CSV

Les transcriptions (format VTT) sont celles des enregistrements Zoom publiés par l'ICANN pour chaque
session (https://icann86.sched.com/list/simple) ; elles ne sont pas redistribuées dans ce dépôt.
"""
import argparse, csv, glob, hashlib, os, re
from decimal import Decimal, ROUND_HALF_UP


def arr(x, d=1):
    """Arrondi au plus proche, demi vers le haut (16,25 -> 16,3)."""
    return Decimal(str(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)

KW = {
    'I': ['inclusion', 'participation', 'diversity', 'linguistic', 'representation', 'Global South',
          'developing', 'underrepresented', 'equity', 'barrier', 'gap', 'access'],
    'S': ['energy', 'bandwidth', 'infrastructure', 'capacity', 'sustainability', 'environmental',
          'carbon', 'server', 'data center', 'electricity', 'cost', 'resource'],
    'T': ['trust', 'security', 'abuse', 'DNS abuse', 'privacy', 'data protection', 'WHOIS', 'RDAP',
          'cybersecurity', 'credential', 'confidence', 'reliability', 'integrity'],
}
REGLES = {
    'sous-chaine': lambda k: re.escape(k),
    'mot': lambda k: r'\b' + re.escape(k) + r'(?:s|es|ies)?\b',
}
ICI = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(ICI, '..', 'data', 'icann86_sessions.csv')


def segments(chemin):
    """Lignes de texte d'un fichier VTT, sans numéros, horodatages ni nom de l'orateur."""
    out = []
    for bloc in open(chemin, encoding='utf8', errors='ignore').read().split('\n\n'):
        for l in bloc.strip().split('\n'):
            if not l or l == 'WEBVTT' or '-->' in l or re.fullmatch(r'\d+', l):
                continue
            out.append(l.split(':', 1)[1] if ':' in l else l)
    return out


def coder(chemin, regle):
    rx = {v: [re.compile(REGLES[regle](k), re.I) for k in ks] for v, ks in KW.items()}
    n = dict.fromkeys('IST', 0)
    for seg in segments(chemin):
        for v in 'IST':
            n[v] += any(r.search(seg) for r in rx[v])
    return n


def recalculer(dossier):
    lignes, vus = {}, set()
    for f in sorted(glob.glob(os.path.join(dossier, '**', '*.vtt'), recursive=True)):
        h = hashlib.md5(open(f, 'rb').read()).hexdigest()
        if h in vus or os.path.basename(f).startswith('._'):
            continue
        vus.add(h)
        lignes[os.path.basename(f)[:18]] = (coder(f, 'sous-chaine'), coder(f, 'mot'))
    meta = list(csv.DictReader(open(CSV, encoding='utf8')))
    for r in meta:
        a, b = lignes[r['enregistrement']]
        r.update(I=a['I'], S=a['S'], T=a['T'], I_mot=b['I'], S_mot=b['S'], T_mot=b['T'])
    with open(CSV, 'w', encoding='utf8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=meta[0].keys()); w.writeheader(); w.writerows(meta)
    print(f'{len(lignes)} sessions distinctes recodées -> data/icann86_sessions.csv')


def synthese():
    rows = list(csv.DictReader(open(CSV, encoding='utf8')))
    for suffixe, nom in [('', 'règle « sous-chaine » (comptages de la thèse, Annexe C)'),
                         ('_mot', 'règle « mot » (mots entiers, variante de contrôle)')]:
        print(f'\nSynthèse inter-communautés, {nom}')
        print(f"{'Communauté':<11}{'Sessions':>9}{'I':>6}{'S':>6}{'T':>6}{'Total':>7}{'I%':>6}{'S%':>6}{'T%':>6}"
              f"{'I/sess.':>9}{'S/sess.':>9}{'T/sess.':>9}")
        tot = [0, 0, 0, 0]
        for c in ['ccNSO', 'At-Large', 'GAC', 'TOTAL']:
            if c == 'TOTAL':
                n, i, s, t = tot
            else:
                rs = [r for r in rows if r['communaute'] == c]
                n = len(rs); i, s, t = (sum(int(r[v + suffixe]) for r in rs) for v in 'IST')
                tot = [tot[0] + n, tot[1] + i, tot[2] + s, tot[3] + t]
            a = i + s + t
            print(f'{c:<11}{n:>9}{i:>6}{s:>6}{t:>6}{a:>7}{arr(100*i/a):>5}%{arr(100*s/a):>5}%{arr(100*t/a):>5}%'
                  f'{arr(i/n):>9}{arr(s/n):>9}{arr(t/n):>9}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--transcripts', help='dossier contenant les fichiers .vtt des sessions')
    a = ap.parse_args()
    if a.transcripts:
        recalculer(a.transcripts)
    synthese()
