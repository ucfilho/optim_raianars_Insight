import numpy as np

def de(bounds, mut, crossp, popsize, its,fobj,X):
    
  Num=len(bounds)
  #print("parte 1",Num)
  MAX=np.zeros(Num)
  MIN=np.zeros(Num)
  for i in range(Num):
        MAX[i]=bounds[i][1]
        MIN[i]=bounds[i][1]
  

  dimensions = len(bounds)  
  
  #for i in range(Num):
  #  bounds[i]=(MIN[i], MAX[i])

  fitness = np.asarray([fobj(ind) for ind in X])
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  for i in range(its):
    for j in range(popsize):
      
      idxs = [idx for idx in range(popsize) if idx != j]
      a, b, c = X[np.random.choice(idxs, 3, replace = False)]
      mutant = a + mut * (b - c)
        
      #print("parte 2=",mutant)

      for k in range(Num):
        if(mutant[k]>MAX[k]):
          mutant[k]=MAX[k]
        if(mutant[k]<MIN[k]):
          mutant[k]=MIN[k]
          
      cross_points = np.random.rand(dimensions) < crossp
      if not np.any(cross_points):
        cross_points[np.random.randint(0, dimensions)] = True

      trial = np.where(cross_points, mutant, X[j,:])
      #print("parte 3=",trial)
      #print("parte 4=",cross_points)

      f = fobj(trial)
      if f < fitness[j]:
        fitness[j] = f
        X[j,:] = trial
        if f < fitness[best_idx]:
          best_idx = j
          best = trial
            
      print("parte 5=",best)
    
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
