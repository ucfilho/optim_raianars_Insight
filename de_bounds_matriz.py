import numpy as np

def de(bounds, mut, crossp, popsize, its,fobj,X):
  
  
  Num=len(bounds)
  dimensions = len(bounds)  
  MAX=np.zeros(Num)
  MIN=np.zeros(Num)
  for k in range(Num):
    MAX[k]=bounds[k][1]
    MIN[k]=bounds[k][0]

  fitness = np.asarray([fobj(ind) for ind in X])
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  
  #print('====0====',X)
  for i in range(its):
    for j in range(popsize):
      
      idxs = [idx for idx in range(popsize) if idx != j]
      a, b, c = X[np.random.choice(idxs, 3, replace = False)]
      mutant = a + mut * (b - c)
      
      #print('===== 1 =====',mutant)

      for k in range(Num):
        if(mutant[k]>MAX[k]):
          mutant[k]=MAX[k]
        if(mutant[k]<MIN[k]):
          mutant[k]=MIN[k]
          
      cross_points = np.random.rand(dimensions) < crossp
      
      #print('===== 2 =====',cross_points)
      
      if not np.any(cross_points):
        cross_points[np.random.randint(0, dimensions)] = True

      trial = np.where(cross_points, mutant, X[j,:])
      

      f = fobj(trial)
      if f < fitness[j]:
        fitness[j] = f
        X[j,:] = trial
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
  
  
  return x,BEST,FOBEST,XY,BEST_XY
