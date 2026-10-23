"""English version of Figure 5.1 (thesis): DTI, equations 5.2 to 5.4. Same computation as ../figure_5_1_dti.py; labels translated."""
import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from dti import GAMMA,DELTA,KAPPA,RC
LS=0.75
def curves(Sb,R):
    T=Sb**GAMMA-(R**DELTA+LS*R**2)/(1+LS); f=np.exp(-KAPPA*np.maximum(0,R-RC))
    return T, -1+(1+T)*f, T*f
R=np.linspace(0,1,1001)
fig,ax=plt.subplots(3,1,figsize=(6.8,10),dpi=250)
a=ax[0]
for Sb,c,lab in [(0.70,'#2ca02c','UAMINIFU, S̄ = 0.70'),(0.45,'#ff7f0e','UAMINIFU, S̄ = 0.45')]:
    T,D,_=curves(Sb,R); a.plot(R,D,color=c,lw=2.4,label=lab)
a.plot(R,0.70-R,'--',color='#1f77b4',lw=1.8,label='Linear model (S̄ − R̄), S̄ = 0.70')
a.axvline(RC,color='#d62728',ls='--',lw=1.6,label='Critical threshold Rc = 0.62'); a.axhline(-1,color='k',lw=.8,ls=':'); a.axhline(0,color='grey',lw=.6)
for x,y,t,dx,dy in [(0.125,0.630,'Scenario B',0.03,0.08),(0.708,-0.536,'Scenario A',-0.07,-0.25),(0.889,-0.908,'Comoros',-0.04,0.12)]:
    a.plot(x,y,'o',color='k',ms=5); a.annotate(t,(x,y),(x+dx,y+dy),fontsize=8.5)
a.set_xlim(0,1); a.set_ylim(-1.1,1.0); a.set_title('(a) Trust index as a function of mean risk',fontsize=10.5); a.set_ylabel('DTI'); a.set_xlabel('Mean risk R̄'); a.grid(alpha=.3); a.legend(fontsize=7.5,loc='lower left')
a=ax[1]
T,D,old=curves(0.45,R)
a.plot(R,old,'-.',color='#9467bd',lw=2.2,label='Multiplicative decay T·e^(−κ(R̄−Rc)⁺)')
a.plot(R,D,color='#ff7f0e',lw=2.4,label='Decay towards the floor (equation 5.3)')
a.axvline(RC,color='#d62728',ls='--',lw=1.4); a.axhline(-1,color='k',lw=.8,ls=':'); a.axhline(0,color='grey',lw=.6)
a.set_xlim(0.4,1); a.set_ylim(-1.1,0.3); a.set_title('(b) Multiplicative decay and decay towards the floor (S̄ = 0.45)',fontsize=10.5); a.set_ylabel('DTI'); a.set_xlabel('Mean risk R̄'); a.grid(alpha=.3); a.legend(fontsize=7.5,loc='lower left')
a.annotate('negative score pulled back towards 0\nas risk increases',(0.9,old[900]),(0.66,0.12),fontsize=7.5,color='#9467bd',arrowprops=dict(arrowstyle='->',color='#9467bd'))
a=ax[2]
T,D,_=curves(0.70,R); tau=(1+D)/2; C=0.5+0.8/tau**1.4
a.plot(R,D,color='#2ca02c',lw=2.4,label='DTI (left axis)'); a.axvline(RC,color='#d62728',ls='--',lw=1.4,label='Rc = 0.62')
a.set_ylim(-1.1,1); a.set_ylabel('DTI',color='#2ca02c'); a.set_xlabel('Mean risk R̄'); a.grid(alpha=.3); a.set_xlim(0,1)
b=a.twinx(); b.plot(R,C,'--',color='#8c564b',lw=2,label='Transaction cost (right axis)'); b.set_ylim(0,15); b.set_ylabel('Transaction cost',color='#8c564b')
h1,l1=a.get_legend_handles_labels(); h2,l2=b.get_legend_handles_labels(); a.legend(h1+h2,l1+l2,fontsize=7.5,loc='upper right')
a.set_title('(c) Trust and transaction cost (S̄ = 0.70)',fontsize=10.5)
plt.tight_layout(); plt.savefig('Figure_5_1_DTI.png',dpi=250); plt.savefig('Figure_5_1_DTI.svg')
print('ok', float(old[900]), float(D[900]))
