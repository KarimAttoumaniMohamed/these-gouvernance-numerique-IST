"""English versions of Figures 6.2 (four scenarios) and 6.3 (sensitivity to lambda), in the manuscript layout.
Same simulations as ../figure_6_2_6_3.py; labels translated."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import generate_figures as g
p=g.ModelParameters()
# Figure 6.2 : four scenarios (thesis layout)
T=20; sc=g._build_4_scenarios(T)
names=['Scenario 1:\nUncontrolled expansion','Scenario 2:\nTechnological dependence','Scenario 3:\nStabilisation by constraint','Scenario 4:\nBalanced governance']
H=[g.run_simulation_G(s,p,T) for s in sc]
fig,ax=plt.subplots(3,2,figsize=(7.47,10),dpi=250)
pan=[('I','(a) Inclusion'),('S','(b) Sustainability'),('T','(c) Trust'),('R','(d) Systemic risk'),('G','(e) Governance')]
t=range(T)
for k,(v,tt) in enumerate(pan):
    a=ax.flat[k]
    for s,h in zip(sc,H): a.plot(t,h[v],s.linestyle,color=s.color,lw=2.2)
    a.set_title(tt,fontsize=11); a.set_xlabel('Period (t)',fontsize=9); a.set_xlim(0,T-1); a.grid(alpha=.3)
    if v=='S': a.axhline(.40,color='orange',ls=':',lw=1.2); a.text(T-1.3,.42,'S_c = 0.40',ha='right',color='#c05a00',fontsize=9)
    if v=='R': a.axhline(.62,color='k',ls=':',lw=1.2); a.text(T-1.3,.635,'Rc = 0.62',ha='right',fontsize=9)
    if v=='G': a.axhspan(.3,.7,color='green',alpha=.08); a.axhline(0,color='grey',lw=.8)
L=ax.flat[5]; L.axis('off')
for s,n in zip(sc,names): L.plot([],[],s.linestyle,color=s.color,lw=2.5,label=n)
L.fill_between([],[],[],color='green',alpha=.15,label='Indicative band\n0.3 < G < 0.7')
L.legend(loc='center',frameon=False,fontsize=10,labelspacing=1.0)
plt.tight_layout(); plt.savefig('Figure_6_2_four_scenarios.png',dpi=250); plt.savefig('Figure_6_2_four_scenarios.svg'); plt.close()
# Figure 6.3 : sensitivity to lambda
lams=[10,25,40,60,80,100]; cols=['#1a9850','#91cf60','#fdae61','#f46d43','#d73027','#7f0000']; sty=['-','-','-','--','-.',':']
fig,ax=plt.subplots(2,1,figsize=(8.82,10),dpi=250)
for i,l in enumerate(lams):
    A=min(1.0,0.3*l/10)
    h=g.run_simulation_G(g.ScenarioConfig(f'λ = {l}',0.35,0.42,0.45,[A]*T,[0.75]*T,False,False,False,cols[i],sty[i]),p,T)
    lab=f'λ = {l}'+('  (saturated intensity)' if A>=1 else '')
    ax[0].plot(range(T),h['S'],sty[i],color=cols[i],lw=2.2,label=lab); ax[1].plot(range(T),h['G'],sty[i],color=cols[i],lw=2.2,label=lab)
ax[0].axhline(.40,color='red',ls='--',lw=1.3,alpha=.8,label='Critical threshold S_c = 0.40')
for a,tt,yl in zip(ax,['(a) Sustainability as a function of λ','(b) Governance as a function of λ'],['Sustainability','Governance']):
    a.set_title(tt,fontsize=11); a.set_xlabel('Period (t)',fontsize=10); a.set_ylabel(yl,fontsize=10); a.legend(fontsize=10,loc='upper right'); a.grid(alpha=.3); a.set_xlim(0,T-1)
plt.tight_layout(); plt.savefig('Figure_6_3_lambda_sensitivity.png',dpi=250); plt.savefig('Figure_6_3_lambda_sensitivity.svg'); plt.close()
print('ok')
