"""English version of Figure 6.4 (thesis): the case of the Comoros. Same simulation as ../figure_6_4_comores.py; labels translated."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import generate_figures as g
p=g.ModelParameters(); T=25
A=[min(0.65,0.25+0.02*t) for t in range(T)]
sq=g.run_simulation_G(g.ScenarioConfig("SQ",.33,.40,.45,A,[0.80]*T,False,False,False,'#d62728','--'),p,T)
s4=g.run_simulation_G(g.ScenarioConfig("S4",.33,.40,.45,A,[max(0.45,0.80-0.015*t) for t in range(T)],True,True,True,'#1f77b4','-'),p,T)
fig,ax=plt.subplots(3,2,figsize=(7.47,10),dpi=250)
pan=[('I','(a) Inclusion'),('S','(b) Sustainability'),('T','(c) Trust'),('R','(d) Systemic risk'),('G','(e) Governance')]
t=range(T)
for k,(v,tt) in enumerate(pan):
    a=ax.flat[k]
    a.plot(t,sq[v],'--',color='#d62728',lw=2.2); a.plot(t,s4[v],'-',color='#1f77b4',lw=2.2)
    a.set_title(tt,fontsize=11); a.set_xlabel('Period (t)',fontsize=9); a.set_xlim(0,T-1); a.grid(alpha=.3)
    if v=='S': a.axhline(.40,color='orange',ls=':',lw=1.2); a.text(T-1.3,.41,'S_c = 0.40',ha='right',color='#c05a00',fontsize=9)
    if v=='R': a.axhline(.62,color='k',ls=':',lw=1.2); a.text(T-1.3,.595,'Rc = 0.62',ha='right',fontsize=9)
    if v=='G': a.axhline(0,color='grey',lw=.8)
ax.flat[5].axis('off')
ax.flat[5].plot([],[],'--',color='#d62728',lw=2.5,label='Status quo'); ax.flat[5].plot([],[],'-',color='#1f77b4',lw=2.5,label='Balanced governance')
ax.flat[5].legend(loc='center',frameon=False,fontsize=11,title='Union of the Comoros\nI₀ = 0.33, S₀ = 0.40, T₀ = 0.45\nX₀ = 0.80',title_fontsize=10)
plt.tight_layout(); plt.savefig('Figure_6_4_Comoros_case.png',dpi=250); plt.savefig('Figure_6_4_Comoros_case.svg')
# print([round(float(sq[k][-1]),3) for k in 'ISTRG'],[round(float(s4[k][-1]),3) for k in 'ISTRG'], round(max(s4['G']),3), int(np.argmax(s4['G'])), round(sq['R'][0],3), round(max(sq['R']),3))
