# -*- coding: utf-8 -*-
"""randWALKsteps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sjAQN85S90YsD_RzuqPD7V_P4no7xQOy
"""

import numpy as np 

def fixWALK(fobj,best,fbest,popsize,tunePAR,MAX,MIN,X,FIX):
    
  #print("==================")
  #print(FES)

  # FIX = 100 # Number of adjusts main code
  nseq = 0
  maxPAR,minPAR,maxFES,FES,gen = tunePAR 
  cont = 0
  dim = len(X[0,:])
  fitness = [fobj(ind) for ind in X]
  FES = FES + popsize

  while(nseq < FIX):
    FES = FES+1
    trial = np.copy(X[cont,:])
    cont = cont + 1
    tunePAR = [maxPAR,minPAR,maxFES,FES,gen]
    for j in range(dim):
      #stdWALK = 0.5*(minPAR/(minPAR+cont))**2*np.random.rand()*best[j]
      stdWALK = ((1/10*np.random.rand()*best[j])**2)**0.5
      afterWALK = np.random.normal(best[j] ,stdWALK )
      if(afterWALK > MAX[j]): afterWALK = MAX[j]
      if(afterWALK < MIN[j]): afterWALK = MIN[j]
      trial[j] = afterWALK

    f = fobj(trial)
    if(f < fbest): 
      X[cont-1,:] = trial
      fbest = f
      best = trial
    if (cont >= popsize): cont = 0
    nseq = nseq + 1
  # tunePAR = [maxPAR,minPAR,maxFES,FES,gen]

  #fitness = np.asarray([fobj(ind) for ind in X]) # I guess this  line can be deleted
  #FES = FES + popsize    # I guess this line  can be deleted
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
