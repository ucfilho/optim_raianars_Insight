# -*- coding: utf-8 -*-
"""annDE_FES.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y4rAcjpXonai6K9tbI_bU8685DRJ2-cY
"""

import numpy as np

def de(MAX,MIN, mut, crossp, popsize, its,fobj,X,FES): 
    
  Num=len(X[0,:]) # num eh usado duas vezes para significados diferentes
  
  XOLD=X
  X=np.zeros((popsize,Num)) 
    
  for i in range(popsize):
    for j in range(Num):
        X[i,j]=np.copy(XOLD[i,j])
  
  
  Num=len(MAX) # alterando Num para segundo significado (definicao de bounds)
  bounds=[(0,0)] * Num
  # dimensions = len(bounds)  # dimensions refere a populacao
  dimensions =len(X[0,:]) # num eh usado duas vezes para significados diferentes
  
  for i in range(Num):
    bounds[i]=(MIN[i], MAX[i])

  fitness = np.asarray([fobj(ind) for ind in X])
  # FES = FES + popsize
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  
  Num=len(X[0,:]) # Alterando Num dimensao da solucao
  for j in range(popsize):
    idxs = [idx for idx in range(popsize) if idx != j]
    a, b, c = X[np.random.choice(idxs, 3, replace = False)]
    mutant = a + mut * (b - c)

    for k in range(Num):
        if(mutant[k]>MAX[k]):
          mutant[k]=MAX[k]
        if(mutant[k]<MIN[k]):
          mutant[k]=MIN[k]
          
    cross_points = np.random.rand(dimensions) < crossp
    if not np.any(cross_points):
      cross_points[np.random.randint(0, dimensions)] = True
    trial = np.where(cross_points, mutant, X[j,:])


    f = fobj(trial)
    FES = FES + 1
    if f < fitness[j]:
      fitness[j] = f
      X[j,:] = trial
    if f < fitness[best_idx]:
      best_idx = j
      best = trial

    fitness = np.asarray([fobj(ind) for ind in X])
    #FES = FES + popsize

  fitness = np.asarray([fobj(ind) for ind in X])
  #FES = FES + popsize
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  fobj_best = fitness[best_idx]

  
  y=fitness

  BEST=best
  FOBEST=fobj_best
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  x=XYsorted[:,0:Num]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)
  
  for i in range(popsize):
    for j in range(Num):
        XOLD[i,j]=np.copy(X[i,j])
  
  return XOLD,BEST,FOBEST,XY,BEST_XY,FES
