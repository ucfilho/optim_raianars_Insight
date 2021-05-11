from AvaliaX import AvaliaX
#from Go2Ann import Go2Ann
import Go2Ann
import pandas as pd
import numpy as np

def GeraIndices(X,BESTo,FOBESTo,DIo,MAT_INDo,SOMA,TOTAL,syn0_F,
                syn1_F,X_max_F,X_min_F,syn0_CR,syn1_CR,X_max_CR,
                X_min_CR,Fc,fields,Fun):
  
  nrow,ncol=X.shape
  FOBESTm=1e99
  Fo=MAT_INDo[0,6]    # VALOR Fo   
  CRo=MAT_INDo[0,7]   # VALOR CRo
  QUANT=17 # quantos indices esta fazendo
  MAT_IND=np.zeros((1,QUANT))

  REF=0.1 # REFERENCIA DE DIFERENCAS ENTRE OS ELEMENTOS
  Fitness = np.asarray([Fun(ind) for ind in X])
  XY,BEST_XY,BEST,FOBEST=AvaliaX(X,Fitness)
  
  soma=0
  for j in range(ncol):
    for i in range(nrow):
        Xj=np.mean(X[:,j])
        soma=soma+(X[i,j]-Xj)**2
  DI=(soma/nrow)**0.5
  DIr=DI/DIo
  MAT_IND[0,0]=DI #dispersao
  MAT_IND[0,1]=DIr # dispersao relativa
  MAT_IND[0,2]=SOMA/TOTAL # fracao relativa

  V1=FOBESTo
  V2=FOBEST
  A=2*V2
  if(V1 > A):
    MAT_IND[0,3]=2 # o valor de fobj torna pelo menos duas vezes melhor
  elif (V2==V1):
    MAT_IND[0,3]=0 # o valor de fobj nao altera
  else:
    MAT_IND[0,3]=1 # o valor de fobj melhora mas menos que duas vezes
  
  # MAT_IND[0,4]  # VELOC X
  DELTA=np.amax(abs(BEST-BESTo))
  if( DELTA >REF):
    MAT_IND[0,4]=2 # difere  for i in range(1,len(PARTIC)):
  elif ( DELTA == 0):
    MAT_IND[0,4]=0 # sem diferenca entre as posicoes do xbest entre duas buscas
  else:
    MAT_IND[0,4]=1 # diferenca entre as posicoes  do xbest menor que ref
  
  MAT_IND[0,5]=nrow  # VALOR NP
  nrow,ncol=XY.shape
  MAT_IND[0,8]=XY[0,(ncol-1)] # VALOR fmin
  MAT_IND[0,9]=XY[(nrow-1),(ncol-1)] # VALOR fmax
  # MAT_IND[0,10] # Valor AD_fmin 
  if abs(MAT_IND[0,8]/MAT_IND[0,8])>1:
    MAT_IND[0,10]=1/abs(MAT_IND[0,8])
  else:
    MAT_IND[0,10]=MAT_IND[0,8]/MAT_IND[0,8]
  # MAT_IND[0,11] # Valor AD_fmax
  if abs(MAT_IND[0,9]/MAT_IND[0,9])>1: # tem que pegar primeira
    MAT_IND[0,11]=1/abs(MAT_IND[0,9]) # tem que pegar primeira
  else:
    MAT_IND[0,11]=MAT_IND[0,9]/MAT_IND[0,9] # tem que pegar do anterior

  # MAT_IND[0,12] # DELTA Fobj
  MAT_IND[0,12]=MAT_IND[0,3]-MAT_IND[0,3]  # tem que pegar do anterior
  

  # MAT_IND[0,13] # DELTA Vx
  MAT_IND[0,13]=MAT_IND[0,4]-MAT_IND[0,4]  # tem que pegar do anterior

  # MAT_IND[0,14] # r_fitness
  Fmin=0.05
  if (MAT_IND[0,8]==0):
    MAT_IND[0,14]=Fmin
  elif (MAT_IND[0,9]==0):
    MAT_IND[0,14]=Fmin
  else:
    if abs(MAT_IND[0,9]/MAT_IND[0,8])<1:
      MAT_IND[0,14]=1-abs(MAT_IND[0,9]/MAT_IND[0,8])
    else:
      MAT_IND[0,14]=1-abs(MAT_IND[0,8]/MAT_IND[0,9])

  MAT_IND[0,6]=Fo
  MAT_IND[0,7]=CRo
  
  x_train=MAT_INDo[0,[1,2,6,7]]
  x_train=pd.DataFrame(x_train).T

  #nrow,ncol=ANN_F.shape
  x_train=Go2Ann.Normatiza(x_train,X_max_F,X_min_F)
  y_calc_F=Go2Ann.ANN_ycal(syn0_F,syn1_F,x_train)
  y_calc_CR=Go2Ann.ANN_ycal(syn0_CR,syn1_CR,x_train)
  y_cod_F=Go2Ann.Classifica(y_calc_F)
  y_cod_CR=Go2Ann.Classifica(y_calc_CR)
  
  # print('y_cod_CR=',y_cod_CR,'y_cod_F=',y_cod_F)
  
  Fd=DIr
  CRa=np.copy(CRo)
  Fa=np.copy(Fo)
  '''
  if(y_cod_F>0):
    Fo=Fo*(1+Fd) #Fo=Fo+Fc
  else:
    Fo=Fo*(1-Fd) #Fo=Fo-Fc
    
  if(y_cod_CR>0):
    CRo=CRo*(1+Fd) #CRo=CRo+Fc
  else:
    CRo=CRo*(1-Fd);#CRo=CRo-Fc
  
  if(CRo<Fc):CRo=Fc 
  if(Fo<Fc):Fo=Fc
  if(CRo>1):CRo=1
  if(CRo< Fc): CRo=Fc
  CRo=(2*CRo+CRa)/3 # para suavizar
  Fo=(3*Fo+Fa)/4 # para suavizar
  '''
  if(y_cod_F>0):
    Fo=Fo*(1+Fd) #Fo=Fo+Fc
    Fo=(3*Fo+Fa)/4 # para suavizar
    if(Fo<Fa):
      Fo=Fa+0.05
    if(Fo<Fa): # conferir a necessidade de melhorar 
      Fo=Fa+0.05
  else:
    Fo=Fo*(1-Fd) #Fo=Fo-Fc
  
  if(y_cod_CR>0):
    CRo=CRo*(1+Fd) #CRo=CRo+Fc
    CRo=(3*CRo+CRa)/4 # para suavizar
    if(CRo<CRa):  # conferir a necessidade de melhorar 
      CRo=CRa+0.05
  else:
    CRo=CRo*(1-Fd);#CRo=CRo-Fc
  
  if(CRo<Fc):
    CRo=(CRo+CRa)/2 # conferir a necessidade de melhorar
  if(CRo> 1):
    CRo=1

  if(Fo<Fc):
    Fo=(Fa+Fo)/2  # conferir a necessidade de melhorar
  if(Fo> 1):
    Fo=1
  
  CRo=(2*CRo+CRa)/3 # para suavizar
  MAT_IND[0,15]=Fo # valor de F que sai da rede
  MAT_IND[0,16]=CRo # valor de CR que sai da rede
  
  return MAT_IND
