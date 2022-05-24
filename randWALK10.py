import random
import numpy as np 

def randWALK(fobj,best,fbest,popsize,MAX,MIN,fitness,X,FES):

  dim = len(X[0,:])  
  
  m = 10
  Xm=np.zeros((m,dim))
  for i in range(m):
    ri = random.randint(0,popsize-1)
    for j in range(dim):
        r=np.random.random()
        Xm[i,j]=r*(MAX[j]-MIN[j])+MIN[j]
        X[ri,j]=Xm[i,j]
  
  fitm = np.asarray([fobj(ind) for ind in Xm])
  FES = FES + m


  best_idx = np.argmin(fitm)
  bestm = X[best_idx]
  fbestm = fitness[best_idx] 
  
  


    
  #tunePAR = [maxPAR,minPAR,maxFES,FES,gen]
  for i in range(popsize):
    rm = random.randint(0,m-1)
    for j in range(dim):
        rnd = np.random.rand()
        eps1 = np.random.rand()
        eps2 = np.random.rand()
        stdWALK = np.abs(X[i,j]-best[j])*rnd
        afterWALK=np.random.normal(best[j] ,stdWALK) 
        afterWALK =  afterWALK + eps1*bestm[j]-eps2*Xm[rm,j]
        if(afterWALK > MAX[j]): afterWALK = MAX[j]
        if(afterWALK < MIN[j]): afterWALK = MIN[j]
        X[i,j] = afterWALK
    fitm = fobj(X[i,:])
    FES = FES + 1
    if(fitm < fbest):
      best =X[i,:]
      fbest = fitm
    if(fitm < fbestm ):
      bestm = X[i,:]
      fbestm = fitm

  y=fitness
  BEST=best
  FOBEST=fbest
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  X=XYsorted[:,0:dim]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)
  
  

  return fitness,X,best,FOBEST,XY,BEST_XY, FES
