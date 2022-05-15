# -*- coding: utf-8 -*-
"""LShade.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ScyQ7_iqKdpDkV7gre66hf1SToh3chAq
"""

import numpy as np
import scipy.stats
import random

def de(MAX,MIN,gen,popsize,fobj,X,fitness,method):
  # you need to return to main code 
  #       return X,BEST,FOBEST,XY,BEST_XY,SF,SCR,SFreq,miF,miCR,miFreq
  # main code need to define before change generations 
  #    
  # SF = np.asarray([0.5]); SCR = np.asarray([0.5]); SFreq=np.asarray([1.0])
  # miF = np.asarray([0.5]); miCR = np.asarray([0.5])
  # NPmax= 18*dim;NP=NPmax;
  # method = NPmax,NPmin,maxFES,FES
  # tuneEVAL= [NP,FES,gen] # to update results main code
  #         use in main code: popsize, FES, gen = tuneEVAL
  
  p = 0.1; c = 0.1; 
  NPmax,NPmin,maxFES,FES,SF,SCR,miValues = method
  dim = len(X[0,:])
  best_idx = np.argmin(fitness) # not using the best anymore but a random best
  best = X[best_idx]
  fbest = fitness[best_idx]
  miF, miCR = miValues
  NP = popsize



  Lehmer = sum(SF)
  Lehmer = np.dot(SF,SF)/Lehmer
  mi_F = random.choice(miF)
  mi_F_gen = (1-c)*mi_F + c* Lehmer 
  mi_CR = random.choice(miCR)
  mi_CR_gen = (1-c)*mi_CR + c* np.mean(SCR)


  
  #F_values = scipy.stats.cauchy.rvs(loc=mi_F, scale=0.1, size=popsize)
  F_values=np.zeros(popsize)
  third = int(popsize/3)-1
  F_values[0:third] = np.random.uniform(0.0, 1.2, third)
  two_third = popsize- third
  F_values[third:] = np.random.normal(mi_F_gen , 0.1, two_third)
  CR_values = np.random.normal(mi_CR_gen , 0.1,popsize )


  if(popsize >= NPmin):

    for i in range(popsize):
      rnd= np.random.uniform()
      best_number = int(p*popsize*rnd)
      ind =np.argpartition(fitness, -best_number)[-best_number:] # find index of best p*popsize
      best_idx = random.choice(ind) # index of the best in p*popsize*rnd (random best)
      best_selection = X[best_idx]

      mut = F_values[i]
      crossp = CR_values[i]
      idxs = [idx for idx in range(popsize) if idx != i]
      a, b, c = X[np.random.choice(idxs, 3, replace = False)]
      mutant = X[i,:]+mut*(best_selection-X[i,:]) + mut * (b - c)

      rnd= np.random.uniform()

      if(rnd <= crossp):
        for ind in range(dim):
          if(mutant[ind]>MAX[ind]):
            mutant[ind] = MAX[ind]
          if(mutant[ind]<MIN[ind]):
            mutant[ind] = MIN[ind] 
        X[i,:] = np.copy(mutant)
        fnew = fobj(mutant)
        fitness[i] = fnew
        FES = FES + 1
        SF=np.append(SF,mut)
        SCR=np.append(SCR,crossp)

        
        if(fnew < fbest):
          best = mutant
          fbest = fnew
          miF= np.append(miF,mut)
          miCR= np.append(miCR,crossp)
    

  if(popsize <= NPmin ): # using random walking to conclude
    Xfinal=np.zeros((NP,dim)) # X is Frannk population
    sigma=np.zeros((NP,dim)) 
    FES = FES + 1
    individual = -1
    NP = popsize

    while(FES < maxFES):
      for k in range(NP):
        individual = individual + 1
        for j in range(dim):
          r=np.random.random()
          test =MIN[j]+r*(MAX[j]-MIN[j])
          #print('test',test)
          valor =(k+1) /(2*NP) *(test -best[j])
          sigma= np.abs(np.cos(np.pi*valor))
          #print('sigma=',sigma)
          Xfinal[k,j] =  np.random.normal(test , sigma )
          for j in range(dim):
            if(Xfinal[k,j]>MAX[j]):
              Xfinal[k,j] = MAX[j]
            if(Xfinal[k,j]<MIN[j]):
              Xfinal[k,j] = MIN[j] 
        if(FES < maxFES):
          fcalc = fobj(Xfinal[k,:])
          FES = FES + 1
          if(fcalc < fbest):
            best = Xfinal[k,:]
            fbest = fcalc
          if(individual < NP): # exchange population until reach maxFES
            X[individual,:] = np.copy(Xfinal[k,:])
            fitness[individual] =fcalc
          else:
            individual = 0
            X[individual,:] = np.copy(Xfinal[k,:])
            fitness[individual] =fcalc


  y=fitness

  BEST=best
  FBEST=fbest
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  XY=XYsorted
  BEST_XY =np.append(BEST,FBEST)
  calc = (NPmin-NPmax)/maxFES*FES+NPmax # Linear Population Size Reduction (LPSR)
  NP = int(np.round(calc)) # Linear Population Size Reduction (LPSR) 
  gen = gen + 1
  tuneEVAL= [NP,FES,gen]

  return X,BEST,FBEST,XY,BEST_XY,tuneEVAL,SF,SCR,miF,miCR
