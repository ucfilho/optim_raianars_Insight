# -*- coding: utf-8 -*-
"""Untitled164.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Crjtjum0G807KSBWkqr6pyFSgr-OrmAq
"""

import numpy as np
import random

def de(MAX,MIN, mut, crossp, popsize, its,fobj,X,SOMA,TOTAL):
  p =0.1  
  Num=len(X[0,:]) # num eh usado duas vezes para significados diferentes
  best_number = int(popsize*p)
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
  ind =np.argpartition(fitness, -best_number)[-best_number:] # find index of best p*popsize
  best_idx = np.argmin(fitness) # not using the best anymore but a random best
  best = X[best_idx]
  best_idx = random.choice(ind) # index of the best in p*popsize (random best)
  best_selection = X[best_idx]
  
  Num=len(X[0,:]) # Alterando Num dimensao da solucao
  for i in range(its):
    if(SOMA>TOTAL):
      break
    for j in range(popsize):
      if(SOMA>TOTAL):
        break
      SOMA=SOMA+1
      
      idxs = [idx for idx in range(popsize) if idx != j]
      a, b, c = X[np.random.choice(idxs, 3, replace = False)]
      # mutant = a + mut * (b - c)
      mutant = X[j,:]+mut*(best_selection-X[j,:]) + mut * (b - c)

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
      if f < fitness[j]:
        fitness[j] = f
        X[j,:] = trial
        if f < fitness[best_idx]:
          best_idx = j
          best = trial
            
  fitness = np.asarray([fobj(ind) for ind in X])
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
  
  return XOLD,BEST,FOBEST,XY,BEST_XY,SOMA