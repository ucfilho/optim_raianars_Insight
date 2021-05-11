import numpy as np

def AvaliaX(X,fitness):
  # def AvaliaX(X):
  
  nrow,ncol=X.shape
  # fitness = np.asarray([Fun(ind) for ind in X])
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  fobj_best = fitness[best_idx]
  y=fitness
  BEST=best
  FOBEST=fobj_best
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  x=XYsorted[:,0:ncol]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)
  return XY,BEST_XY,BEST,FOBEST
