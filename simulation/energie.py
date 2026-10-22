"""Chapitre 4 : demande liée à l'IA en Afrique en 2030, sans double projection.
Demande = utilisateurs × taux d'adoption × requêtes par utilisateur IA × consommation par requête."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
U=600e6; PROD=965e3/365   # GWh/jour (965 TWh en 2024, Ember)
E25=(0.24,0.30); E23=(2.9,5.0); MO=(2.0,5.0); CI=0.456   # kgCO2e/kWh, implicite dans l'article (50 Mt pour 300 GWh/j)
PROFILS=[("Faible",0.25,10),("Intermédiaire",0.50,30),("Intensif (hypothèse de l'article)",1.00,100)]
def req(a,q): return U*a*q
def gwh(n,e): return n*e/1e9            # Wh -> GWh
def po(n,mo): return n*mo/1e9            # Mo -> Po
def mt(g): return g*365*1e6*CI/1e9       # GWh/j -> Mt/an
if __name__=='__main__':
    for nom,a,q in PROFILS:
        n=req(a,q)
        e25=[gwh(n,e) for e in E25]; e23=[gwh(n,e) for e in E23]
        print(f"{nom:35s} req/j {n/1e9:5.1f} Md | 2025 {e25[0]:.2f}-{e25[1]:.2f} GWh ({100*e25[0]/PROD:.2f}-{100*e25[1]/PROD:.2f} %) "
              f"| 2023 {e23[0]:.1f}-{e23[1]:.1f} GWh ({100*e23[0]/PROD:.1f}-{100*e23[1]/PROD:.1f} %) | BP {po(n,MO[0]):.0f}-{po(n,MO[1]):.0f} Po "
              f"| CO2 2025 {mt(e25[0]):.2f}-{mt(e25[1]):.2f} Mt, 2023 {mt(e23[0]):.1f}-{mt(e23[1]):.1f} Mt")
    print('web',gwh(U*100,0.02),'GWh', po(U*100,0.5),'Po','prod',PROD)
    a=np.linspace(0.05,1,200)
    fig,ax=plt.subplots(3,1,figsize=(7.1,10),dpi=250)
    cols={10:'#2ca02c',30:'#ff7f0e',100:'#d62728'}
    x=ax[0]
    for q,c in cols.items():
        x.fill_between(a*100,gwh(U*a*q,E23[0]),gwh(U*a*q,E23[1]),color=c,alpha=0.25,label=f'{q} req./j, hypothèse haute (2,9 à 5 Wh)')
    for q,c in cols.items():
        x.fill_between(a*100,gwh(U*a*q,E25[0]),gwh(U*a*q,E25[1]),color=c,alpha=0.75,label=f'{q} req./j, hypothèse basse (0,24 à 0,3 Wh)')
    x.axhline(1.2,color='k',ls=':',lw=1.2); x.text(6,1.35,'Web : 100 clics par jour (1,2 GWh)',fontsize=7.5)
    x.axhline(PROD*0.01,color='#7f7f7f',ls='--',lw=1.2); x.text(6,PROD*0.0113,'1 % de la production électrique africaine',fontsize=7.5,color='#555')
    x.set_yscale('log'); x.set_xlim(5,100); x.set_xlabel("Part des 600 millions d'utilisateurs qui recourent à l'IA (%)"); x.set_ylabel('GWh par jour')
    x.set_title("(a) Demande d'électricité en 2030 selon l'adoption et l'hypothèse de consommation par requête",fontsize=9); x.grid(alpha=.3,which='both'); x.legend(fontsize=6.3,loc='lower right',ncol=2)
    x=ax[1]
    labs=[p[0].split(' (')[0] for p in PROFILS]; xs=np.arange(3)
    s25=[100*gwh(req(a_,q),E25[1])/PROD for _,a_,q in PROFILS]; s23=[100*gwh(req(a_,q),E23[1])/PROD for _,a_,q in PROFILS]
    s25l=[100*gwh(req(a_,q),E25[0])/PROD for _,a_,q in PROFILS]; s23l=[100*gwh(req(a_,q),E23[0])/PROD for _,a_,q in PROFILS]
    x.bar(xs-0.18,s23,0.34,color='#d62728',alpha=0.35,label='Hypothèse haute : 2,9 à 5 Wh par requête (estimations publiées en 2023)')
    x.bar(xs+0.18,s25,0.34,color='#1f77b4',alpha=0.8,label='Hypothèse basse : 0,24 à 0,3 Wh par requête (mesures publiées en 2025)')
    for i in range(3):
        x.text(xs[i]-0.18,s23[i]*1.15,f'{s23l[i]:.1f}–{s23[i]:.1f} %'.replace('.',','),ha='center',fontsize=7)
        x.text(xs[i]+0.18,s25[i]*1.15,f'{s25l[i]:.2f}–{s25[i]:.2f} %'.replace('.',','),ha='center',fontsize=7)
    x.set_yscale('log'); x.set_ylim(0.005,40); x.set_xticks(xs); x.set_xticklabels([f'{l}\n(adoption {int(a_*100)} %, {q} req./j)' for l,(_,a_,q) in zip(labs,PROFILS)],fontsize=7.5)
    x.set_ylabel('% de la production'); x.set_title("(b) Part de la production électrique africaine absorbée en 2030, selon le profil d'usage",fontsize=9); x.grid(alpha=.3,axis='y',which='both'); x.legend(fontsize=7,loc='upper left')
    x=ax[2]
    for q,c in cols.items():
        x.fill_between(a*100,po(U*a*q,MO[0]),po(U*a*q,MO[1]),color=c,alpha=0.45,label=f'{q} requêtes par jour')
    x.axhline(30,color='k',ls=':',lw=1.2); x.text(6,33,'Web : 100 clics par jour (30 Po)',fontsize=7.5)
    x.set_xlim(5,100); x.set_yscale('log'); x.set_xlabel("Part des 600 millions d'utilisateurs qui recourent à l'IA (%)"); x.set_ylabel('Po par jour')
    x.set_title('(c) Volume de données en 2030 (2 à 5 Mo par requête, quelle que soit l\'hypothèse d\'énergie)',fontsize=9); x.grid(alpha=.3,which='both'); x.legend(fontsize=7.5,loc='lower right')
    plt.tight_layout(); plt.savefig('Figure_4_1_demande_IA.png',dpi=250); plt.savefig('Figure_4_1_demande_IA.svg')
