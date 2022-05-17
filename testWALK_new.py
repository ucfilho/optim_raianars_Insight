import numpy as np 

def randWALK(fobj,best,fbest,popsize,tunePAR,MAX,MIN,fitness,X):
    
  #print("==================")
  #print(FES)

  # FIX = 100 # Number of adjusts main code
  nseq = 1
  maxPAR,minPAR,maxFES,FES,gen = tunePAR 
  cont = 0
  dim = len(X[0,:])
  #fitness = [fobj(ind) for ind in X]
  #FES = FES + popsize
  keepFLOW = True

  while(keepFLOW):
    FES = FES+1
    trial = np.copy(X[cont,:])
    cont = cont + 1
    tunePAR = [maxPAR,minPAR,maxFES,FES,gen]
    for i in range(popsize):
      for j in range(dim):
        #stdWALK = 0.5*(minPAR/(minPAR+cont))**2*np.random.rand()*best[j]
        #stdWALK = ((1/10*np.random.rand()*best[j])**2)**0.5
        r = np.log(nseq+2)/(nseq+2)
        stdWALK = np.abs(r*(X[i,j]-best[j]))*np.random.rand()
        afterWALK = np.random.normal(best[j] ,stdWALK )
        if(afterWALK > MAX[j]): afterWALK = MAX[j]
        if(afterWALK < MIN[j]): afterWALK = MIN[j]

      X[i,j] = afterWALK
    
    # tunePAR = [maxPAR,minPAR,maxFES,FES,gen]
    
    FES = FES + popsize
    if(FES > maxFES):
      FES = FES - popsize
      nseq  = FIX
      keepFLOW = False
    else:
      fitness = np.asarray([fobj(ind) for ind in X]) # I guess this  line can be deleted
      best_idx = np.argmin(fitness)
      new_best = X[best_idx]
      new_fbest = fitness[best_idx]
      if( new_fbest < fbest):
        fbest = new_fbest
        best = new_best
      else:
        X[0,:] = best
    nseq = nseq + 1
  

  
  y=fitness
  Num = popsize
  BEST=best
  FOBEST=fbest
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  x=XYsorted[:,0:Num]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)


  return fitness,X,best,FOBEST,XY,BEST_XY, FES
