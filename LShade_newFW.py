import numpy as np
import scipy.stats
import random

def LShade(MAX,MIN, popsize,fobj,setTUNE,best,fbest,fitness,X,Xarq,FES):

  SF,SCR,MF,MCR,p, terminal, Narquive,H,kH = setTUNE
  maxFES = 300000
  fmutant = []
  Xmutant = []
  fx=[]; fu=[] # to select the wij Lehmer Mean.
  # setTUNE = [SF,SCR,MF,MCR,p, terminal, Narquive,H] 
  dim = X.shape[1]
  #best_number = int(p*popsize)
  if (p*popsize<1):
    best_number=1
  else:
    best_number = int(p*popsize)
  justGoOUT=1

  if(justGoOUT==1):
    SCR =[];SF=[];
    for i in range(popsize):
      ri = random.randint(0,H-1) # line 7
      miF = MF[ri]
      miCR = MCR[ri]
      if(MCR[ri] == terminal):
        miCR = 0
        crossp = 0
      else:
        crossp = np.random.normal(miCR , 0.1)
      while (True):
        mut = scipy.stats.cauchy.rvs(loc=miF, scale=0.1)
        if (mut > 0):
          break
      if(mut > 1.0): mut =1.0
      if(crossp > 1.0): crossp =1
      if(crossp < 0): crossp = 0 

      ind = fitness.argsort()[range(best_number)] # find index of best p*popsize
      best_idx = random.choice(ind) # index of the best in p*popsize (random best)
      pbest = X[best_idx] # random best 
      idxs = [idx for idx in range(popsize) if idx != i]
      iused = np.random.choice(idxs, 1, replace = False)
      idxs = [idx for idx in range(popsize) if (idx != iused and idx != best_idx)]
      a  = X[iused]
      if(len(Xarq)>0):
        Xii = np.asarray(Xarq)
        Xnew = np.append(X[idxs,:],Xii,axis=0)
      else:
        Xnew=np.copy(X[idxs,:])

      idxs2 = [idx for idx in range(len(Xnew[:,0])) if 2 > 1]
      b  = Xnew[np.random.choice(idxs2, 1, replace = False)]

      if(FES < 0.2*maxFES):
        FW = 0.7*mut
      elif(FES > 0.2*maxFES and FES < 0.4*maxFES):
        FW = 0.8* mut
      else:
        FW = 1.2*mut

      mutant = X[i,:]+FW*(pbest-X[i,:]) + mut * (b - a)
      mutant = mutant.ravel()

      #trial = np.copy(mutant)
      trial = np.copy(X[i,:])

      jrand = random.randint(0,dim-1)

      for j in range(dim):
        rdn = np.random.rand()
        if(rdn < crossp or j == jrand) : 
          trial[j] = mutant[j] 
        else:
          trial[j] = X[i,j]

      mutant  = np.copy(trial) # just to use word mutant instead of trial
      
      for k in range(dim):
        if(mutant[k]>MAX[k]):
          mutant[k]=MAX[k]
        if(mutant[k]<MIN[k]):
          mutant[k]=MIN[k]

      Xmutant.append(mutant)

      FES = FES + 1
      fmut =fobj(mutant)
      fmutant.append(fmut)
    
    

      #for i in range(popsize):
      if( fmutant[i]  <= fitness[i]):
        Xold = X[i,:] 
        X[i,:] = Xmutant[i]
        fx.append(fitness[i])
        fu.append(fmutant[i])
        fitness[i]=fmutant[i]
        SCR.append(crossp)
        SF.append(mut)

        sizeARQ = np.array(Xarq).shape[0]
        if(sizeARQ < Narquive):
          Xarq.append(Xold)
        else:
          ri = random.randint(0, Narquive-1) # deleting individuals if necessary line 19
          Xarq[ri] = Xold

        if(fbest >= fmutant[i]):
          best = Xmutant[i]
          fbest = fmutant[i]
      else:
        X[i,:] = X[i,:] # it is not necessary this line but just to remeber it

    
    # memory update algorithm 1:
    if(kH > H-1): kH = 0

    if (len(SCR)>0):
      deltaF = np.abs(np.asarray(fu)-np.asarray(fx))
      if( sum(deltaF) > 0):
        w = deltaF/sum(deltaF)
      else:
        w =np.ones(len(fu))
      if(MCR[kH] == terminal or max(SCR)==0):
        MCR[kH] = terminal
      else:
        y = np.asarray(SCR)
        MCR[kH] = np.dot(w,y**2)/np.dot(w,y)
      y = np.asarray(SF)
      MF[kH] = np.dot(w,y**2)/np.dot(w,y)
      kH = kH + 1

    else:
      MCR = MCR
      MF = MF

  setTUNE =[SF,SCR,MF,MCR,p, terminal, Narquive,H,kH]


  y=fitness


  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  X=XYsorted[:,0:dim]
  XY=XYsorted
  fitness = XYsorted[:,-1]  
  BEST=X[0,:]
  FOBEST=fitness[0]
  BEST_XY =np.append(BEST,FOBEST)
  
  return fitness,X,BEST,FOBEST,XY,BEST_XY,FES,Xarq,setTUNE
