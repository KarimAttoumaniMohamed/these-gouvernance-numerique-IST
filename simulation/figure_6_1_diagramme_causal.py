"""Figure 6.1 de la thèse : diagramme causal du modèle I-S-T (liens simulés en trait plein, liens postulés en pointillés)."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np
from matplotlib.patches import FancyArrowPatch, Ellipse, FancyBboxPatch, Arc
plt.rcParams['font.family']='DejaVu Serif'
fig,ax=plt.subplots(figsize=(13,8.4)); ax.set_xlim(-2.7,10.1); ax.set_ylim(-3.0,5.4); ax.axis('off')
SH={}  # shape info
def ell(k,x,y,txt,w,h,lw):
    ax.add_patch(Ellipse((x,y),w,h,fc='white',ec='black',lw=lw,zorder=3)); ax.text(x,y,txt,ha='center',va='center',fontsize=13,zorder=4)
    SH[k]=('e',np.array([x,y]),w/2,h/2)
def box(k,x,y,txt,w,h):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.05',fc='#f2f2f2',ec='#555555',lw=1,zorder=3))
    ax.text(x,y,txt,ha='center',va='center',fontsize=10.5,color='#222222',zorder=4)
    SH[k]=('b',np.array([x,y]),w/2+0.05,h/2+0.05)
ell('I',0.6,3.2,'Inclusion\nI',1.9,1.0,2.2); ell('S',5.6,3.2,'Soutenabilité\nS',2.3,1.0,2.2)
ell('T',1.6,0.0,'Confiance\nT',1.9,1.0,2.2); ell('R',4.9,0.0,'Risque\nsystémique R',2.3,1.0,1.6)
box('A',8.6,1.6,"Intensité d'usage\nde l'IA, A\n(exogène)",1.7,0.9)
box('X',8.6,-1.6,"Dépendance\nexterne, X\n(exogène)",1.7,0.9)
box('INV',5.6,4.85,"Investissements,\narchitectures frugales",2.4,0.62)
box('PI',0.6,4.85,"Politiques\nd'inclusion π",1.7,0.62)
box('M',-1.7,-1.4,"Audit et\ntransparence M",1.75,0.62)
box('U',1.6,-2.35,"Gouvernance\nmultipartite U",1.75,0.62)
def bound(k,v):
    t,c,a,b=SH[k]; v=v/np.linalg.norm(v)
    if t=='e': s=1/np.sqrt((v[0]/a)**2+(v[1]/b)**2)
    else: s=min(a/abs(v[0]) if v[0] else 1e9, b/abs(v[1]) if v[1] else 1e9)
    return c+v*s
def edge(a,b,sign,rad=0.0,dashed=False,col='black',t=0.78,off=0.24):
    ca,cb=SH[a][1],SH[b][1]
    mid=(ca+cb)/2; d=cb-ca; ctrl=mid+rad*np.array([d[1],-d[0]])
    pa=bound(a,ctrl-ca if rad else d); pb=bound(b,ctrl-cb if rad else -d)
    # keep same curvature: recompute rad for new endpoints so control stays similar
    d2=pb-pa; m2=(pa+pb)/2; n2=np.array([d2[1],-d2[0]])
    r2=np.dot(ctrl-m2,n2)/np.dot(n2,n2) if rad else 0.0
    ax.add_patch(FancyArrowPatch(pa,pb,arrowstyle='-|>',mutation_scale=17,lw=1.6,color=col,
        connectionstyle=f'arc3,rad={r2}',shrinkA=1,shrinkB=1,zorder=5,linestyle=(0,(5,3)) if dashed else '-'))
    c=m2+r2*n2; q=(1-t)**2*pa+2*(1-t)*t*c+t**2*pb
    tan=2*(1-t)*(c-pa)+2*t*(pb-c); nn=np.array([-tan[1],tan[0]]); nn/=np.linalg.norm(nn)
    p=q+off*nn
    ax.text(p[0],p[1],sign,fontsize=16,ha='center',va='center',color=col,fontweight='bold',zorder=6,
            bbox=dict(boxstyle='circle,pad=0.05',fc='white',ec='none'))
G='#444444'; DG='#555555'
edge('S','I','+',t=0.82,off=0.25)
edge('I','S','−',rad=0.20,dashed=True,col=DG,t=0.5,off=0.24)
edge('I','S','+',rad=-0.42,dashed=True,col=DG,t=0.82,off=0.25)
edge('S','T','+',t=0.45,off=0.25)
edge('T','I','+',t=0.84,off=-0.25)
edge('I','R','+',t=0.4,off=-0.25)
edge('S','R','−',t=0.8,off=0.25)
edge('T','R','−',rad=-0.30,t=0.5,off=0.24)
edge('R','T','−',rad=-0.30,t=0.5,off=0.24)
edge('A','S','−',t=0.75,off=-0.25)
edge('A','R','+',t=0.78,off=0.25)
edge('X','R','+',t=0.75,off=-0.25)
edge('X','T','−',rad=-0.20,t=0.45,off=-0.26)
edge('INV','S','+',col=G,off=0.22,t=0.6)
edge('PI','I','+',col=G,off=0.22,t=0.6)
edge('M','T','+',col=G,t=0.7)
edge('U','T','+',dashed=True,col=DG,off=0.22,t=0.6)
edge('T','X','−',rad=0.30,dashed=True,col=DG,t=0.5,off=-0.27)
ax.text(3.1,3.42,'S → I : sous le seuil S$_c$',ha='center',fontsize=9.5,color='#333333',zorder=7,bbox=dict(fc='white',ec='none',pad=1))
ax.text(3.1,2.3,'pression des usages (postulée)',ha='center',fontsize=9.5,color=DG,style='italic',zorder=7,bbox=dict(fc='white',ec='none',pad=1))
ax.text(3.1,4.42,'L2 (postulée)',ha='center',fontsize=9.5,color=DG,style='italic',zorder=7,bbox=dict(fc='white',ec='none',pad=1))
ax.text(5.5,-2.5,'L3 (postulée)',ha='center',fontsize=9.5,color=DG,style='italic')
ax.text(1.6,-2.85,'(non modélisé)',ha='center',fontsize=9,color=DG,style='italic')
def loop(x,y,txt):
    ax.add_patch(Arc((x,y),0.8,0.8,theta1=50,theta2=340,lw=1.5,color='black',zorder=6))
    ax.annotate('',xy=(x+0.27,y+0.29),xytext=(x+0.36,y+0.13),arrowprops=dict(arrowstyle='-|>',color='black',lw=1.3,mutation_scale=11),zorder=6)
    ax.text(x,y,txt,ha='center',va='center',fontsize=12.5,fontweight='bold',zorder=7)
loop(2.05,1.05,'B1'); loop(3.25,0.0,'R1')
ax.text(3.5,-0.93,'(au-delà de R$_c$)',fontsize=9.5,va='center',color='#222222',zorder=7,bbox=dict(fc='white',ec='none',pad=0.5))
lx,ly=7.25,5.3
ax.text(lx,ly,'Lecture',fontsize=10.5,fontweight='bold',va='top')
items=[('——','lien présent dans le modèle simulé'),('- - -','lien postulé, absent du modèle simulé'),('+','variation dans le même sens'),('−','variation en sens inverse'),('B / R','boucle d\'équilibrage / de renforcement')]
for i,(s,tx) in enumerate(items):
    ax.text(lx,ly-0.3*(i+1),s,fontsize=10,va='top',fontweight='bold'); ax.text(lx+0.6,ly-0.3*(i+1),tx,fontsize=9,va='top')
ax.text(10.05,-2.95,'G(t) agrège I, S, T (+) et R (−) : équation (2.4).',ha='right',fontsize=9.5,color='#333333',style='italic')
plt.savefig('Figure_6_1_diagramme_causal.png',dpi=220,bbox_inches='tight',facecolor='white'); print('ok')
