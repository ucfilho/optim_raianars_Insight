import numpy as np 

def randWALK(fobj,best,fbest,popsize,tunePAR,MAX,MIN,fitness,X,FES):
    
  #print("==================")
  #print(FES)

  # FIX = 100 # Number of adjusts main code
  
  maxPAR,minPAR,maxFES,FES,gen = tunePAR 
  dim = len(X[0,:])
  keepFLOW = True


  FES = FES+popsize
    
  tunePAR = [maxPAR,minPAR,maxFES,FES,gen]
  for i in range(popsize):
    for j in range(dim):
        r = np.log(i+2)/(i+2)
        stdWALK = np.abs(r*(X[i,j]-best[j]))*(np.random.rand())**2
        afterWALK = np.random.normal(best[j] ,stdWALK )
        if(afterWALK > MAX[j]): afterWALK = MAX[j]
        if(afterWALK < MIN[j]): afterWALK = MIN[j]

    X[i,j] = afterWALK
       
  
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
