# -*- coding: utf-8 -*-
"""de_JadeEq.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQOu6VWN_YoCZW4tytAbDEQfTRboPPmE
"""

import numpy as np
import random

def de(bounds, mut, crossp, popsize, its,fobj,X):
  
  p =0.1
  Num=len(bounds)
  dimensions = len(bounds)  
  MAX=np.zeros(Num)
  MIN=np.zeros(Num)
  for k in range(Num):
    MAX[k]=bounds[k][1]
    MIN[k]=bounds[k][0]
  best_number = int(popsize*p)
  fitness = np.asarray([fobj(ind) for ind in X])
  ind =np.argpartition(fitness, -best_number)[-best_number:] # find index of best p*popsize
  best_idx = np.argmin(fitness) # not using the best anymore but a random best
  best = X[best_idx]
  best_idx = random.choice(ind) # index of the best in p*popsize (random best)
  best_selection = X[best_idx]
  
  #print('====0====',X)
  for i in range(its):
    for j in range(popsize):
      
      idxs = [idx for idx in range(popsize) if idx != j]
      a, b, c = X[np.random.choice(idxs, 3, replace = False)]
      mutant = X[j,:]+mut*(best_selection-X[j,:]) + mut * (b - c)
      
      #print('===== 1 =====',mutant)

      for k in range(Num):
        if(mutant[k]>MAX[k]):
          mutant[k]=MAX[k]
        if(mutant[k]<MIN[k]):
          mutant[k]=MIN[k]
          
      cross_points = np.random.rand(dimensions) < crossp
      
      #print('===== 2 =====',cross_points)
      
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
  
  
  return x,BEST,FOBEST,XY,BEST_XY
