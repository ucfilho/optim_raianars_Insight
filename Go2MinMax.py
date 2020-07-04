"""
Created on Fri Aug 11 00:01:34 2017
@author: raiana
"""
import numpy as np
from math import *
   

def Intervalo(dim,fchoice):
   
    if(fchoice=='Noisy_Quartic'):
        MAX=np.repeat(1.28,dim)
        MIN=np.repeat(-1.28,dim)
         
    if(fchoice=='Schwefel_222'):
        MAX=np.repeat(10,dim)
        MIN=np.repeat(-10,dim)
      
    if(fchoice=='Schwefel_221'):
        MAX=np.repeat(100,dim)
        MIN=np.repeat(-100,dim)
      
    if(fchoice=='Schwefel_12'):
        MAX=np.repeat(100,dim)
        MIN=np.repeat(-100,dim)     
         
    if(fchoice=='Rosenbrock'):
        MAX=np.repeat(10,dim)
        MIN=np.repeat(-10,dim)

    
    if(fchoice=='Sum_of_different_powers'):
        MAX=np.repeat(1,dim)
        MIN=np.repeat(-1,dim)

    if(fchoice=='Sphere'):
        MAX=np.repeat(5.12,dim)
        MIN=np.repeat(-5.12,dim)
      
    if(fchoice=='Step'):
        MAX=np.repeat(100,dim)
        MIN=np.repeat(-100,dim)      

    if(fchoice=='Easom'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

    if(fchoice=='Booth'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

    if(fchoice=='Beale'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

### Unimodais parecidas

    if(fchoice=='bohachevsky_function'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

    if(fchoice=='sum_squares_function'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar
    
    if(fchoice=='matyas_function'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar
    
    if(fchoice=='mccormick_function'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar
    
    if(fchoice=='dixon_price_function'):#sum_of_different_powers_function
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar
    
    if(fchoice=='three_hump_camel_function'):#sum_of_different_powers_function
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

### Funções multimodais

    if(fchoice=='Rastrigin'):
      MAX=np.repeat(5.12,dim)
      MIN=np.repeat(-5.12,dim)
    
    if(fchoice=='Shubert'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

    if(fchoice=='Schwefel'):
        MAX=np.repeat(500,dim)
        MIN=np.repeat(-500,dim)
 
    if(fchoice=='Ackley'):
        MAX=np.repeat(32,dim)
        MIN=np.repeat(-32,dim)

    if(fchoice=='Bukin'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

    if(fchoice=='Cross_in_tray'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

    if(fchoice=='Michalewicz'):
        MAX=np.repeat(np.pi,dim)
        MIN=np.repeat(0,dim)

    if(fchoice=='Drop_wave'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar

    if(fchoice=='Six_hump_camel'):
        MAX=np.repeat(10,dim) # precisa trocar
        MIN=np.repeat(-10,dim) # precisa trocar
      
    ###########################################
    # novas funcoes adicionadas em dez 02 2019 
    ###########################################
   
    if(fchoice=='alpinen2'):
        MAX=np.repeat(10,dim) 
        MIN=np.repeat(0,dim)     
      
    if(fchoice=='Griewank'):
        MAX=np.repeat(600,dim) 
        MIN=np.repeat(-600,dim)     
      
    if(fchoice=='HappyCat'):
        MAX=np.repeat(2,dim) 
        MIN=np.repeat(-2,dim)     
     
    if(fchoice=='Periodic'):
        MAX=np.repeat(2,dim) 
        MIN=np.repeat(-2,dim)     
      
    if(fchoice=='Qing'):
        MAX=np.repeat(500,dim) 
        MIN=np.repeat(-500,dim)     
      
    if(fchoice=='ridge'):
        MAX=np.repeat(2,dim) 
        MIN=np.repeat(-2,dim)     
      
    if(fchoice=='Salomon'):
        MAX=np.repeat(2,dim) 
        MIN=np.repeat(-2,dim)     
 
    if(fchoice=='Styblinskitank'):
        MAX=np.repeat(5,dim) 
        MIN=np.repeat(-5,dim)     
   
    if(fchoice=='Shubert'):
        MAX=np.repeat(10,dim) 
        MIN=np.repeat(-10,dim)     
      
    if(fchoice=='Shubert3'):
        MAX=np.repeat(10,dim) 
        MIN=np.repeat(-10,dim)     
      
    if(fchoice=='Zakharov'):
        MAX=np.repeat(10,dim) 
        MIN=np.repeat(-5,dim)     
      
    if(fchoice=='XinSheYang'):
        pi2=2*np.pi
        MAX=np.repeat(pi2,dim) 
        MIN=np.repeat(-pi2,dim)     


    return MIN,MAX  #  MIN,MAX=Go2MinMax.Intervalo(dim,fchoice)

