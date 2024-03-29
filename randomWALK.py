# -*- coding: utf-8 -*-
"""randomWALK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15PEY4WtS5MvoO7ZVI9p5Jj9JIMxDG8ta
"""
import numpy as np 

def randomWALK(fobj,best,fbest,popsize,tunePAR,MAX,MIN,X):

  def checkRES(FES,maxFES):
    if(FES < maxFES ):
      flag = True
    else:
      flag = False
    return flag
  
  maxPAR,minPAR,maxFES,FES,gen = tunePAR 
  cont = 0
  dim = len(X[0,:])
  flag = checkRES(FES,maxFES)

  while(flag):
    FES = FES+1
    trial = np.copy(X[cont,:])
    cont = cont + 1
    tunePAR = [maxPAR,minPAR,maxFES,FES,gen]
    flag = checkRES(FES,maxFES)
    for j in range(dim):
      stdWALK = 0.5*(minPAR/(minPAR+cont))**2*np.random.rand()*best[j]
      afterWALK = np.random.normal(best[j] ,stdWALK )
      if(afterWALK > MAX[j]): afterWALK = MAX[j]
      if(afterWALK < MIN[j]): afterWALK = MIN[j]
      trial[j] = afterWALK
    f = fobj[trial]
    if(f < fbest): 
      X[cont-1,:] = trial
      fbest = f
      best = trial
    if (cont > popsize): cont = 0
  # tunePAR = [maxPAR,minPAR,maxFES,FES,gen]

  #fitness = np.asarray([fobj(ind) for ind in X]) # I guess this  line can be deleted
  #FES = FES + popsize    # I guess this line  can be deleted
  fitness = [fobj(ind) for ind in X]
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  fobj_best = fitness[best_idx]

  
  y=fitness
  Num = popsize
  BEST=best
  FOBEST=fobj_best
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  x=XYsorted[:,0:Num]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)


  return X,best,FOBEST,XY,BEST_XY, FES
