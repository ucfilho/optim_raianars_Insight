# -*- coding: utf-8 -*-
"""jade_creating.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ucfilho/Raianars_paper_one_revisited/blob/main/After_asked_reviews_one_2022/InsaneMy/jade_creating.ipynb
"""

import numpy as np
import scipy.stats
import random

def de(MAX,MIN, popsize, its,fobj,X,SOMA,TOTAL,SF,mi_F,SCR,mi_CR):
  # you need to return to main code 
  #       return XOLD,BEST,FOBEST,XY,BEST_XY,SOMA,SF,mi_F,SCR,mi_CR
  # main code need to define before change generations 
  #    SF = [0.0]; SCR = [0.0]; mi_CR = 0.9; mi_F = 0.5;
  # SF = [0.0]; SCR = [0.0]; # values initialized with zero but in main code
  # you need to have SF = [0.0]; SCR = [0.0]; before initialize generations
  # mi_CR = 0.9; mi_F = 0.5; 
  # you need to have mi_F = 0.5, mi_F = 0.5 before initialize generations
  
  p = 0.1; c = 0.67
  # c = 0.67 # c is a number between 0 and 1 (filter of result)
  best_number = int(p*popsize)
  Lehmer = sum(SF)
  if (Lehmer == 0):
    mi_F_gen = mi_F
  else:
    Lehmer = np.dot(SF,SF)/Lehmer
    mi_F_gen = (1-c)*mi_F + c* Lehmer 
  if(sum(SCR)==0):
    mi_CR_gen = mi_CR
  else:
    mi_CR_gen = (1-c)*mi_CR + c* np.mean(SCR)

  
  #F_values = scipy.stats.cauchy.rvs(loc=mi_F, scale=0.1, size=popsize)
  F_values=np.zeros(popsize)
  third = int(popsize/3)-1
  #F_values[0:third] = np.random.uniform(0.0, 1.2, third+1)
  F_values[0:third] = np.random.uniform(0.0, 1.2, third)
  #two_third = popsize-(third+1)
  two_third = popsize- third
  F_values[third:] = np.random.normal(mi_F_gen , 0.1, two_third)
  CR_values = np.random.normal(mi_CR_gen , 0.1,popsize )

  Num = len(X[0,:])
  XOLD=np.copy(X)
  X=np.zeros((popsize,Num)) 
    
  for i in range(popsize):
    for j in range(Num):
        X[i,j]=np.copy(XOLD[i,j])
  
  # Num eh usado com dois significados aqui 
  Num=len(MAX) # alterando Num para segundo significado (definicao de bounds)
  bounds=[(0,0)] * Num
  # dimensions = len(bounds)  # dimensions refere a populacao
  dimensions =len(X[0,:]) # num eh usado duas vezes para significados diferentes
  
  for i in range(Num):
    bounds[i]=(MIN[i], MAX[i])

  fitness = np.asarray([fobj(ind) for ind in X])
  ind =np.argpartition(fitness, -best_number)[-best_number:] # find index of best p*popsize
  # best_idx = np.argmin(fitness) # not using the best anymore but a random best
  best_idx = random.choice(ind) # index of the best in p*popsize (random best)
  best = X[best_idx]
  
  Num=len(X[0,:]) # Alterando Num dimensao da solucao popsize
  for i in range(its):
    if(SOMA>TOTAL):
      break
    for j in range(popsize):
      if(SOMA>TOTAL):
        break
      SOMA=SOMA+1
      mut = F_values[i]
      crossp = CR_values[i]
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
      if f < fitness[j]:
        fitness[j] = f
        X[j,:] = trial
        SF.append(mut); SCR.append(crossp) # new line to add vectors
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
  
  for i in range(popsize):
    for j in range(Num):
        XOLD[i,j]=np.copy(X[i,j])
        
  mi_F = mi_F_gen   ; mi_CR = mi_CR_gen

  return XOLD,BEST,FOBEST,XY,BEST_XY,SOMA,SF,mi_F,SCR,mi_CR
