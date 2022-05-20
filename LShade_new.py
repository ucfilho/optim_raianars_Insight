
import numpy as np
import scipy.stats
import random

def LShade(MAX,MIN, popsize,fobj,setTUNE,best,fbest,fitness,X,Xarq,FES):

  SF,SCR,MF,MCR,p, terminal, Narquive = setTUNE
  # return X,BEST,FOBEST,XY,BEST_XY,FES
  #H = 6
  #kH = 0 # kH is used to work with H  
  #terminal = 0.1
  #p=0.1
  #Narquive = popsize
  #Xarq = [] # just to initialize
  mutant= np.copy(X) # just to initialize mutants Uij
  fmutant = np.copy(fitness) # just to initialize fobj(Uij)
  fx=[]; fu=[] # to select the wij Lehmer Mean.
  # setTUNE = [SF,SCR,MF,MCR,FES,p] 

  best_number = int(p*popsize)

  
  
  termination_not_meet = True

  while(termination_not_meet):
    SCR =[];SF=[];
    for i in range(popsize):
      ri = random.randint(1, H) # line 7
      miF = MF[ri]
      if(MCR[ri] == terminal):
        miCR = 0
      else:
        crossp = np.random.normal(miCR , 0.1)
      while (True):
        mut = scipy.stats.cauchy.rvs(loc=miF, scale=0.1)
        if (mut > 0):
          break
        
      ind = fitness.argsort()[range(best_number)] # find index of best p*popsize
      best_idx = random.choice(ind) # index of the best in p*popsize (random best)
      pbest = X[best_idx] # random best 
      idxs = [idx for idx in range(popsize) if idx != i]
      a  = X[np.random.choice(idxs, 1, replace = False)]
      Xnew = np.append(X,Xarq,axis=0)
      idxs2 = [idx for idx in range(popsize+len(Xarq[:,0])) if idx != idxs]
      b  = Xnew[np.random.choice(idxs2, 1, replace = False)]

      mutant[i,:] = X[i,:]+mut*(pbest-X[i,:]) + mut * (a - b)
      FES = FES + 1
      fmutant[i] = fobj(mutant[i,:])


    for i in range(popsize):
      if( fmutant[i]  <= fitness[i]):
        Xold = X[i,:] 
        X[i,:] = mutant[i,:]
        fitness[i]=fmutant[i]
        if(fbest >= fmutant[i]):
          best = mutant[i,:]
          fbest = fmutant[i]
      else:
        X[i,:] = X[i,:] # it is not necessary this line but just to remeber it
      if( fmutant[i]  < fitness[i]):
        if(len(Xarq[:,0])< Narquive):
          Xarq=np.append(Xarq,Xold)
        else:
          ri = random.randint(0, Narquive-1) # deleting individuals if necessary line 19
          Xarq[ri] = Xold
        #Xarq[i,:] = Xold  # need better discussion
        SCR.append(crossp)
        SF.append(mut)
        fx.append(fitness[i])
        fu.append(fmutant[i])
    # memory update algorithm 1:
    if (len(SCR)>0):
      deltaF = np.abs(np.asarray(fu)-np.asarray(fx))
      w = deltaF/sum(deltaF)
      if(MCR[kH] == terminal or max(SRC)==0):
        MCR[kH] = terminal
      else:
        y = np.asarray(SCR)
        MCR[kH] = np.dot(w,y**2)/np.dot(w,y)
      y = np.asarray(SF)
      MF[kH] = np.dot(w,y**2)/np.dot(w,y)
      kH = kH + 1
      if(kH > H): kH = 0
    else:
      MCR = MCR
      MF = MF
  termination_not_meet = False  
  
  setTUNE =[SF,SCR,MF,MCR,p, terminal, Narquive]

  y=fitness

  BEST=best
  FOBEST=fbest
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  X=XYsorted[:,0:Num]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)
  

  
  return fitness,X,BEST,FOBEST,XY,BEST_XY,FES,Xarq,setTUNE
