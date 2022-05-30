from AvaliaX import AvaliaX
#from Go2Ann import Go2Ann
import Go2Ann
import pandas as pd
import numpy as np

def GeraIndices(eqFRANNK,X,Fitness,MAT_INDo,setANN,BESTo,FOBESTo,DIo,SOMA,TOTAL,syn0_F,
                syn1_F,X_max_F,X_min_F,syn0_CR,syn1_CR,X_max_CR,
                X_min_CR,fields,Fun):

  nrow,ncol=X.shape
  FOBESTm=1e99
  #print('=======',MAT_INDo)
  #Fo=MAT_INDo[0,6]    # VALOR Fo  
  Fo=MAT_INDo[0,6]    # VALOR Fo   
  CRo=MAT_INDo[0,7]   # VALOR CRo
  QUANT=17 # quantos indices esta fazendo
  MAT_IND=np.zeros((1,QUANT))
  
  Foo = eqFRANNK(0.5,1,1)
  print('Foo =',Foo)
  
  CRoo = eqFRANNK(0.6,2,-1)
  print('CRoo =',CRoo)

  REF=0.1 # REFERENCIA DE DIFERENCAS ENTRE OS ELEMENTOS
  nrow,ncol=X.shape
  FOBESTm=1e99
  Fo=MAT_INDo[0,6]    # VALOR Fo   
  CRo=MAT_INDo[0,7]   # VALOR CRo
  QUANT=17 # quantos indices esta fazendo
  MAT_IND=np.zeros((1,QUANT))

  REF=0.1 # REFERENCIA DE DIFERENCAS ENTRE OS ELEMENTOS
  #Fitness = np.asarray([Fun(ind) for ind in X])
  XY,BEST_XY,BEST,FOBEST=AvaliaX(X,Fitness)
 
  RAIN = setANN #np.array(setANN)
  Fc= RAIN[0] 
  Fd= RAIN[1]
  filter1 = RAIN[2]
  filter2 = RAIN[3]
  filter3 = RAIN[4]
  filter4 = RAIN[5]
  #Fc,Fd,filter1, filter2, filter3= setANN 

  f1 = filter1
  f2 = filter2
  f3 = filter3
  f4 = filter4


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
  BEST = BESTo
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
  if(Fd == 1e99):
    Fd=DIr
  else:
    Fd = Fd


  Fo = eqFRANNK(Fo,1,y_cod_F)
  print('Fo =',Fo)
  
  CRo = eqFRANNK(CRo,2,y_cod_CR)
  print('CRo =',CRo)

  MAT_IND[0,15]=Fo # valor de F que sai da rede
  MAT_IND[0,16]=CRo # valor de CR que sai da rede
  
  return 
