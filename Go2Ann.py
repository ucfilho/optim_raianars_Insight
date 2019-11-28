# -*- coding: utf-8 -*-
import time
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from scipy import optimize
import pandas as pd

import Function
import de_soma_Insight
import de_bounds_matriz

# Functions
def sigmoid(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

def tasig(x,deriv=False):
    if(deriv==True):
        return 1-x*x
    return 2/(1+np.exp(-2*x))-1

# purelin function
def purelin(x,deriv=False):
    if(deriv==True):
        return 1
    return x

# funcao normatiza dados
def Normatiza(x_train,X_max,X_min):
    strings=list(x_train)
    k=-1
    for i in strings:
        k=k+1
        max_x=X_max[k]
        min_x=X_min[k]
        a=(max_x+min_x)/2
        b=(max_x-min_x)/2
        x_train[i]=(x_train[i]-a)/b
    return x_train

def GetMatriz(ANN):
  nrow0=int(ANN.iloc[0,1]);#print(nrow0);
  ncol0=int(ANN.iloc[1,1]);#print(ncol0);
  nrow1=int(ANN.iloc[2,1]);#print(nrow1);
  ncol1=int(ANN.iloc[3,1]);#print(ncol1);
  Col=np.array(range(2,ncol0+2)); # print(Col)
  Row=np.array(range(0,nrow0)); # print(Row)
  syn0=np.array(ANN.iloc[Row,Col])
  syn0=pd.DataFrame(syn0).dropna() 
  syn0=np.array(syn0)
  ncol=int(ANN.iloc[0,1])
  syn1=ANN.iloc[:,(ncol0+ncol1+1)] ;#print(syn1_F)
  nrow=len(np.array(syn1.dropna()))
  A=np.zeros((nrow,1));
  A[:,0]=np.copy(syn1.dropna());
  syn1=np.copy(A);#print(pd.DataFrame(syn1_F))
  row,col=ANN.shape
  X_max=np.array(ANN.iloc[:,col-1].dropna());#print(X_max_F)
  X_min=np.array(ANN.iloc[:,col-2].dropna());#print(X_min_F)

  return syn0,syn1,X_max,X_min

# funcao retorna os dados a forma original
def Original(x_train,X_max,X_min):
    strings=list(x)
    k=-1
    for i in strings:
        k=k+1
        max_x=X_max[k]
        min_x=X_min[k]
        a=(max_x+min_x)/2
        b=(max_x-min_x)/2
        x_train[i]=x_train[i]*b+a
    return x_train

def ANN_ycal(syn0,syn1,X_train):
  l0 = X_train
  l1 = tasig(np.dot(l0,syn0))
  l2 = purelin(np.dot(l1,syn1))
  y_calc=np.reshape(l2,len(l2))
  return y_calc

def Classifica(y):
  n=len(y)
  yc=np.zeros(n)
  for i in range(n):
    if(y[i]<0):
      yc[i]=-1
    else:
      yc[i]=1
  return yc

def GeraIndices(X,BESTo,FOBESTo,DIo,MAT_INDo,SOMA,TOTAL):
  global fields, Go2Ann, Fc
  global syn0_F,syn1_F,X_max_F,X_min_F
  global syn0_CR,syn1_CR,X_max_CR,X_min_CR
  nrow,ncol=X.shape
  FOBESTm=1e99
  Fo=MAT_INDo[0,6]    # VALOR Fo   
  CRo=MAT_INDo[0,7]   # VALOR CRo
  QUANT=17 # quantos indices esta fazendo
  MAT_IND=np.zeros((1,QUANT))

  REF=0.1 # REFERENCIA DE DIFERENCAS ENTRE OS ELEMENTOS
  
  XY,BEST_XY,BEST,FOBEST=AvaliaX(X)
  soma=0
  for j in range(ncol):
    for i in range(nrow):
        Xj=np.mean(X[:,j])
        soma=soma+(X[i,j]-Xj)**2
  DI=(soma/nrow)**0.5
  DIr=DI/DIo
  MAT_IND[0,0]=DI #dispersao
  MAT_IND[0,1]=DIr # dispersao relativa
  MAT_IND[0,2]=SOMA/TOTAL # fracao relativa

  V1=FOBESTo
  V2=FOBEST
  A=2*V2
  if(V1 > A):
    MAT_IND[0,3]=2 # o valor de fobj torna pelo menos duas vezes melhor
  elif (V2==V1):
    MAT_IND[0,3]=0 # o valor de fobj nao altera
  else:
    MAT_IND[0,3]=1 # o valor de fobj melhora mas menos que duas vezes
  
  # MAT_IND[0,4]  # VELOC X
  DELTA=np.amax(abs(BEST-BESTo))
  if( DELTA >REF):
    MAT_IND[0,4]=2 # difere  for i in range(1,len(PARTIC)):
  elif ( DELTA == 0):
    MAT_IND[0,4]=0 # sem diferenca entre as posicoes do xbest entre duas buscas
  else:
    MAT_IND[0,4]=1 # diferenca entre as posicoes  do xbest menor que ref
  
  MAT_IND[0,5]=nrow  # VALOR NP
  nrow,ncol=XY.shape
  MAT_IND[0,8]=XY[0,(ncol-1)] # VALOR fmin
  MAT_IND[0,9]=XY[(nrow-1),(ncol-1)] # VALOR fmax
  # MAT_IND[0,10] # Valor AD_fmin 
  if abs(MAT_IND[0,8]/MAT_IND[0,8])>1:
    MAT_IND[0,10]=1/abs(MAT_IND[0,8])
  else:
    MAT_IND[0,10]=MAT_IND[0,8]/MAT_IND[0,8]
  # MAT_IND[0,11] # Valor AD_fmax
  if abs(MAT_IND[0,9]/MAT_IND[0,9])>1: # tem que pegar primeira
    MAT_IND[0,11]=1/abs(MAT_IND[0,9]) # tem que pegar primeira
  else:
    MAT_IND[0,11]=MAT_IND[0,9]/MAT_IND[0,9] # tem que pegar do anterior

  # MAT_IND[0,12] # DELTA Fobj
  MAT_IND[0,12]=MAT_IND[0,3]-MAT_IND[0,3]  # tem que pegar do anterior
  

  # MAT_IND[0,13] # DELTA Vx
  MAT_IND[0,13]=MAT_IND[0,4]-MAT_IND[0,4]  # tem que pegar do anterior

  # MAT_IND[0,14] # r_fitness
  Fmin=0.05
  if (MAT_IND[0,8]==0):
    MAT_IND[0,14]=Fmin
  elif (MAT_IND[0,9]==0):
    MAT_IND[0,14]=Fmin
  else:
    if abs(MAT_IND[0,9]/MAT_IND[0,8])<1:
      MAT_IND[0,14]=1-abs(MAT_IND[0,9]/MAT_IND[0,8])
    else:
      MAT_IND[0,14]=1-abs(MAT_IND[0,8]/MAT_IND[0,9])

  MAT_IND[0,6]=Fo
  MAT_IND[0,7]=CRo

  # comecando a rede!!!
  #['DI RELATIVO', 'FRAC Its', 'Fo', 'CRo'] VALORES A USAR
  #MAT_IND[0,1]=DIr # dispersao relativa
  #MAT_IND[0,2]=SOMA/TOTAL # fracao relativa
  #MAT_IND[0,6]=Fo
  #MAT_IND[0,7]=CRo
  
  x_train=MAT_INDo[0,[1,2,6,7]]
  x_train=pd.DataFrame(x_train).T

  nrow,ncol=ANN_F.shape
  x_train=Go2Ann.Normatiza(x_train,X_max_F,X_min_F)
  y_calc_F=Go2Ann.ANN_ycal(syn0_F,syn1_F,x_train)
  y_calc_CR=Go2Ann.ANN_ycal(syn0_CR,syn1_CR,x_train)
  #print(x_train);
  #print(y_calc);
  y_cod_F=Go2Ann.Classifica(y_calc_F)
  y_cod_CR=Go2Ann.Classifica(y_calc_CR)

  Fd=DIr
  CRa=np.copy(CRo)
  Fa=np.copy(Fo)

  if(y_cod_F>0):
    Fo=Fo*(1+Fd) #Fo=Fo+Fc
    Fo=(3*Fo+Fa)/4 # para suavizar
    if(Fo<Fa):
      Fo=Fa+0.05
    if(Fo<Fa): # conferir a necessidade de melhorar 
      Fo=Fa+0.05
  else:
    Fo=Fo*(1-Fd) #Fo=Fo-Fc
  
  if(y_cod_CR>0):
    CRo=CRo*(1+Fd) #CRo=CRo+Fc
    CRo=(3*CRo+CRa)/4 # para suavizar
    if(CRo<CRa):  # conferir a necessidade de melhorar 
      CRo=CRa+0.05
  else:
    CRo=CRo*(1-Fd);#CRo=CRo-Fc
  
  if(CRo<Fc):
    CRo=(CRo+CRa)/2 # conferir a necessidade de melhorar
  if(CRo> 1):
    CRo=1

  if(Fo<Fc):
    Fo=(Fa+Fo)/2  # conferir a necessidade de melhorar
  if(Fo> 1):
    Fo=1
  
  CRo=(2*CRo+CRa)/3 # para suavizar
  
  MAT_IND[0,15]=Fo # valor de F que sai da rede
  MAT_IND[0,16]=CRo # valor de CR que sai da rede
  #print(confusion_matrix(y_quali,y_obs_test))
  
  return MAT_IND

def AvaliaX(X):
  nrow,ncol=X.shape
  fitness = np.asarray([Fun(ind) for ind in X])
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  fobj_best = fitness[best_idx]
  y=fitness
  BEST=best
  FOBEST=fobj_best
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  x=XYsorted[:,0:ncol]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)
  return XY,BEST_XY,BEST,FOBEST
