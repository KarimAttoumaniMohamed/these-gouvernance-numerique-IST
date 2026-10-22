"""DTI révisé (UAMINIFU, version de la thèse) : borné dans [-1 ; 1] et monotone."""
import math
GAMMA, DELTA, KAPPA, RC = 1.15, 1.55, 7.0, 0.62
def dti(S, R, pairs, gamma=GAMMA, delta=DELTA, kappa=KAPPA, Rc=RC):
    """S, R : listes de facteurs dans [0,1] ; pairs : liste (lambda, j, k) (indices dans R)."""
    Sb = sum(S)/len(S); Rb = sum(R)/len(R)
    L = sum(l*R[j]*R[k] for l,j,k in pairs); Ls = sum(l for l,_,_ in pairs)
    rho = (Rb**delta + L)/(1+Ls)
    T = Sb**gamma - rho
    f = math.exp(-kappa*max(0.0, Rb-Rc))
    D = -1 + (1+T)*f
    return dict(Sb=Sb, Rb=Rb, Sg=Sb**gamma, Rd=Rb**delta, L=L, Ls=Ls, rho=rho, T=T, f=f, DTI=D, tau=(1+D)/2)
def dti_means(Sb, Rb, L, Ls=0.75, **kw):
    rho=(Rb**DELTA+L)/(1+Ls); T=Sb**GAMMA-rho; f=math.exp(-KAPPA*max(0.0,Rb-RC)); D=-1+(1+T)*f
    return dict(Sb=Sb,Rb=Rb,Sg=Sb**GAMMA,Rd=Rb**DELTA,L=L,Ls=Ls,rho=rho,T=T,f=f,DTI=D,tau=(1+D)/2)
# Comores
S_com=[0.392, None, None, None, None]
S_com=[0.392,0.797,0.212,0.695,0.240]
R_com=[0.750,1.000,1.000,0.833,1.000,0.750]   # R1..R6
P_com=[(0.30,0,2),(0.20,1,2),(0.10,3,1),(0.15,0,5)]
if __name__=='__main__':
    f=lambda r:{k:round(v,4) for k,v in r.items()}
    c=dti(S_com,R_com,P_com); print('Comores',f(c))
    s1=list(S_com); s1[0]=0.037; print('S1=0.037',f(dti(s1,R_com,P_com))['DTI'])
    for r6 in (0.5,1.0):
        r=list(R_com); r[5]=r6; print('R6',r6,f(dti(S_com,r,P_com))['DTI'],f(dti(S_com,r,P_com))['T'])
    k=list(R_com); k[0]=0.25; k[5]=0.50; print('Kenya-like R1=.25 R6=.5',f(dti(S_com,k,P_com)))
    SA=[0.50,0.75,0.25,0.50,0.25]; RA=[0.75,0.75,0.50,0.75,0.50,1.00]   # scénario A (risque élevé)
    SB=[0.75,0.75,0.50,0.75,0.75]; RB=[0.25,0.00,0.25,0.00,0.25,0.00]   # scénario B (mature)
    print('Scénario A',f(dti(SA,RA,P_com))); print('Scénario B',f(dti(SB,RB,P_com)))
    print('Entrées initiales du document de travail (A, moyennes) :',f(dti_means(0.44,0.45,0.50)))
    import itertools
    vals=[dti(S_com,R_com,[(l*k,j,m) for (l,j,m),k in zip(P_com,fs)])['DTI'] for fs in itertools.product((0.5,1.5),repeat=4)]
    print('Interactions ±50 % :',round(min(vals),3),round(max(vals),3))
    for g,dl,ka,rc in [(1,1,7,.62),(1.15,1.55,3.5,.62),(1.15,1.55,14,.62),(1.15,1.55,7,.5),(1.15,1.55,7,.75)]:
        print('gamma,delta,kappa,Rc =',g,dl,ka,rc,'-> DTI',round(dti(S_com,R_com,P_com,g,dl,ka,rc)['DTI'],3))
    # monotonie : balayage
    import itertools
    ok=True
    for j in range(6):
        prev=None
        for v in [i/20 for i in range(21)]:
            r=list(R_com); r[j]=v; D=dti(S_com,r,P_com)['DTI']
            if prev is not None and D>prev+1e-12: ok=False
            prev=D
    print('monotone en chaque R_j:',ok)
